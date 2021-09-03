---
- GuiCommand:
   Name:SheetMetal AddRelief
   MenuLocation:SheetMetal → Make Relief
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**S** **R**
---

## Description

The <img alt="" src=images/SheetMetal_Relief.svg  style="width:24px;"> **SheetMetal AddRelief** command\...

 <img alt="" src=images/PostRelief.png  style="width:320px;">  
*Create relief for sheet metal bend*

## Usage

To add relief to corner of bend:

1.  Start with a base plate or sheet, select a corner vertex to apply relief
2.  Click on the <img alt="" src=images/SheetMetal_Relief.svg  style="width:24px;"> **Relief** tool to add relief cut to corner.


**Note**

: The workbench does not have a tool to create a base plate, so you need to start your model with one of the following methods:

:\* Method 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box.md)

:\* Method 2: An extruded solid made with <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrude](Part_Extrude.md) from either a:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle.md) or a

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md) or a

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md)

::\* Use <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Part Thickness](Part_Thickness.md) to create shell (**Typically with the thickness value of the sheet metal.**)

:\* Method 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md) containing either an

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [additive box](PartDesign_AdditiveBox.md) or a

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md) made from a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md).

::\* Use <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> [PartDesign Thickness](PartDesign_Thickness.md) to create shell (**Typically with the thickness value of the sheet metal.**)

:   

    :   If you start with a <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Body, you can mix Sheet Metal features with PartDesign features such as <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [pockets](PartDesign_Pocket.md) or <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [holes](PartDesign_Hole.md).

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Relief object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: \"Base Object\". Links to the corner vertexes defining relief positions.

-    **relief|Length**: \"Relief Size\". Default: {{value|2,00 mm}}.






[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)