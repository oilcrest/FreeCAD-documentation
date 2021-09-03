 {{VeryImportantMessage|(November 2018) This information may be incomplete and outdated. For the latest API, see the [https://www.freecadweb.org/api autogenerated API documentation].}}

TopoShape es el objeto madre del módulo de pieza. Todos los tipos de formas (contornos, caras, sólidos, etc.) del módulo de pieza son TopoShapes, y comparten los siguientes atributos y métodos. Ejemplo: 
```python
import Part
sh = Part.makeBox(10,10,10)
print sh.Faces
for f in sh.Faces:
   print f.Edges
```


<div class="mw-translate-fuzzy">


{{APIProperty/es|Area|El área total de las caras de la forma.}}


{{APIProperty/es|CompSolids|Lista las formas subsiguientes en esta forma.}}


{{APIProperty/es|Compounds|Lista los componentes en esta forma.}}


{{APIProperty/es|Edges|Lista las aristas en esta forma.}}


{{APIProperty/es|Faces|Lista las caras en esta forma.}}


{{APIProperty/es|Length|Longitud total de las aristas de la forma.}}


{{APIProperty/es|Orientation|La orientación de la forma.}}


{{APIProperty/es|ShapeType|El tipo de la forma.}}


{{APIProperty/es|Shells|Lista las subsiguientes formas en esta forma.}}


{{APIProperty/es|Solids|Lista las subsiguientes formas en esta forma.}}


{{APIProperty/es|Vertexes|Lista los vértices en esta forma.}}


{{APIProperty/es|Volume|Volumen total de los sólidos de la forma.}}


{{APIProperty/es|Wires|Lista de contornos en una forma.}}


{{APIProperty/es|BoundBox|La caja de abarque del objeto}}


{{APIProperty/es|Matrix|La transformación actual del objeto como una matriz}}


{{APIProperty/es|Placement|La transformación actual del objeto como una ubicación}}


{{APIFunction/es|getAllDerivedFrom| |Devuelve todos los descendientes de este tipo de objeto|Una lista}}


{{APIFunction/es|isDerivedFrom|string|Devuelve true si el tipo indicado es un padre|Un booleano}}


{{APIFunction/es|approximate| |Aproxima un curva BSpline a partir de su contorno|Un objeto BSplineCurve}}


{{APIFunction/es|makeHomogenousWires|wire|Crea este y el contorno dado homogéneos para tener el mismo número de aristas|Un contorno}}


{{APIFunction/es|makeOffset|float|Equidista la forma una cantidad dada|Un TopoShape}}


{{APIProperty/es|CenterOfMass|El centro de masa del sistema actual. Si el campo gravitacional es uniforme, es el centro de gravedad. Las coordenadas devueltas para el centro de masas están expresadas en el sistema de coordenadas cartesiano absoluto.}}


{{APIFunction/es|check| |Comprueba la forma e informa de errores en su estructura. Es una comprobación más detallada que en isValid().| }}


{{APIFunction/es|common|TopoShape|Intersección de esta y una TopoShape dada.|Una TopoShape}}


{{APIFunction/es|complement| |Calcula el complemento de la orientación de esta forma, por ejemplo invierte el estado de los límites exteriores / interiores de esta forma.|Una TopoShape}}


{{APIFunction/es|copy| |Crea una copia de la forma|Una TopoShape}}


{{APIFunction/es|cut|TopoShape|Resta de esta y la TopoShape dada.|Una TopoShape}}


{{APIFunction/es|exportBrep|string |Exporta el contenido de esta forma a un archivo BREP. BREP es un formato nativo de CasCade.| }}


{{APIFunction/es|exportIges|string |Exporta el contenido de esta forma a un archivo IGES.| }}


{{APIFunction/es|exportStep|string |Exporta el contenido de esta forma a un archivo STEP.| }}


{{APIFunction/es|exportStl|string |Exporta el contenido de esta forma a un archivo STL.| }}


{{APIFunction/es|extrude|Vector|Extrusiona la forma a lo largo de una dirección.|Una TopoShape}}


{{APIFunction/es|fuse|TopoShape|Union de esta y una TopoShape dada.|Una TopoShape}}


{{APIFunction/es|hashCode| |Este valor es calculado a partir de la referencia y localización de la forma subyacente. La orientación no se tiene en cuenta.|Una cadena de texto}}


{{APIFunction/es|isClosed| |Comprueba si la forma está cerrada.|Un booleano}}


{{APIFunction/es|isEqual|TopoShape|Comprueba si ambas formas son iguales.|Un booleano}}


{{APIFunction/es|isNull| |Comprueba si la la forma es nula (null).|Un booleano}}


{{APIFunction/es|isSame|TopoShape|Comprueba si ambas formas comparten la misma geometría.|Un booleano}}


{{APIFunction/es|isValid| |Comprueba si la forma es válida, por ejemplo no nula, no vacía, no corrupta.|Un booleano}}


{{APIFunction/es|makeFillet| |Crea redondeo.| }}


{{APIFunction/es|makePipe|wire|Crea un tubo barriendo a lo largo de un contorno.|Una TopoShape}}


{{APIFunction/es|makePipeShell|wire|Crea un recubrimiento definido por perfiles a lo largo de un contorno.|Una TopoShape}}


{{APIFunction/es|makeShapeFromMesh|mesh|Crea una forma compuesta a partir de los datos de la malla. Nota: Esto debería utilizarse sólo para algunas pequeñas mallas.|Una TopoShape}}


{{APIFunction/es|makeThickness|list,float,float|Un sólido hueco es construido a partir del sólido inicial mediante un vaciado. El espesor del sólido se define en el momento de la construcción. Los argumentos que son pasados son una lista de caras a ignorar por la operación de vaciado, el espesor de las paredes y un valor de tolerancia.|Una TopoShape}}


{{APIFunction/es|nullify| |Destruye la referencia a la forma subyacente almacenada en esta forma. Como resultado, esta forma se convierte en vacía.}}


{{APIFunction/es|project|TopoShape|Proyecta una forma en esta forma|Una TopoShape}}


{{APIFunction/es|read|string|Lee en un archivo IGES, STEP o BREP.|Una TopoShape}}


{{APIFunction/es|reverse| |Invierte la orientación de esta forma.| }}


{{APIFunction/es|revolve|Vector, Vector, float|Revoluciona la forma alrededor de un eje unos grados dados. Ejemplo: Part.revolve(Vector(0,0,0),Vector(0,0,1),360) revoluciona la forma alrededor del eje Z 360 grados.|Una TopoShape}}


{{APIFunction/es|rotate|Vector, Vector, float|Aplica la rotación (grados) a la ubicación actual de esta forma. Ejemplo: Shp.rotate(Vector(0,0,0),Vector(0,0,1),180) rota la forma alrededor del eje Z 180 grados.|Una TopoShape}}


{{APIFunction/es|scale| |Aplica un escalado con un punto base y factor de escala a esta forma.|Una TopoShape}}


{{APIFunction/es|section|TopoShape|Sección de esta con una TopoShape dada.|Una TopoShape}}


{{APIFunction/es|sewShape| |Cose la forma si existe un hueco.| }}


{{APIFunction/es|tessellate|float|Tesela la forma y devuelve una lista de índices de vértices y caras. El valor numérico indicado es la tolerancia.|Una lista}}


{{APIFunction/es|toNurbs| |Conversión de la geometría completa de una forma en geometría NURBS. Por ejemplo, todas las curvas soportando aristas de formas básicas se convierten en curvas BSpline, y todas las superficies soportando sus caras se convierten en superficies BSpline.|Una curva NURBS}}


{{APIFunction/es|transformGeometry|matrix|Aplica transformación geométrica a una copia de la forma. La transformación a ser aplicada se define como una matriz 4x4. La geometría subyacente de las siguientes formas puede cambiar a una curva que soporte una arista de la forma, o una superficie que soporte una cara de la forma. Por ejemplo, una circunferencia puede ser transformada en una elipse cuando se aplica una transformación de afinidad. También puede ocurrir que la circunferencia entonces se represente por una curva Bspline. La transformación es aplicada a todas las curvas que soportan aristas de la forma, y todas las superficies que soportan caras de la forma. Nota: Si quieres transformar una forma sin cambiar la geometría subyacente entonces utiliza el método o rotate.| Una TopoShape}}


{{APIFunction/es|transformShape|matrix|Aplica transformación en una forma son cambiar la geometría subyacente.| }}


{{APIFunction/es|translate|Vector|Aplica la traslación a la ubicación actual de esta forma.| }}


{{APIFunction/es|writeInventor| |Escribe la malla en formato de OpenInventor en una cadena de texto.|Una cadena de texto}}


</div>

Some attributes and methods apply only to certain TopoShapes. These items apply to Edges (TopoShapeEdge).


{{APIProperty|FirstParameter|The parameter value at one end of the Edge. Not necessarily at Vertex[0]. [http://en.wikipedia.org/wiki/Parametric_equations See Parametric Equations]}}


{{APIProperty|LastParameter|The parameter value at the other end of the Edge. Not necessarily at Vertex[1].}}


{{APIFunction|getParameterByLength|Float|Maps the interval [0,Length] to the interval [FirstParameter,LastParameter]|Float }}


{{APIFunction|valueAt|Float|Returns the 3D vector corresponding to a parameter value.|Vector}}


{{APIFunction|parameterAt|Vertex,[Face]|Returns the parameter value corresponding to a Vertex (3D point).|Float}}


{{APIFunction|tangentAt|Float|Returns the direction vector of the tangent to the edge at a parameter value (if it exists).|Vector}}


{{APIFunction|normalAt|Float|Returns the direction vector of the normal to the edge at a parameter value (if it exists uniquely).|Vector}}


{{APIFunction|curvatureAt|Float|Returns the curvature of the edge at a parameter value.|Float}}


{{APIFunction|centerOfCurvatureAt|Float|Returns the center (3D point) of the osculating circle at a parameter value.|Vector}}


 

[Category:API{{\#translation:}}](Category:API.md) [Category:Poweruser Documentation{{\#translation:}}](Category:Poweruser_Documentation.md)