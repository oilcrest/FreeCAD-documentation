---
- GuiCommand:/de
   Name:SheetMetal Unfold
   Name/de:SheetMetal Abwickeln
   MenuLocation:SheetMetal → Unfold
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**U**
   SeeAlso:[SheetMetal UnattendedUnfold](SheetMetal_UnattendedUnfold/de.md)
---

# SheetMetal Unfold/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **Abwickeln** wickelt ein Blechobjekt ab.

## Anwendung

To unfold a sheet metal part:

1.  Switch to the <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [SheetMetal Workbench](SheetMetal_Workbench.md).
2.  Select a flat face of the sheet metal part. **Note**:the face should be a plane, the thickness should be constant
3.  Click on the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **Unfold** tool to display a menu in task panel to manage unfolding options.
4.  Select projection options of future flattened sketch
5.  Select the rule for bend deduction with [Kfactor](https://github.com/shaise/FreeCAD_SheetMetal#terminology):
    -   Use [Material Definition Sheet](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet)
    -   Or select a manual [Kfactor](https://github.com/shaise/FreeCAD_SheetMetal#terminology) then the ANSI or DIN standard to apply

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

This tool creates an Unfold object and has no representation of its own in the [Tree view](Tree_view.md) or elsewhere and so has no properties.

The **Unfold** object, on the other hand, is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It has no additional properties, but its label has a default value:

### Daten


{{Properties_Title/de|Basis}}

-    **Label|String**: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

## Einschränkungen

-   Blechobjekte sollten eine konstante Wandstärke haben
-   Flat faces should be planar with no split lines
-   Bend angles should be radius with cylindrical faces
-   Das Unfold-Objekt ist bisher nicht parametrisch.




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Unfold/de