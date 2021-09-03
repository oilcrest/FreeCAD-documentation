---
- GuiCommand:/fr
   Name:SheetMetal Unfold
   Name/fr:SheetMetal Déplier
   MenuLocation:SheetMetal → Unfold
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**U**
---


</div>

## Description

La commande <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **SheetMetal Unfold** permet de déplier un objet en tôle.

## Utilisation

Pour déplier une pièce de tôlerie:

1.  Basculez vers <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [atelier SheetMetal](SheetMetal_Workbench/fr.md).
2.  Sélectionnez une face plane de la pièce de tôlerie. **Remarque**: la face doit être un plan, l\'épaisseur doit être constante .
3.  Cliquez sur l\'outil <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **Unfold** pour afficher un menu dans le panneau des tâches pour gérer les options de dépliage.
4.  Sélectionnez les options de projection de la future esquisse aplatie
5.  Sélectionnez la règle de déduction des plis avec [Kfactor](https://github.com/shaise/FreeCAD_SheetMetal#terminology):
    -   Utilisez [Material Definition Sheet](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet)
    -   Ou sélectionnez un manuel [Kfactor](https://github.com/shaise/FreeCAD_SheetMetal#terminology) puis la norme ANSI ou DIN à appliquer.

## Propriétés

See also: [Property editor](Property_editor.md).

This tool creates an Unfold object and has no representation of its own in the [Tree view](Tree_view.md) or elsewhere and so has no properties.

The **Unfold** object, on the other hand, is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It has no additional properties, but its label has a default value:

### Données


{{Properties_Title|Base}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/fr|Label}}: Nom d\'utilisateur de l\'objet dans la [Vue en arborescence](Tree_view/fr.md).

-    {{PropertyData/fr|Label2}}: Description utilisateur de l\'objet dans la [Vue en arborescence](Tree_view/fr.md).


</div>

## Limites

-   La tôle doit avoir une épaisseur constante , y compris dans les rayons
-   Les faces plates doivent être planes sans lignes de division.
-   Les angles de pliage doivent être des rayons avec des faces cylindriques.
-   La fonction de dépliage n\'est pas paramétrique pour le moment.


<div class="mw-translate-fuzzy">





</div>

[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)