 {{VeryImportantMessage|(Novembre 2018) Ces informations peuvent être incomplètes et obsolètes. Pour la dernière API, consultez [https://www.freecadweb.org/api autogenerated API documentation].}} Ces fonctions font partie de l\'[Atelier TechDraw](TechDraw_Workbench/fr.md) et peuvent être utilisées dans [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) une fois que le module `TechDraw` a été importé.

Good examples of basic TechDraw scripting can be found in the [unit test scripts](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/TDTest).

See the [TechDrawGui API](TechDrawGui_API.md) for more functions.

Example: 
```python
import FreeCAD
import TechDraw

page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage', 'Page')
FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate', 'Template')
FreeCAD.ActiveDocument.Template.Template = templateFileSpec
FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template
page.ViewObject.show()
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart', 'View')
rc = page.addView(view)
```


{{APIFunction|EdgeWalker|listOfEdges, [bool]|Creates wires from edges in input by planar graph traversal.  Optionally exclude the OuterWire by setting optional parameter to false.|List of wires sorted by size (descending)}}


{{APIFunction|findOuterWire|listOfEdges|Finds the OuterWire (largest) of a list of edges (that form a planar graph).|Outer wire}}


{{APIFunction|findShapeOutline|TopoShape, scale, direction|Project shape in direction and find outer wire of result.|Outline wire}}


{{APIFunction|viewPartAsDxf|DrawViewPart|Return the edges of a DrawViewPart in Dxf format.|String}}

Example: 
```python
fileSpecDxf = "fcOut.dxf"
v = App.ActiveDocument.View
s = TechDraw.viewPartAsDxf(v)
dxfEnd = "0\nEOF\n"
dxfFile = open(fileSpecDxf, "w")
dxfFile.write(s)
dxfFile.write(dxfEnd)
dxfFile.close()
```


{{APIFunction|viewPartAsSvg|DrawViewPart|Return the edges of a DrawViewPart in Svg format.|String}}

Example: 
```python
fileSpecSvg = "fcOut.svg"
v = App.ActiveDocument.View
s = TechDraw.viewPartAsSvg(v)
head = '<svg\n' + \
       '    xmlns="http://www.w3.org/2000/svg" version="1.1" \n' + \
       '    xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace">\n'
tail = '\n</svg>'
svgFile = open(fileSpecSvg, "w")
svgFile.write(head)
svgFile.write(s)
svgFile.write(tail)
svgFile.close()
```


{{APIFunction|writeDXFView|DrawViewPart, FileName|Save the DrawViewPart in Dxf.|File}}

Example: 
```python
import TechDraw
TechDraw.writeDXFView(myPart,myFileName)
```


{{APIFunction|writeDXFPage|DrawPage, FileName|Save the DrawPage in Dxf.|File}}

Example: 
```python
import TechDraw
TechDraw.writeDXFPage(myPage,myFileName)
```

### DrawViewPart Cosmetics 

#### CosmeticVertex (CV) routines accessible from Python 

dvp = App.ActiveDocument.View \#CV\'s belong to views
add a CosmeticVertex at p1 (View coordinates). Returns unique tag.
tag = dvp.makeCosmeticVertex(vector p1)

add a CosmeticVertex at p1 (3d model coordinates). Returns unique tag.
tag = dvp.makeCosmeticVertex3d(vector p1)

returns CosmeticVertex with unique id.
cv = dvp.getCosmeticVertex(string id)

returns CosmeticVertex with name (Vertex6). Used in selections.
cv = dvp.getCosmeticVertexBySelection(string name)

remove CosmeticVertex from View. Returns None.
dvp.removeCosmeticVertex(object cv)

remove all CosmeticVertices from the View. Returns None.
dvp.clearCosmeticVertices()

CosmeticView attributes
Tag: unique identifier. String.
Point: location within view. Vector.

-   -   


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Py CosmeticVertex demo
import FreeCAD
import TechDraw

v = App.ActiveDocument.View
p = App.Vector(-3.0, -3.0, 0.0)

#make CV
tag = v.makeCosmeticVertex(p)
print("t: {}".format(tag))

#retrieve CV
cv = v.getCosmeticVertex(tag)
print("cv: {}".format(cv))
print("Tag: {}".format(cv.Tag))


cv2 = v.getCosmeticVertexBySelection("Vertex4")
print("New Point: {}".format(cv2.Point))

#make CV from 3d
p3d = App.Vector(2.0, 2.0, 2.0)
print("3d point in: {}".format(p3d))
tag3d = v.makeCosmeticVertex3d(p3d)
cv3 = v.getCosmeticVertex(tag3d)
print("3d point out: {}".format(cv3.Point))
```

#### CosmeticEdge (CE) routines accessible from Python 

dvp = App.ActiveDocument.View \#CE\'s belong to views
Make a CosmeticEdge from p1 to p2(View coordinates). Returns unique tag.
tag = dvp.makeCosmeticLine(p1, p2)

Make a CosmeticEdge at center with radius radius(View coordinates). Returns unique tag.
tag = dvp.makeCosmeticCircle(center, radius)

Make a CosmeticEdge at center with radius radius(View coordinates) from start angle to end angle. Returns unique tag.
tag = dvp.makeCosmeticCircleArc(center, radius, start, end)

returns CosmeticEdge with unique id.
ce = dvp.getCosmeticEdge(id)

returns CosmeticEdge by name (Edge25). Used in selections.
ce = dvp.getCosmeticEdgeBySelection(name)

remove CosmeticEdge ce from View. Returns None.
dvp.removeCosmeticEdge(ce)

remove all CosmeticLines from the View. Returns None.
dvp.clearCosmeticEdges()

CosmeticEdge attributes
Tag: unique identifier. String.
Format: appearance attributes (style, color, weight, visible). Tuple.

-   -   


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Py CosmeticEdge demo
import FreeCAD
import TechDraw

#points
org = App.Vector(0.0, 0.0, 0.0)
midTop = FreeCAD.Vector (1.0, 5.0, 0.0)   # middle, top
midBot = FreeCAD.Vector(2.0, -5.0, 0.0)      # middle, bottom
stdZ = FreeCAD.Vector(0.0, 0.0, 1.0)
center = FreeCAD.Vector(0.0, 0.0, 0.0)
arcCenter = FreeCAD.Vector(3.0, 3.0, 0.0)
vPt = FreeCAD.Vector(-3.0, 3.0, 0.0)
topRight = FreeCAD.Vector(5.0, 5.0, 0.0)
bottomLeft = FreeCAD.Vector(-5.0, -5.0, 0.0)

#angles
arcStart = -45
arcEnd = 45

#styles
solid = 1 
dashed = 2
dotted = 3
#weights
weight15 = 0.15
weight75 = 0.75
#colors
pyRed = (1.0, 0.0, 0.0, 0.0)
pyBlue = (0.0, 1.0, 0.0, 0.0)
pyGreen = (0.0, 0.0, 1.0, 0.0)
pyBlack = (0.0, 0.0, 0.0, 0.0)
shadow = (0.1, 0.1, 0.1, 0.0)

radius = 5.0
style = dashed
weight = weight75

dvp = App.ActiveDocument.View

print(dvp)

print("making line")
tag = dvp.makeCosmeticLine(midTop,midBot,style, weight, pyBlue)
ce = dvp.getCosmeticEdge(tag)
print("line tag: {}".format(tag))

print("making diagonal")
dvp.makeCosmeticLine(bottomLeft,topRight,solid, weight, pyGreen)

print("making circle")
tag2 = dvp.makeCosmeticCircle(center, radius, style, weight, pyRed)
ce2 = dvp.getCosmeticEdge(tag2)

print("making circleArc")
dvp.makeCosmeticCircleArc(arcCenter, radius, arcStart, arcEnd, style, weight, shadow)

#replace
print("making new format")
oldFormat = ce.Format
newFormat = (dotted,oldFormat[1], pyRed, True)
ce.Format = newFormat

print("removing CE with tag: {}".format(tag2))
dvp.removeCosmeticEdge(tag2)

print("finished")
```

#### CenterLine (CL) routines accessible from Python 

make a new CenterLine
tag = dvp.makeCenterLine(subObjs, mode)
retrieve CenterLine with unique tag.
cl = dvp.getCenterLine(tag)

retrieve CenterLine by subobject name. Used in selection.
cl = dvp.getCenterLine(\"Edge5\")

remove CenterLine cl from View. Returns None.
dvp.removeCenterLine(cl)

CenterLine Attributes
Tag: unique identifier. String. ReadOnly.
Type: 0 - face, 1 - 2 line, 2 - 2 point. Integer. ReadOnly.
Mode: 0 - vert, 1 - horiz, 2 - aligned. Integer.
Format: appearance attributes (style, color, weight, visible). Tuple.
HorizShift: left/right offset. Float.
VertShift: up/down offset. Float.
Rotation: rotation in degrees. Float.
Extension: additional length to be added. Float.
Flip: reverse the order of points for 2 point CenterLine. Boolean.
Edges: names of source edges. List of string.
Faces: names of source faces. List of string.
Points: names of source points (Vertices). List of string.

-   -   


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Py CenterLine demo
import FreeCAD
import Part
import TechDraw

start = FreeCAD.Vector (1.0, 5.0, 0.0)   # middle, top
end = FreeCAD.Vector(1.0, -5.0, 0.0)      # middle, bottom
faceNames = ["Face0"]
edgeNames = ["Edge2", "Edge3"]
vertNames = ["Vertex1", "Vertex2"]
vMode = 0   #vertical
hMode = 1   #horizontal
aMode = 2   #aligned
#styles
solid = 1 
dashed = 2
dotted = 3
#weights
weight15 = 0.15
weight75 = 0.75
#colors
pyRed = (1.0, 0.0, 0.0, 0.0)
pyBlue = (0.0, 1.0, 0.0, 0.0)
pyBlack = (0.0, 0.0, 0.0, 0.0)
#adjustments
hShift = 1.0
vShift = 1.0
extend = 4.0
rotate = 30.0
flip = False;

dvp = App.ActiveDocument.View

print("making face CenterLine")
tag = dvp.makeCenterLine(faceNames,vMode)
cline = dvp.getCenterLine(tag)
print("cline tag: {}".format(tag))

#replace
print("making new format")
oldFormat = cline.Format
newFormat = (dotted,oldFormat[1], pyRed, True)
cline.Format = newFormat
cline.Extension = 10.0

print("making edgeCenterLine")
cline2 = dvp.makeCenterLine(edgeNames,hMode)

print("making vertexCenterLine")
cline3 = dvp.makeCenterLine(vertNames,aMode)

print("finished")
```

### DrawViewPart Geometry 

\[topoShapeEdge\] = dvp.getVisibleEdges()

\[topoShapeEdge\] = dvp.getHiddenEdges()

topoShapeEdge = dvp.getEdgeByIndex(i)
topoShapeEdge = dvp.getEdgeBySelection(\"Edge1\")

topoShapeVertex = dvp.getVertexByIndex(i)
topoShapeVertex = dvp.getVertexBySelection(\"Vertex1\")

dvp.requestPaint() Redraw the graphic for this View.


{{TechDraw Tools navi

}}  

[Category:API{{\#translation:}}](Category:API.md) [Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md)