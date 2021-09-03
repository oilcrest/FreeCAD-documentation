#!/usr/bin/env python3

#***************************************************************************
#*   Copyright (c) 2021 Yorik van Havre <yorik@uncreated.net>              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

"""
migrate.py - MediaWiki to Markdown migration tool

This tool allows to download all pages and images from a MediaWiki instance,
and save all images and pages as markdown files. It keeps track of page versions,
so it can update an existing download by just updating what has changed.

Basic command-line usage:
-------------------------

    migrate.py --init

    See bottom of file for available functions

Basic Python usage:
-------------------

    from migrate import MediaWiki
    wiki = MediaWiki([url])
    wiki.init() # do this the first time. You can interrupt and resume init() later
    wiki.update() # do this next times

Detailed Python usage:
----------------------

First time:

    from migrate import MediaWiki
    wiki = MediaWiki(url="https://wiki.freecadweb.org")
    wiki.getPageNames() # not strictly needed, done automatically by next step
    wiki.getAllPages() # this writes to disk cache, so it can be interrupted/resumed
    wiki.writeAllPages() # write md files
    wiki.getAllImages() # fetches and saves all images

You will get two json files a text cache and a revision set.

Next times:

    from migrate import MediaWiki
    wiki = MediaWiki(url="https://wiki.freecadweb.org") # this loads filecache.json
    oldrevisions = wiki.readRevisions() # this loads the latest revision set
    wiki.getPageNames() # this fetches new page names, if any
    newrevisions = wiki.getRevisions()
    wiki.updateRevisions(oldrevisions,newrevisions) # this writes to disk cache like getAllPages
    wiki.writeAllPages() # write md files
    wiki.getAllImages() # fetches and saves all images - existing ones are not overwritten
"""

import requests
import sys
import os
import re
import json
import datetime
import pypandoc

