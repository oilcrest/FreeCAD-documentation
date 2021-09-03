---
- GuiCommand:/sv   Name:Draft Point   Name/sv:Draft Point   Workbenches:[Arch](Draft_Workbench/sv___Draft]],_[[Arch_Workbench/sv.md)|MenuLocation:Draft -> Point   Shortcut:P T---


</div>

#### Beskrivning

The <img alt="" src=images/Draft_Point.svg  style="width:24px;"> **Draft Point** command creates a simple point. Draft points can be useful as a reference for placing lines, wires or other objects.

<img alt="" src=images/Draft_point_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

## Bruk


</div>

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Point.svg" width=16px> [Draft Point](Draft_Point.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Point.svg" width=16px> Point** option from the menu.
2.  The **Point** task panel opens. See [Options](#Options.md) for more information.
3.  Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   The **Relative** checkbox has no purpose for this command.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after finishing, allowing you to continue creating points.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.

## Notes

-   Use <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Draft Snap Near](Draft_Snap_Near.md) to snap to Draft points.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Point object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **X|Distance**: specifies the X coordinate of the point.

-    **Y|Distance**: specifies the Y coordinate of the point.

-    **Z|Distance**: specifies the Z coordinate of the point.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Skript


</div>

To create a Draft Point use the `make_point` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makePoint` method.


```python
point = make_point(X=0, Y=0, Z=0, color=None, name="Point", point_size=5)
point = make_point(point, Y=0, Z=0, color=None, name="Point", point_size=5)
```

-   Creates a `point` object in the specified `X`, `Y` and `Z` coordinates, with units in millimeters. If no coordinates are given the point is created at the origin (0,0,0).
    -   If `X` is a `point` defined by a `FreeCAD.Vector`, it is used.

-    `color`is a tuple `(R, G, B)` that indicates the color of the point in the RGB scale; each value in the tuple should be in the range from `0` to `1`.

-    `name`is the name of the object.

-    `point_size`is the size of the object in pixels, if the graphical user interface is loaded.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

point1 = Draft.make_point(1600, 1400, 0)

p2 = App.Vector(-3200, 1800, 0)
point2 = Draft.make_point(p2, color=(0.5, 0.3, 0.6), point_size=10)

doc.recompute()
```

Example:

This code creates `N` random points within a square of side `2L`. It makes a loop creating `N` points, that may appear anywhere from `-L` to `+L` on both X and Y. It also chooses a random color and size for each point. Change `N` to change the number of points, and change `L` to change the area covered by the points.


```python
import random
import FreeCAD as App
import Draft

doc = App.newDocument()

L = 1000
centered = App.Placement(App.Vector(-L, -L, 0), App.Rotation())
rectangle = Draft.make_rectangle(2*L, 2*L, placement=centered)

N = 10
for i in range(N):
    x = 2*L*random.random() - L
    y = 2*L*random.random() - L
    z = 0
    r = random.random()
    g = random.random()
    b = random.random()
    size = 15*random.random() + 5
    Draft.make_point(x, y, z, color=(r, g, b), point_size=size)

doc.recompute()
```





 