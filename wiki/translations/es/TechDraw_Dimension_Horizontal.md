---
- GuiCommand:/es
   Name:TechDraw  Dimension Horizontal
   Name/es:TechDraw  Dimensión Horizontal
   MenuLocation:TechDraw →  Dimensión Horizontal
   Workbenches:[TechDraw](TechDraw_Workbench/es.md)
   Shortcut:**Shift** + **H**
   SeeAlso:[TechDraw Dimensión Longitud](TechDraw_Dimension_Length/es.md), [TechDraw Dimensión Vertical](TechDraw_Dimension_Vertical/es.md)
---


</div>

## Descripción

The Dimension Horizontal tool adds a horizontal dimension to a View. The dimension may be between two vertices, the length of one edge or the horizontal distance between 2 edges. The distance will initially be the projected distance (ie as shown on the drawing), but this may be changed to the actual 3D distance using the **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Link Dimension](TechDraw_Dimension_Link.md)** tool.

<img alt="" src=images/TechDraw_Dimension_Horizontal_example.png  style="width:200px;"> 
*Length dimension taken from two arbitrary nodes of the view; the distance is measured horizontally*

## Utilización

1.  Select the points or edge which define your measurement.
2.  Press the **<img src="images/TechDraw_Dimension_Horizontal.svg" width=16px> [Dimension Horizontal](TechDraw_Dimension_Horizontal.md)** button
3.  A dimension will be added to the View. The dimension may be dragged to the desired position.
4.  If needed, add tolerances as described in [this page](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerances.md).

To change the properties of a dimension object either double-clicking it in the drawing or in the [Tree view](Tree_view.md). This will open the [dimension dialog](TechDraw_Dimension_Length#Dimension_dialog.md).

## Limitaciones

Dimension objects are vulnerable to \"topological naming\" issues. See the information in the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool for more information.

## Propiedades

This object has the same properties as the [TechDraw Dimension Length](TechDraw_Dimension_Length.md) tool. See that tool for details.

## Guión


**See also:**

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Dimension Horizontal tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  