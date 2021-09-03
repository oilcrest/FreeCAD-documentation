---
- GuiCommand:/fr
   Name:Draft Shape2DView
   Name/fr:Draft Vue 2D d'une forme
   MenuLocation:Modification → Vue 2D de la forme
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
---

## Description

La commande <img alt="" src=images/Draft_Shape2DView.svg  style="width:24px;"> **Draft Vue 2D d\'une forme** crée des projections 2D à partir d\'objets sélectionnés, généralement des solides 3D ou des [Arch Plan de section](Arch_SectionPlane/fr.md). Les projections sont placées dans la [Vue 3D](3D_view/fr.md).

Les projections Vue 2D d\'une forme peuvent être affichées sur une page de l\'[atelier TechDraw](TechDraw_Workbench/fr.md) à l\'aide de la commande [TechDraw Vue Draft](TechDraw_DraftView/fr.md). Par ailleurs, l\'[atelier TechDraw](TechDraw_Workbench/fr.md) offre ses propres commandes de projection, mais celles-ci créent des projections qui ne sont affichées que sur la page de dessin et non dans la [Vue 3D](3D_view/fr.md).

![](images/Draft_Shape2DView_example.jpg ) *Projection de formes solides sur le plan XY*

## Utilisation

1.  Vous pouvez faire la [Vue 3D](3D_view/fr.md). La direction de la caméra dans la [Vue 3D](3D_view/fr.md) détermine le vecteur de projection. Par exemple, une [vue de dessus](Std_ViewTop/fr.md) sera projetée sur le plan XY. Le vecteur de projection est ignoré pour les projections créées à partir de [Arch Plan de section](Arch_SectionPlane/fr.md).
2.  Sélectionnez éventuellement un ou plusieurs objets.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Shape2DView.svg" width=16px> [Créer une projection 2D...](Draft_Shape2DView.md)**.
    -   Sélectionnez l\'option **Modification → <img src="images/Draft_Shape2DView.svg" width=16px> Vue 2D de la forme ** dans le menu.
4.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez un objet dans la [Vue 3D](3D_view/fr.md).
5.  Les objets projetés sont créés sur le plan XY.

## Comment produire des plans et des sections avec des largeurs de ligne différentes 

<img alt="" src=images/Draft_shape2dview_example_plan.png  style="width:700px;">

Des dessins avec des largeurs de ligne différentes pour les lignes vues et coupées peuvent être facilement produits en utilisant deux objets Vue 2D d\'une forme d\'un même [Arch Plan de section](Arch_SectionPlane/fr.md). Un des objets Vue 2D d\'une forme a son mode de projection défini sur **Solide**, qui restitue les lignes vues, et un autre sur **Couper les lignes** ou **Couper les faces** pour rendre la coupe lignes. Les deux Vue 2D d\'une forme sont ensuite placées au même endroit, l\'une au-dessus de l\'autre.

## Propriétés

Voir aussi : [Éditeur de propriétés](property_editor/fr.md).

Un objet Draft Vue 2D d\'une forme est dérivé d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Draft}}

-    {{PropertyData/fr|Base|Link}}: spécifie l\'objet à projeter.

-    {{PropertyData/fr|Face Numbers|IntegerList}}: spécifie les indices des faces à projeter. Ne fonctionne que si {{PropertyData/fr|Projection Mode}} est {{Value|Faces individuelles}}.

-    {{PropertyData/fr|Fuse Arch|Bool}}: spécifie si les [Arch objects](Arch_Workbench.md) de même type et matériau sont fusionnés ou non.

-    {{PropertyData/fr|Hidden Lines|Bool}}: spécifie si les lignes cachées sont affichées ou non.

-    {{PropertyData/fr|In Place|Bool}}: ne fonctionne que si l\'objet sélectionné est un [Arch Plan de section](Arch_SectionPlane/fr.md), et que {{PropertyData/fr|Projection Mode}} est {{Value|Cutlines}} ou {{Value|Cutfaces}}, spécifie si la projection apparaîtra coplanaire avec le plan de section.

-    {{PropertyData/fr|Projection|Vector}}: spécifie la direction de la projection. Ignoré si {{PropertyData/fr|Base}} est un [Arch Plan de section](Arch_SectionPlane/fr.md).

-    {{PropertyData/fr|Projection Mode|Enumeration}}: spécifie le mode de projection. Les modes suivants sont disponibles :

    -   
        {{Value|Solid}}
        
        : projette l\'objet sélectionné dans son intégralité.

    -   
        {{Value|Faces individuelles}}
        
        : projette uniquement les faces de la liste {{PropertyData/fr|Face Numbers}}.

    -   
        {{Value|Cutlines}}
        
        : ne fonctionne que si l\'objet sélectionné est un [Arch Plan de section](Arch_SectionPlane/fr.md), ne projette que les arêtes coupées par le plan de coupe.

    -   
        {{Value|Cutfaces}}
        
        : ne fonctionne que si l\'objet sélectionné est un [Arch Plan de section](Arch_SectionPlane/fr.md), projette les zones coupées dans les solides par le plan de coupe comme des faces.

    -   
        {{Value|Faces solides}}
        
        : projette l\'objet sélectionné dans son intégralité en découpant les faces une par une. Peut être utilisé si le mode {{Value|Solid}} donne de mauvais résultats. {{Version/fr|0.20}}

-    {{PropertyData/fr|Segment Length|Float}}: spécifie la taille en millimètres des segments linéaires si {{PropertyData/fr|Tessellation}} est `True`.

-    {{PropertyData/fr|Tessellation|Bool}}: spécifie si la tessellation doit être effectuée. La tessellation signifie que les courbes sont remplacées par des séquences de segments de lignes. Cette opération peut être coûteuse en calcul si la {{PropertyData/fr|Segment Length}} est trop courte.

-    {{PropertyData/fr|Visible Only|Bool}}: spécifie si la projection doit être recalculée uniquement si elle est visible.

-    {{PropertyData/fr|Exclusion Points|Vector list}}: Une liste de points d\'exclusion. Toute arête passant par l\'un de ces points ne sera pas dessinée. {{Version/fr|0.20}}

### Vue


{{TitleProperty/fr|Draft}}

-    {{PropertyView/fr|Pattern|Enumeration}}: non utilisé.

-    {{PropertyView/fr|Pattern Size|Float}}: non utilisé.

## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer une projection 2D, utilisez la méthode `make_shape2dview` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode obsolète `makeShape2DView`.


```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```

-    `baseobj`est l\'objet à projeter.

-    `projectionVector`est le vecteur de projection. S\'il n\'est pas fourni, l\'axe Z est utilisé.

-    `facenumbers`est une liste de numéros de face (basé sur 0). Si elles sont fournies, seules ces faces sont prises en compte.

-    `shape2dview`est renvoyé avec la projection 2D créée.

Modifiez la propriété `ProjectionMode` de l\'objet créé si nécessaire. Cela peut être : `"Solid"`, `"Individual Faces"`, `"Cutlines"`, `"Cutfaces"` ou `"Faces pleines"`.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 500
box.Height = 1000

shape1 = Draft.make_shape2dview(box)

shape2 = Draft.make_shape2dview(box, App.Vector(1, -1, 1))

shape3 = Draft.make_shape2dview(box, App.Vector(-1, 1, 1), [0, 5])
shape3.ProjectionMode = "Individual Faces"

doc.recompute()
```





 