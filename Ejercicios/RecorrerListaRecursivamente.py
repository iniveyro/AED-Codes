Accion RecorrerLista (Prim,ult:Puntero a nodo) Es
Ambiente

nodo = Registro
	
	Dato: Entero;
	Prox:= Puntero a nodo; o Prox:= nodo;
	ant:= Puntero a nodo; o Prox:= nodo;

Fin Registro

p:= Puntero a nodo;




|Procedimiento RecorrerListaDelante(p: Puntero a nodo);
|Ambiente 
|
|
|
|Algoritmo
|
|
|	|si ( p < > Null ) Entonces 
|	|
|	|	Esc( "Contenido del Nodo:  ",*p.dato );
|	|	RecorrerListaRecursivamente ( *p.prox ); // recorrer hacia delante
|	|
|	|Fin si
|
|Fin Procedimiento



|Procedimiento RecorrerListaAtras (q: Puntero a nodo);
|Ambiente 
|
|
|
|Algoritmo
|
|
|	|si ( q < > Null ) Entonces 
|	|	Esc( "Contenido del Nodo:  ",*q.dato );
|	|	RecorrerListaAtras ( *q.ant ); // recorrer hacia delante
|	|
|	|Fin si
|
|Fin Procedimiento







|Algoritmo
|
|
|p:= Prim;
|q:= ult;
|
|RecorrerLista(p);
|RecorrerLista(q);
|
|
|Fin Accion







