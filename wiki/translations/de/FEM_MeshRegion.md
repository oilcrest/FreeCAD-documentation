---
- GuiCommand   */de
   Name   *FEM MeshRegion
   Name/de   *FEM Netzbereich
   MenuLocation   * Netz → FEM mesh region
   Workbenches   *[FEM](FEM_Workbench/de.md)
   SeeAlso   *[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM MeshRegion/de

## Beschreibung

FEM MeshRegion enables the user to set a localized set of meshing parameters by selecting a set of elements (Vertex, Edge, Face) and applying the parameters to it. It is especially useful for refining meshes in areas of interest or areas where the solver will generate stronger gradient of a variable. For example, it can be used to refine the mesh around stress-risers (sharp edges, circles\...) in mechanical analysis, or at areas of contraction in a fluid flow.

Refining the mesh has the advantage of enabling accurate simulation where needed, while allowing coarser mesh in the wider domain, thus drastically optimizing the computation time while maintaining meaningful solutions output.

## Anwendung

1.  To enable the function a mesh must be first provided <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width   *32px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md).
    -   Select the Mesh object in the Model Tree and press the <img alt="" src=images/FEM_MeshRegion.svg  style="width   *32px;"> button.
    -   Select the Mesh object in the Model Tree and select the **Mesh → <img src="images/FEM_MeshRegion.svg" width=32px> FEM mesh region** option from the menu.
2.  Edit the maximal element size for the region.
3.  Click the **OK** button.
4.  Close the task.

       *   Result   * You now should see a new `FEMMeshRegion` object under the `FEMMeshGMSH` object (see example #3 below) in your active analysis container.
5.  Double-click on the `FEMMeshGMSH` parent object in your Model Tree and press **Apply** to force a mesh recalculation.
6.  Close the task.

Nachdem das Netz generiert wurde, kann der [Eigenschafteneditor](Property_editor/de.md) verwendet werden, um seine Eigenschaften anzupassen. Nach Änderung einer Eigenschaft, muss der Aufgabenbereich FEM-Netz durch Gmsh erneut geöffnet und die Schaltfläche **Anwenden** gedrückt werden. (Der Aufgabenbereich kann geöffnet bleiben, solange weitere Eigenschaften geändert werden.)

Es können so viele unterschiedliche Netzbereiche wie nötig erstellt werden.

## Visual examples 

<img alt="" src=images/FEMMeshRegion_Example1.png style="width   *300px;"> 
*Beispiel 1   * Das grobe Start-FEMMeshGMSH*

<img alt="" src=images/FEMMeshRegion_Example2.png  style="width   *300px;"> 
*Example 2   * After applying a Mesh refinement using two FEMMeshRegion, the large hole is refined to a maximum element size of 3 mm, the smaller hole is refined to 1 mm*

<img alt="" src=images/FEMMeshRegion_Example3.png  style="width   *300px;"> 
*Beispiel 3   * Ein einfaches Beispiel des entstehenden Modellbaums*

## Hinweise

The order in which the regions are shown in [Tree view](Tree_view.md) could change the mesh result. See this [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=41955).

## Related

-   \"Mesh Regions for a Better Analysis\" - Video Tutorial by Joko Engineering ([link](https   *//www.youtube.com/watch?v=X5RVe2SDPvw))





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshRegion/de