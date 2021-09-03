---
- GuiCommand:/es
   Name:Sketcher ConstrainDistanceX
   Name/es:Restricción de distancia horizontal
   Workbenches:[Sketcher](Sketcher_Workbench/es.md)
   MenuLocation:Sketch → Restricciones de croquis  → Restricción de distancia horizontal
   Shortcut:May + H
   SeeAlso:[Restricción de longitud](Sketcher_ConstrainDistance/es.md), [Restricción de distancia vertical](Sketcher_ConstrainDistanceY/es.md)
---


</div>


<div class="mw-translate-fuzzy">

## Descripción

Fija la distancia horizontal entre dos puntos o los fines de una línea. Si sólo un objeto es seleccionado, la distancia se fija respecto al origen.


</div>

Fixes the horizontal distance between 2 points or line ends. If only one point is selected, the distance is set to the sketch origin.

![](images/Constraint_H_Distance.png )


<div class="mw-translate-fuzzy">

#### Uso

1.  Selecciona uno o dos puntos
2.  Activa la restricción





</div>

1.  Pick one or two points or one line.
2.  Invoke the tool several ways:
    -   Press the **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Constrain horizontal distance](Sketcher_ConstrainDistanceX.md)** button in the toolbar.
    -   Use the **Shift** + **H** keyboard shortcut. (**H** is for **H**orizontal)
    -   Use the **Sketch → Sketcher constraints → <img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> Constrain horizontal distance** from the top menu.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate.


<div class="mw-translate-fuzzy">

**Note:** the constraint tool can also be started with no prior selection, but will require selection of two points or one line. To set the distance to the origin, the sketch origin point needs to be selected as well. By default the command will be in continue mode to create new constraints; press the right mouse button or **ESC** once to quit the command.


</div>

## Scripting

Distance from origin:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Distance between two vertices:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Horizontal span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1`, `Edge2`, `Edge`, ` PointOfEdge1`, ` PointOfEdge2`, `PointOfEdge` and `Line`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}  