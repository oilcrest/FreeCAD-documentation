# Manual:Creating FEM analyses/ro
{{Manual:TOC/ro}}

MEF înseamnă [Finite Element Method](https://en.wikipedia.org/wiki/Finite_element_method). Este un subiect matematic vast, dar în FreeCAD ne putem gândi la acesta ca la o modalitate de a calcula propagările în interiorul unui obiect 3D, prin tăierea lui în bucăți infinitezimal mici și analizarea impactului fiecărei bucăți mici asupra vecinilor săi. Acest lucru are mai multe utilizări în diverse domenii ale ingineriei în general și al câmpuri electromagnetice ( ca alt exemplu), dar ne vom concentra pe o utilizare deja dezvoltată în FreeCAD, care simulează deformările în obiecte care sunt supuse forțelor și greutăților.


<div class="mw-translate-fuzzy">

Obtaining such simulation is done in FreeCAD with the _ chapter, and finally calculating the simulation.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_01.jpg )


</div>

### Pregătirea FreeCAD 


<div class="mw-translate-fuzzy">

The simulation itself is done by another piece of software, that is used by FreeCAD to obtain the results. As there are several interesting open source FEM simulation applications available, the _.


</div>

### Preparing the geometry 

We will start with the house we modeled in the _ chapter. However, some changes have to be made to make the model suitable for FEM calculations. This involves, basically, discarding the objects that we don\'t want to include in the calculation, such as the door and window, and joining all the remaining objects into one.

-   Load the [house model](https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd) we modeled earlier
-   Delete or hide the page object, the section planes and the dimensions, leaving only our model
-   Hide the window, the door and the ground slab
-   Also hide the metal beams on the roof. They are very different objects from the rest of the house so we will simplify our calculation by not including them. Instead, we will assume that the roof slab is placed directly on top of the wall.
-   Now move the roof slab down so it rests on top of the wall: Edit the **Rectangle** object that we used as a base of the roof slab, and change its **Placement-\>Position-\>X** value from 3.18m to 3.00m
-   Our model is now clean:


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_02.jpg )


</div>


<div class="mw-translate-fuzzy">

-   The FEM Workbench can currently only calculate deformations on a single object. Therefore, we need to join our two objects (the wall and the slab). Switch to the _. We have now obtained a fused object:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_03.jpg )


</div>

### Creating the analysis 


<div class="mw-translate-fuzzy">

-   We are now ready to start a FEM analysis. Let\'s switch to the [FEM Workbench](FEM_Workbench.md)
-   Select the fused object
-   Press the <img alt="" src=images/Fem_Analysis.png  style="width:16px;"> [New Analysis](FEM_Analysis.md) button
-   A new analysis will be created and a settings panels opened. Here you can define the meshing parameters to be used to produce the FEM mesh. The main setting to edit is the **Max Size** which defines the maximum size (in millimeters) of each piece of the mesh. For now, we can leave the default value of 1000:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_04.jpg )


</div>


<div class="mw-translate-fuzzy">

-   After pressing OK and a few seconds of calculation, our FEM mesh is now ready:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_05.jpg )


</div>


<div class="mw-translate-fuzzy">

-   We can now define the material to be applied to our mesh. This is important because depending on the material strength, our object will react differently to forces applied to it. Select the analysis object, and press the <img alt="" src=images/FEM_MaterialSolid.png  style="width:16px;"> [New Material](FEM_MaterialSolid.md) button.
-   A task panel will open to allow us to choose a material. In the Material drop-down list, choose the **Concrete-generic** material, and press OK.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_06.jpg )


</div>


<div class="mw-translate-fuzzy">

-   We are now ready to apply forces. Let\'s start by specifying which faces are fixed into the ground and can therefore not move. Press the <img alt="" src=images/FEM_ConstraintFixed.png  style="width:16px;"> [Constraint fixed](FEM_ConstraintFixed.md) button.
-   Click on the bottom face of our building and press OK. The bottom face is designated as unmovable:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_07.jpg )


</div>


<div class="mw-translate-fuzzy">

-   We will now add a load on the top face, that could represent, for example, a massive weight being placed on the roof. For this we will use a pressure constraint. Press the <img alt="" src=images/FEM_ConstraintPressure.png  style="width:16px;"> [Constraint pressure](FEM_ConstraintPressure.md) button.
-   Click the top face of the roof, set the pressure to **10MPa** (the pressure is applied by square millimeter) and click the OK button. Our force is now applied:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_08.jpg )


</div>


<div class="mw-translate-fuzzy">

-   We are now ready to start the calculation. Select the **CalculiX** object in the tree view, and press the <img alt="" src=images/FEM_ControlSolver.png  style="width:32px;"> [Start Calculation](FEM_SolverControl.md) button.
-   In the task panel that will open, click first the **Write .inp file** button to create the input file for CalculiX, then the **Run CalculiX** button. A few moments later, the calculation will be done:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_09.jpg )


</div>

-   We can now look at the results. Close the task panel, and see that a new **Results** object has been added to our analysis.
-   Double-click the Results object
-   Set the type of result that you want to see on the mesh, for example \"absolute displacement\", tick the **show** checkbox under **Displacement**, and move the slider next to it. You will be able to see the deformation growing as you apply more force:


<div class="mw-translate-fuzzy">

![](images/Exercise_fem_10.jpg )


</div>

The results displayed by the FEM workbench are of course currently not enough to perform real-life decisions about structures dimensioning and materials. However, they can already give precious information about how the forces flow through a structure, and which are the weak areas that will feel the most stress.

**Downloads**

-   The file created during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/fem.FCStd>

**Read more**


<div class="mw-translate-fuzzy">

-   [The FEM Workbench](FEM_Workbench.md)
-   [Installing required FEM components](FEM_Install.md)
-   [CalculiX](http://www.calculix.de)
-   [NetGen](https://sourceforge.net/projects/netgen-mesher)


</div>





{{Tutorials navi

}}

---
[documentation index](../README.md) > Manual:Creating FEM analyses/ro