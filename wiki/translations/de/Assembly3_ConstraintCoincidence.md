---
- GuiCommand:/de
   Name:Assembly3 ConstraintCoincidence
   Name/de:Assembly3 DeckungsgleicheEbenen
   Icon:Assembly ConstraintCoincidence.svg
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
---

## Beschreibung

Dieses Werkzeug verbindet zwei oder mehr Objekte eines Zusammenbaus und gleicht ihre Ausrichtungen an. Die gewählten Elemente der einzelnen Objekte oder präziser ihre lokalen Koordinatensysteme (LKS) werden genutzt, um ein oder mehrere Objekte im Verhältnis zu einem anderen Objekt zu positionieren.

Davon ausgehend, dass das erste Objekt bereits mittels <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [Festsetzen](Assembly3_ConstraintLock/de.md) unbeweglich gemacht wurde, werden die weiteren Objekte auf Positionen bewegt, wo die X-Y-Ebenen aller LKS komplanar und die Z-Achsen kollinear sind.

Optional kann für diese Verbindung ein Abstand zwischen den X-Y-Ebenen gesetzt werden, sodass sie parallel zueinander liegen.

Die Winkel zwischen ihren X-Achsen (und genauso ihren Y-Achsen) sind nicht festgelegt. Im Bezug auf das erste Element, können sich die weiteren Objekte noch um die Z-Achse drehen. Dies lässt für jede einzelne Verbindung einen Freiheitsgrad unbestimmt.

Diese Verbindung kann als Scharnier in kinematischen Systemen benutzt werden.

Die Drehung kann gestoppt werden, durch das setzen der Variablen Lock Angle im Eigenschaften-Fenster (Properties Panel) auf true, und der Winkel kann auf einen bestimmten Wert gesetzt werden. Mit einem gesteuerten Wert, kann die Verbindung als Antrieb in einem kinematischen System verwendet werden.

## Anwendung

1.  Zwei oder mehr Objekte in einen Zusammenbau einfügen.
2.  Je ein planeres Flächenelement pro Objekt auswählen.
3.  Schaltfläche**<img src="images/Assembly_ConstraintCoincidence.svg" width=16px> [Deckungsgleiche Ebenen](Assembly3_ConstraintCoincidence/de.md)** drücken.