class MediaWiki:

    """MediaWiki([url]) - A class to represent an online MediaWiki instance.
       default url is wiki.freecadweb.org"""

    def __init__(self,url="https://wiki.freecadweb.org"):

        if not url.endswith("api.php"):
            if not url.endswith("/"):
                url += "/"
            url += "api.php"
        self.url = url
        self.cachefile = os.path.join(os.path.dirname(__file__),"cache.json")
        self.session = requests.Session()
        self.pagenames = []
        self.pagecount = 0
        self.pagecontents = {}
        self.readCache()
        self.imagecount = 0
        self.images = {}
        self.output = os.path.join(os.path.dirname(__file__),"wiki")
        if not os.path.exists(self.output):
            os.mkdir(self.output)
        self.imagefolder = "images"
        self.translationfolder = "translations"

    ### MAIN TOOLS


    def init(self):

        """init():
        Performs an initial import of the pages and images.
        If a cache already exists, it will be fully overwritten."""

        self.getPageNames()
        self.getAllPages()


    def update(self):

        """update():
        Performs initial import if running for the first time,
        or updates the contents if a cache already exists"""

        if not self.pagecontents:
            self.init()
        oldrevisions = self.readRevisions()
        self.getPageNames()
        newrevisions = self.getRevisions()
        self.updateRevisions(oldrevisions,newrevisions)


    ### UTILS


    def printProgress(self,count=None,total=100,text=""):

        """printProgress([count,total,text]):
        Prints a progress bar indicating the current progresses (count/total)
        and optionally an info text. Calling printProgress() terminates with a
        newline"""

        sys.stdout.flush()
        if count is None:
            sys.stdout.write("\r"+" ".ljust(72)+"\r")
            return
        sys.stdout.write(('\r'+text+' '+str(int((count/total)*100))+'%').ljust(72))


    ### CACHE OPERATIONS


    def writeCache(self):

        """writeCache():
        Writes the contents of self.pagecontents to disk"""

        if self.pagecontents:
            with open(self.cachefile,'w',encoding='utf8') as jfile:
                json.dump(self.pagecontents, jfile, ensure_ascii = False)


    def readCache(self):

        """readCache():
        Reads the contents of self.pagecontents from disk"""

        if os.path.exists(self.cachefile):
            with open(self.cachefile) as jfile:
                self.pagecontents = json.load(jfile)
                self.pagenames = self.pagecontents.keys()
                self.pagecount = len(self.pagecontents)


    ### PAGE OPERATIONS


    def getPageCount(self):

        """getPageCount():
        Returns the number of content pages.
        Also stores the total in self.pagecount"""

        params = { "action": "query",
                   "meta": "siteinfo",
                   "formatversion": "2",
                   "format": "json",
                   "siprop": "statistics",
                 }
        result = self.session.get(url=self.url, params=params)
        data = result.json()
        pagecount = data["query"]["statistics"]["articles"]
        self.pagecount = pagecount
        return pagecount


    def getPageNames(self):

        """getPageNames():
        Returns a list of all pages of the wiki.
        Also stores the list in self.pagenames"""

        pages = []
        count = 1
        apfrom = None
        params = { "action": "query",
                   "format": "json",
                   "list": "allpages",
                   "aplimit": "500",
                 }
        if not self.pagecount:
            self.getPageCount()
        while True:
            self.printProgress(len(pages),self.pagecount,"Getting pages list...")
            if apfrom:
                params["apfrom"] = apfrom
            else:
                if "apfrom" in params:
                    break
            result = self.session.get(url=self.url, params=params)
            data = result.json()
            pages.extend([page["title"].replace(" ","_") for page in data["query"]["allpages"]])
            apfrom = None
            if "continue" in data:
                if "apcontinue" in data["continue"]:
                    if data["continue"]["apcontinue"]:
                        apfrom = data["continue"]["apcontinue"]
                        count += 1
        self.printProgress()
        self.pagenames = pages
        self.pagecount = len(self.pagenames)
        return pages


    def getPage(self,name):

        """getPage(name):
        Returns the wiki content of a page and a revision ID.
        Also stores it in self.pagecontents[name]"""

        params = { "action": "parse",
                   "format": "json",
                   "page": name,
                   "prop": "wikitext|revid",
                   "formatversion": "2",
                 }
        result = self.session.get(url=self.url, params=params)
        data = result.json()
        wikitext = data["parse"]["wikitext"]
        revision = data["parse"]["revid"]
        self.pagecontents[name] = wikitext
        return wikitext,revision


    def getAllPages(self,pageset=None):

        """getAllPages([pageset])
        Gets the contents of all of the wiki pages
        and stores everything in self.pagecontents. If pageset is
        not given, all pages from self.pagenames are retrieved"""

        revfile = os.path.join(os.path.dirname(__file__),"revisions_tmp.json")
        revisions = self.readRevisions(revfile)
        overwrite = True
        if not pageset:
            overwrite = False
            if not self.pagenames:
                self.getPageNames()
            pageset = self.pagenames
        count = 1
        for page in pageset:
            self.printProgress(count,len(pageset),"Getting page "+page+"...")
            if overwrite or (not page in self.pagecontents):
                text,revid = self.getPage(page)
                revisions[page] = revid
                if count % 10 == 0:
                    self.writeCache()
                    self.writeRevisions(revisions,revfile)
            count += 1
        self.writeCache()
        self.printProgress()
        if os.path.exists(revfile):
            os.remove(revfile)
        self.writeRevisions(revisions)
        return revisions


    ### IMAGE OPERATIONS


    def getImageCount(self):

        """getImageCount():
        Returns the number of images.
        Also stores the total in self.imagecount"""

        params = { "action": "query",
                   "meta": "siteinfo",
                   "formatversion": "2",
                   "format": "json",
                   "siprop": "statistics",
                 }
        result = self.session.get(url=self.url, params=params)
        data = result.json()
        imagecount = data["query"]["statistics"]["images"]
        self.imagecount = imagecount
        return imagecount


    def getImageNames(self):

        """getImageNames():
        Returns a list of all images of the wiki.
        Also stores the paths in self.images"""

        images = {}
        count = 1
        aifrom = None
        params = { "action": "query",
                   "format": "json",
                   "list": "allimages",
                   "ailimit": "100",
                 }
        if not self.imagecount:
            self.getImageCount()
        while True:
            self.printProgress(count,self.imagecount,"Getting images list...")
            if aifrom:
                params["aifrom"] = aifrom
            else:
                if "aifrom" in params:
                    break
            result = self.session.get(url=self.url, params=params)
            data = result.json()
            for image in data["query"]["allimages"]:
                images[image["name"]] = image["url"]
                count += 1
            aifrom = None
            if "continue" in data:
                if "aicontinue" in data["continue"]:
                    if data["continue"]["aicontinue"]:
                        aifrom = data["continue"]["aicontinue"]
        self.printProgress()
        self.images = images
        self.imagecount = len(self.images.keys())
        return images


    def getImage(self,name,overwrite=False,basepath=None):

        """getImage(name,[overwrite,basepath]):
        Downloads and saves the given image in an images subfolder.
        If no basepath is given, the current dir is used.
        If overwrite is True, file is downloaded again"""

        if not basepath:
            basepath = self.output
        basedir = os.path.join(basepath,self.imagefolder)
        if not os.path.isdir(basedir):
            os.mkdir(basedir)
        filename = os.path.join(basedir,name)
        if overwrite or (not os.path.exists(filename)):
            filecontents = requests.get(self.images[name])
            with open(filename,"wb") as imagefile:
                imagefile.write(filecontents.content)


    def getAllImages(self,overwrite=False,basepath=None):

        """getAllImages([overwrite]):
        Saves all images to disk.
        If no basepath is given, the current dir is used.
        If overwrite is True, file is downloaded again"""

        if not basepath:
            basepath = self.output
        if not self.images:
            self.getImageNames()
        count = 1
        for name in self.images.keys():
            self.printProgress(count,self.imagecount,"Downloading "+name+"...")
            self.getImage(name,overwrite,basepath)
            count += 1


    ### REVISION OPERATIONS


    def getRevisions(self):

        """getRevisions():
        Returns a list of revisions for the pages stored in self.pagenames"""

        revisions = {}
        count = 1
        apfrom = None
        params = { "action": "query",
                   "format": "json",
                   "prop": "revisions",
                   "rvprop": "ids",
                   "rvslots": "main",
                   "formatversion": "2",
                 }
        if not self.pagenames:
            self.getPageNames()
        self.printProgress(0,100,"Getting pages revisions...")
        titles = ""
        for page in self.pagenames:
            if titles:
                titles += "|"
            titles += page
            count += 1
            if count % 10 != 0:
                params["titles"] = titles
                result = self.session.get(url=self.url, params=params)
                data = result.json()
                for page in data["query"]["pages"]:
                    if "revisions" in page:
                        revisions[page["title"]] = page["revisions"][0]["revid"]
                self.printProgress(count,self.pagecount,"Getting pages revisions...")
                titles = ""
        self.printProgress()
        return revisions


    def writeRevisions(self,revisions,filename=None):

        """writeRevisions(revisions,[filename]):
        Writes the contents of revisions to disk. If no filename is
        given, one is created automatically from the current timestamp"""

        if not filename:
            d = str(datetime.datetime.now())
            fp = os.path.dirname(__file__)
            filename = os.path.join(fp,"revisions_"+d+".json")
        with open(filename,'w',encoding='utf8') as jfile:
            json.dump(revisions, jfile, ensure_ascii = False)


    def readRevisions(self,filename=None):

        """readRevisions([filename]):
        Returns a revisions dictionary previously stored in a file. If
        no filename is given, the latest one is taken"""

        data = {}
        if not filename:
            files = os.listdir(os.path.dirname(__file__))
            jsonfiles = [f for f in files if (f.endswith(".json") and f.startswith("revision"))]
            jsonfiles.sort(key=os.path.getmtime, reverse=True)
            filename = os.path.join(os.path.dirname(__file__),jsonfiles[0])
            print("Opening",filename)
        if os.path.exists(filename):
            with open(filename) as jfile:
                data = json.load(jfile)
        return data


    def updateRevisions(self,oldrevision,newrevision):

        """updateRevisions(oldrevision,newrevision):
        Reads again the pages that need an update"""

        pageset = []
        for page,revid in newrevision.items():
            if page in oldrevision:
                if oldrevision[page] == revid:
                    continue
            pageset.append(page)
        self.getAllPages(pageset)


    ### MARKDOWN OPERATIONS


    def getMarkdown(self,wikitext,clean=True):

        """getMarkdown(wikitext,[clean]):
        Returns a markdown version of a text in wiki format.
        If clean is false, raw pandoc output is returned"""

        xargs = ['--atx-headers'] # pandoc arguments
        try:
            fmt = 'markdown+hard_line_breaks'
            result = pypandoc.convert_text(wikitext, fmt, format='mediawiki', extra_args=xargs)
        except:
            return None
        else:
            if clean:
                return self.cleanMarkdown(result)
            else:
                return result


    def cleanMarkdown(self,mdtext,imagepath=None):

        """cleanMarkdown(mdtext,[imagepath]):
        Returns a cleaned version of the given markdown text.
        Imagepath indicates the location of images relative to this page
        (default = "images")"""

        result = mdtext
        flags = re.DOTALL|re.MULTILINE
        if not imagepath:
            imagepath = self.imagefolder

        # templates that are safe to remove entirely
        unusedtemplates = ["Userdocnavi","Arch Tools navi","\\#translation:","clear",
                           "Part Tools navi","Draft Tools navi",
                          ]

        # path replacements
        result = re.sub("\!\[(.*?)\]\(",r"![\1]("+imagepath+"/",result) # add /image to image paths
        result = re.sub(" \"wikilink\"",".md",result) # add .md to wiki page links

        # template that are simply removed
        result = re.sub("\`.*?\`\{\=html\}","",result)
        result = re.sub("<!--.*?-->","",result,flags=flags)
        result = re.sub("{{Docnav.*?}}","",result,flags=flags)
        result = re.sub("{{Page in progress}}","",result,flags=flags)
        result = re.sub("{{\#translation\:}}","",result,flags=flags)

        # templates that get turned into bold text
        result = re.sub("{{Caption\|(.*?)}}",r"*\1*",result,flags=flags)
        result = re.sub("{{KEY\|(.*?)}}",r"**\1**",result,flags=flags)
        result = re.sub("{{Button\|(.*?)}}",r"**\1**",result,flags=flags)
        result = re.sub("{{MenuCommand\|(.*?)}}",r"**\1**",result,flags=flags)
        result = re.sub("{{PropertyData\|(.*?)}}",r"**\1**",result,flags=flags)
        result = re.sub("{{PropertyView\|(.*?)}}",r"**\1**",result,flags=flags)
        result = re.sub("{{Emphasis\|(.*?)}}",r"**\1**",result,flags=flags)

        # templates that get turned into <small> text
        result = re.sub("{{Version\|(.*?)}}",r"<small>(v\1)</small> ",result,flags=flags)
        result = re.sub("{{version\|(.*?)}}",r"<small>(v\1)</small> ",result,flags=flags)
        result = re.sub("{{VersionPlus\|(.*?)}}",r"<small>(v\1)</small> ",result,flags=flags)

        # templates that get turned into a newline char
        result = re.sub("{{Clear}}",r"\n",result,flags=flags)

        # all other templates are simply converted to normal text (see below)

        # turning GuiCommand block into YAML
        if "{{GuiCommand" in result:
            guicommandblk = re.findall("```{\=mediawiki}.*?{{GuiCommand(.*?)}}\n```",result,flags=flags)
            if guicommandblk:
                guicommandblk = guicommandblk[0]
                guicommandblk = re.sub("\|(.*?)\=(.*?)",r"   \1:\2",guicommandblk) # fixing GuiCommand contents
                result = re.sub("```{\=mediawiki}.*?{{GuiCommand(.*?)}}\n```",r"---\n- GuiCommand:"+guicommandblk+"---\n",result,flags=flags)
                result = "---"+"---".join(result.split("---")[1:]) # removing empty line before yaml block

        # remove code fences
        result = re.sub("\`","",result)
        result = re.sub("\{\=mediawiki\}","",result)
        result = re.sub("\{\:mediawiki\}","",result)

        # creating new code fences
        result = re.sub("{{Code\|code\=(.*?)}}",r"```python\1```",result,flags=flags) # replace {{Code}} templates
        result = re.sub("{{incode\|(.*?)}}",r"`\1`",result,flags=flags) # replace {{incode}} templates
        result = re.sub(" \`\`\`",r" \n```",result,flags=flags) # make sure all ``` are on a new line
        result = re.sub("{{TRUE}}",r"`True`",result,flags=flags) # replace {{TRUE}} templates
        result = re.sub("{{FALSE}}",r"`False`",result,flags=flags) # replace {{TRUE}} templates

        # fixing links
        result = re.sub("(!\[.*?\]\(.*?)\".*?\"(\))",r"\1\2",result) # remove image path descriptions
        for l1 in re.findall("\[\[Image\:.*?\|.*?px\]\]",result):
            iml1 = re.findall("Image\:(.*?)\|",l1)[0]
            iml2 = re.findall("\|(.*?)px\]\]",l1)[0]
            l2 = "<img src=\""+imagepath+"/"+iml1.replace(" ","_")+"\" width="+iml2+"px>"
            result = result.replace(l1,l2)
        result = re.sub("\[\[Image\:(.*?)\|(.*?)\]\]",r"![]("+imagepath+"/\1)",result)
        result = re.sub("\[\[(.*?)\|(.*?)\]\]",r"[\2](\1.md)",result)
        result = re.sub(r"\]\(.*?\.",lambda x:x.group().replace(" ","_"),result) # replace spaces by underscores in all remaining links
        result = re.sub("!\[(.*?)\]\((.*?)\){width=\"(.*?)\"}",r'<img alt="\1" src=\2 style="width:\3px;">',result) # fix img sizes
        #for l in re.findall("\[.*?\]\(.*?\)",result):
        #    print("   ",l)

        # fixing misc formatting glitches
        result = re.sub("\n-   \n","\n-",result,flags=flags) # condensing newlines in bullet point lists
        result = re.sub("\n    \n    ","",result,flags=flags) # condensate empty lines
        result = re.sub("\n\n\n\(v",r" (v",result,flags=flags) # condensate badly formatted version templates
        result = re.sub("\n:\n","",result,flags=flags) # condensate remaining : lines
        result = re.sub("\n\n\n\n-","\n-",result,flags=flags) # condensate bad - lists
        result = re.sub("(<img.*?>.*?)(\*.*?\*\n)",r"\1\n\2",result) # put captions on a newline
        result = re.sub("\[(.*?)\]\(image:(.*?)\.md\)",r"![\1]("+imagepath+r"/\2)",result) # fix image: links
        result = re.sub("\[(.*?)px\]\(File:(.*?)\.md\)",r'<img src='+imagepath+r'/\2 style="width:\1px">',result) # fix File: links

        # removing other leftovers
        result = re.sub("\\_\\_NOTOC\\_\\_","",result,flags=flags) # removing __NOTOC__ entries
        result = re.sub("\{\#.*?\}","",result,flags=flags) # removing {#...} tags

        # removing all remaining templates
        for template in re.findall("{{.*?}}",result,flags=flags):
            if template.strip("{").strip("}").strip() in unusedtemplates:
                result = re.sub(template,"",result,flags=flags) # remove all remaining templates
            else:
                print("WARNING: Unhandled template:",template)

        return result


    def writeMarkdown(self,page,overwrite=True,basepath=None,clean=True):

        """writeMarkdown(page,[overwrite,basepath,clean]):
        Writes the given page as a .md file. If basepath is
        not given, file is written in the current dir.
        If overwrite is False, existing files are skipped.
        If clean is false, raw pandoc output is returned"""

        if not basepath:
            basepath = self.output
        if not os.path.exists(basepath):
            print("base path",basepath,"does not exist")
            return page
        result = self.getMarkdown(self.pagecontents[page],clean)
        if not result:
            print("Error writing page:",page)
            return page
        if "REDIRECT" in result.split("\n")[0]:
            truepage = re.findall("\((.*?)\.md\)",result)
            if not truepage:
                truepage = re.findall("\((.*?)[\"\)]",result)
            if not truepage[0].strip() in self.pagecontents:
                print("Error:redirecting to",truepage[0].strip())
                return page
            result = self.getMarkdown(self.pagecontents[truepage[0].strip()],clean)
        if not result:
            print("Error writing page:",page)
            return page
        else:
            filename = page
            if "/" in filename:
                filename = os.path.join(self.output,self.translationfolder,page.split("/")[-1],page.split("/")[0])
                transpath = os.path.dirname(filename)
                if not os.path.exists(transpath):
                    if not os.path.exists(os.path.join(self.output,self.translationfolder)):
                        os.mkdir(os.path.join(self.output,self.translationfolder))
                    os.mkdir(transpath)
            filename += ".md"
            filename = os.path.join(basepath,filename)
            filename = filename.replace(" ","_")
            if overwrite or (not os.file.exists(filename)):
                with open(filename,"w") as mdfile:
                    mdfile.write(result)
            return None


    def writeAllPages(self,overwrite=True,basepath=None):

        """writeAllPages([overwrite]):
        Writes all pages to markdown files. Returns
        a list of pages which couldn't be written for some reason.
        If basepath is not given, file is written in the current dir.
        If overwrite is False, existing files are skipped"""

        errors = []
        count = 1
        if not basepath:
            basepath = self.output
        for page in self.pagenames:
            self.printProgress(count,len(self.pagenames),"Saving page "+page+"...")
            r = self.writeMarkdown(page,overwrite,basepath)
            if r:
                errors.append(r)
            count += 1
        self.printProgress()
        return errors



