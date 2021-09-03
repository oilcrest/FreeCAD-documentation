---
- GuiCommand:/fr
   Name:Draft Mirror
   Name/fr:Draft Miroir
   MenuLocation:Modification → Miroir
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**M** **I**
   SeeAlso:[Draft Clone](Draft_Clone/fr.md)
---

## Description

La commande <img alt="" src=images/Draft_Mirror.svg  style="width:24px;"> **Draft Miroir** crée des copies miroir, des objets [Part Miroir](Part_Mirror/fr.md), à partir des objets sélectionnés. Un objet [Part Miroir](Part_Mirror/fr.md) est paramétrique et il sera mis à jour si son objet source change.

Cette commande peut être utilisée sur des objets 2D créés avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi sur de nombreux objets 3D tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md), l\'[atelier PartDesign](PartDesign_Workbench/fr.md) ou l\'[atelier Arch](Arch_Workbench/fr.md).

<img alt="" src=images/Draft_Mirror_example.jpg  style="width:400px;"> 
*Mise en miroir d'un objet*

## Utilisation

Voir aussi : [Draft Accrochage](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  En option, sélectionnez un ou plusieurs objets.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Mirror.svg" width=16px> [Créer une symétrie des objets...](Draft_Mirror/fr.md)**.
    -   Sélectionnez l\'option **Modification → <img src="images/Draft_Mirror.svg" width=16px> Miroir** dans le menu.
    -   Utilisez le raccourci clavier : **M** puis **I**.
3.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez un objet dans la [Vue 3D](3D_view/fr.md).
4.  Le panneau de tâches **Mirror** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
5.  Choisissez le premier point du plan miroir dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
6.  Choisissez le deuxième point du plan miroir dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
7.  Le plan miroir est défini par les points sélectionnés et la normale du [DraftPlan de travail](Draft_SelectPlane/fr.md).

## Options

Les raccourcis clavier à caractère unique mentionnés ici peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md).

-   Pour saisir manuellement des coordonnées, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune, ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **R** ou cliquez sur la case **Relative** pour activer le mode relatif. Si le mode relatif est activé, les coordonnées du deuxième point sont relatives au premier point, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   La case à cocher **Continue** n\'a aucune utilité pour cette commande.
-   La case à cocher **Modifier les sous-éléments** n\'a pas d\'utilité pour cette commande.
-   Appuyez sur **S** pour activer ou désactiver [Draft Accrochage](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour abandonner la commande.

## Remarques

-   Les copies miroir des [Draft Lignes](Draft_Line/fr.md), [Draft Polylignes](Draft_Wire/fr.md), [Draft Arcs](Draft_Arc/fr.md) et [Draft Cercles](Draft_Circle/fr.md) peuvent être transformées en objets Draft éditables indépendants en utilisant [Draft Rétrograder](Draft_Downgrade/fr.md) et ensuite [Draft Mettre à niveau](Draft_Upgrade/fr.md).
-   La commande [Part Copie simple](Part_SimpleCopy/fr.md) peut être utilisée pour créer une copie d\'un objet miroir qui n\'est pas lié à son objet source.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées : **Edition → Préférences... → Général → Unités → Systèmes d'unités → Nombre de décimales**.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet [Part Miroir](Part_Mirror/fr.md) est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Source|Link}}: spécifie l\'objet qui est mis en miroir.


{{TitleProperty|Plane}}

-    {{PropertyData/fr|Base|Vector}}: indique le point de base du plan miroir.

-    {{PropertyData/fr|Normal|Vector}}: spécifie la direction normale du plan miroir.

## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour mettre en miroir des objets, utilisez la méthode `mirror` du module Draft.


```python
mirrored_list = mirror(objlist, p1, p2)
```

-    `objlist`contient les objets à mettre en miroir. Il s\'agit soit d\'un objet unique, soit d\'une liste d\'objets.

-    `p1`est le premier point du plan miroir.

-    `p2`est le second point du plan miroir.

-   Si le [Draft Plan de travail](Draft_SelectPlane/fr.md) est disponible, l\'alignement du plan miroir est déterminé par sa normale, sinon la direction de la caméra dans la [3D view](3D_view.md) active est utilisée. Si l\'interface graphique n\'est pas disponible, l\'axe Z est utilisé.

-    `mirrored_list`est retourné avec les nouveaux objets `Part::Mirroring`. Il s\'agit soit d\'un objet unique, soit d\'une liste d\'objets, en fonction de `objlist`.

Exemple:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(FreeCAD.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

p1 = App.Vector(2000, -1000, 0)
p2 = App.Vector(2000, 1000, 0)

line1 = Draft.make_line(p1, p2)
mirrored1 = Draft.mirror(polygon1, p1, p2)

Line2 = Draft.make_line(-p1, -p2)
mirrored2 = Draft.mirror([polygon1, polygon2], -p1, -p2)

doc.recompute()
```





 