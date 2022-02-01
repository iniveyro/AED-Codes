  La Universidad Tecnológica Nacional contiene información de los alumnos almacenada en una secuencia

  de caracteres. Estos datos son código de carrera, nombre y apellido del alumno, año que cursa

  actualmente, de la siguiente forma:


1GuillermoFernandez|4#3MicaelaLopez|1#3CarlosGomez|5#.....*


 Además se cuenta con un arreglo de 10 posiciones cuyo contenido es el nombre de cada carrera (alfanumérico de 40). 
Se pide:


a | Generar como salida una lista con los alumnos (guardar como máximo 40 caracteres) y la carrera 
    
    a cual pertenece, ordenada por nombre de carrera.

b | Emitir un listado de los alumnos que se encuentran en quinto año.


c | Al finalizar mostrar por pantalla la cantidad de alumnos por carrera.


|Accion Secuencia+Lista () Es
|Ambiente
|
|Sec: Secuencia de Caracter;
|v: Caracter;
|
|NumeroCAracteres: ('1'..'5');
|NombreCarrera = Registro
|
|	NombreCarrera: AN(40);
|
|Fin Registro 
|
|
|NombreDeLaCarrera: Arreglo [1..10] de NombreCarrera; ## Nombres de las Carreras
|TotalxCarrera: Arreglo [1..10] De Entero; ## Aqui se almacenan los totales de alumnos por carrera
|
|Salida = Registro
|
|	NombreyApellido: Arreglo [1..40] de Caracter; ## Nombre de los alumnos seran alamacenados
|	Carrera: Arreglo [1..40] de Caracter; ## Carrera de los alumnos seran almacenados
|	prox: Puntero a Salida;
|	ant: Puntero a Salida;
|
|Fin Registro
|
|Prim,Ult,p,q: Puntero a Salida;
|TipoCarrera,i:Entero;
|ResgCarrera: AN(1);
|
|
|
|
||Procedimiento CopiarCarrera ( q: Puntero a Salida, NombreDeLaCarrera: Arreglo [1..10] de NombreCarrera,x: Entero,v: Caracter ) Es
||	Ambiente
||
||	
||
||	Algoritmo
||
||	## i es una variable global, por lo tanto puedo usarlo dentro de cualquier funcion o Procedimiento
||
||	|Para ( i:= 0 Hasta 40 ) Hacer
||	|
||	|	*q.Carrera[i]:= NombreDeLaCarrera[x].NombreCarrera[i];
||	|	Avz(Sec,v);
||	|
||	|Fin Para
||
||
||Fin Procedimiento
|
|
|Algoritmo
|
|Arr (Sec);
|Avz (Sec,v);
|
|Prim:= Null;
|Ult:= Null;
|
|Sec: Secuencia de Caracter; [CodigoCarrera N(1)][NombreyApellido]|[AñoCursaActualmente]#[CodigoCarrera N(1)][NombreyApellido]|[AñoCursaActualmente]#*
|
|	|Mientras (NoFDS( Sec )) Hacer
|	|
|	|	|Segun (v) Hacer ## Segun la carrera que cursan
|	|	|
|	|	|	='0': TotalxCarrera[0]:= TotalxCarrera[0] + 1;ResgCarrera:= v;
|	|	|	='1': TotalxCarrera[1]:= TotalxCarrera[1] + 1;ResgCarrera:= v;
|	|	|	='2': TotalxCarrera[2]:= TotalxCarrera[2] + 1;ResgCarrera:= v;
|	|	|	='3': TotalxCarrera[3]:= TotalxCarrera[3] + 1;ResgCarrera:= v;
|	|	|	='4': TotalxCarrera[4]:= TotalxCarrera[4] + 1;ResgCarrera:= v;
|	|	|	='5': TotalxCarrera[5]:= TotalxCarrera[5] + 1;ResgCarrera:= v;
|	|	|	='6': TotalxCarrera[6]:= TotalxCarrera[6] + 1;ResgCarrera:= v;
|	|	|	='7': TotalxCarrera[7]:= TotalxCarrera[7] + 1;ResgCarrera:= v;
|	|	|	='8': TotalxCarrera[8]:= TotalxCarrera[8] + 1;ResgCarrera:= v;
|	|	|	='9': TotalxCarrera[9]:= TotalxCarrera[9] + 1;ResgCarrera:= v;
|	|	|
|	|	|Fin segun
|	|	
|	|	Avz ( Sec , v );
|	|## [CodigoCarrera N(1)][NombreyApellido]|[AñoCursaActualmente]#[CodigoCarrera N(1)][NombreyApellido]|[AñoCursaActualmente]#*
|	|	
|	|	
|	|	Nuevo (q);
|	|
|	|	##Copio el nombre y apellido
|	|	##Estoy posicionado en el primer caracter caracter del Nombre
|	|
|	|	i:=0;
|	|
|	|	|Mientras ( ( v < > ' | ' ) ) Hacer	
|	|	|
|	|	|	*q.NombreyApellido[i]:= v;
|	|	|	i:= i + 1;
|	|	|	Avz (Sec,v);
|	|	|
|	|	|Fin Mientras
|	|
|	|	## Copio La carrera en la Salida
|	|
|	|	|Segun ( ResgCarrera ) Hacer
|	|	|	
|	|	|	= '0': CopiarCarrera ( q,NombreDeLaCarrera, 0 ,v);
|	|	|	= '1': CopiarCarrera ( q,NombreDeLaCarrera, 1 ,v);
|	|	|	= '2': CopiarCarrera ( q,NombreDeLaCarrera, 2 ,v);
|	|	|	= '3': CopiarCarrera ( q,NombreDeLaCarrera, 3 ,v);
|	|	|	= '4': CopiarCarrera ( q,NombreDeLaCarrera, 4 ,v);
|	|	|	= '5': CopiarCarrera ( q,NombreDeLaCarrera, 5 ,v);
|	|	|	= '6': CopiarCarrera ( q,NombreDeLaCarrera, 6 ,v);
|	|	|	= '7': CopiarCarrera ( q,NombreDeLaCarrera, 7 ,v);
|	|	|	= '8': CopiarCarrera ( q,NombreDeLaCarrera, 8 ,v);
|	|	|	= '9': CopiarCarrera ( q,NombreDeLaCarrera, 9 ,v);
|	|	|
|	|	|Fin Segun
|	|		
|	|	
|	|	Avz ( Sec,v ); ## Avanzo al Caracter numerico del año
|	|
|	|
|	|	|Si ( v = '5' ) entonces
|	|	|	Esc ("Nombre Alumno |     Año   ");
|	|	|	|Para (i:= 0 Hasta 40 ) Hacer
|	|	|	|
|	|	|	|	Esc (*q.NombreyApellido[i],"    |");
|	|	|	|
|	|	|	|Fin para
|	|	|	
|	|	|	Escribir ("    5° Año");
|	|	|
|	|	|Fin Si
|	|
|	|	
|	|
|	|	|Si ( Prim = null ) entonces  ## Agregamos primer elemento a la Lista
|	|	|
| 	|	|	Prim:= q;
|	|	|	Ult:= q;
| 	|	|	*q.prox:= Null;
|	|	|	*q.ant:= Null;
|	|	|
|	|	|	Sino
| 	|	|
| 	|	|		## Agregamos el nodo a la salida, todo ordenado por Nombre Carrera 
| 	|	|
|	|	|		p:= Prim; ## Siempre debemos colocar P:= Prim, para poder Ordenar y tambien insertar nodos
|	|	|
|	|	|		|Mientras ( p < > Null ) y ( *p.Carrera < *q.Carrera ) Hacer ## Ordenamiento ascendente
|	|	|		|	
|	|	|		|	p:= *p.prox;
|	|	|		|
|	|	|		|Fin Mientras
| 	|	|	
|	|	|
|	|	|
|	|	|		|Si ( p = Prim ) entonces ## Actalizamos Prim
| 	|	|		|
|	|	|		|	*q.prox:= p;
| 	|	|		|	*p.ant:= q;
|	|	|		|	Prim:= q;
|	|	|		|
|	|	|		|	Sino 
|	|	|		|
|	|	|		|		|Si ( p = Null ) entonces  ## Actualizamos Ult
|	|	|		|		|
|	|	|		|		|		*q.ant:= Ult;
|	|	|		|		|		*q.prox:= Null;
|	|	|		|		|		*Ult.prox:= q;
|	|	|		|		|		Ult:= q;	
| 	|	|		|		|		Sino 
|	|	|		|		|
|	|	|		|		|			## Elementos Intermedios 
| 	|	|		|		|
|	|	|		|		|		*q.prox:= p;
| 	|	|		|		|		*p.ant:= q;
|	|	|		|		|		*q.ant:= *p.ant;
|	|	|		|		|		*(*p.ant).prox:= q;
|	|	|		|		|			
|	|	|		|		|
|	|	|		|		|Fin Si
|	|	|		|
|	|	|		|Fin Si
|	|	|
|	|	|Fin Si
|	|
|	|
|	|	Avz ( Sec,v );
|	|
|	|Fin Mientras
|
|	Escribir ( "Cantidad de alumnos por Carrera" );
|	Escribir ( "-------------------------------");
|
|	|Para ( i:= 0 Hasta 40 ) Hacer
|	|
|	|	Para ( j:= 0 Hasta 40 ) Hacer
|	|
|	|		Esc (NombreDeLaCarrera[i].NombreCarrera[j];);
|	|
|	|	Fin Para
|	|
|	|	Esc ( TotalxCarrera[i] );
|	|
|	|Fin Para
|
|Cerrar ( Sec );
|Fin Accion