### GENERAL FUNCTIONS



def init():

    """performs an initial import"""

    wiki = MediaWiki()
    wiki.init()
    print("All done!")


def update():

    """performs a full update of the local contents from the wiki"""

    wiki = MediaWiki()
    wiki.update()
    print("All done!")


def test():

    """creates a couple of pages for testing"""

    w = MediaWiki()
    w.writeMarkdown("Arch_Workbench")
    w.writeMarkdown("Arch_Wall")
    w.writeMarkdown("Draft_Line")
    w.writeMarkdown("Part_Extrude")
    w.writeMarkdown("Arch_Workbench",basepath=os.path.dirname(__file__)+"/orig",clean=False)
    w.writeMarkdown("Arch_Wall",basepath=os.path.dirname(__file__)+"/orig",clean=False)
    w.writeMarkdown("Draft_Line",basepath=os.path.dirname(__file__)+"/orig",clean=False)
    w.writeMarkdown("Part_Extrude",basepath=os.path.dirname(__file__)+"/orig",clean=False)


def writepages():

    """writes all pages to .md files"""

    wiki = MediaWiki()
    #wiki.update()
    wiki.writeAllPages()


def writeimages():

    """downloads and wrie images. Existing images are skipped"""

    wiki = MediaWiki()
    #wiki.update()
    wiki.getAllImages()






### COMMAND-LINE USAGE



if __name__ == "__main__":

    args = sys.argv[1:]

    # execute function
    if len(args) == 1:
        arg = args[0]
        if arg.startswith("--"):
            arg = arg[2:]
            if arg in globals():
                if callable(globals()[arg]):
                    globals()[arg]()
                    exit(0)

    # print help text
    funcs = "    Available functions:\n"
    for name in list(globals().keys()):
        if (name != "MediaWiki") and callable(globals()[name]):
            funcs += "    --" + name + " : " + globals()[name].__doc__ + "\n"
    print(__doc__.replace("    See bottom of file for available functions",funcs))
