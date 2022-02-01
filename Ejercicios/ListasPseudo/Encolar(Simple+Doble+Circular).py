Accion Encolar.py
Ambiente

TiposLista = (1,2,3,4);







SimpleEnlazada = Registro

	Dato: Entero;
	Prox: Puntero a SimpleEnlazada;

Fin registro

PrimS,pS,antS:Puntero a SimpleEnlazada;














DobleEnlazadaSimple = Registro
	
	Dato:Entero;
	prox: Puntero a DobleEnlazadaSimple;
	ant: Puntero a DobleEnlazadaSimple;

Fin registro

PrimD,qD,ult: Puntero a DobleEnlazadaSimple;














CircularEnlazadaSimple = Registro
	
	Dato:Entero;
	prox: Puntero a CircularEnlazadaSimple;

Fin registro

PrimC,qC,pC: Puntero a CircularEnlazadaSimple;













CircularEnlazadaDoble = Registro

	Dato:Entero;
	prox: Puntero a CircularEnlazadaDoble;
	ant: Puntero a CircularEnlazadaDoble;
Fin registro

PrimCD,pCD,qCD: Puntero a CircularEnlazadaDoble;

Band:Booleano;















Procedimiento Validacion(val:entero) Es

	Si (val en TiposLista) Entonces
		Band:=False;

		Sino 

			Esc ("'Fuera de Rango' -->> Debe ingresar (1 - 2 - 3 - 4)")

	Fin si

Fin Funcion


















Funcion ValidacionCaracter(Dat:AN(1)):Booleano Es 

	Mientras (Dat <> 's') y (Dat <> 'n') Hacer

		Esc ("Ingrese Solo Una ltra ['s'] o ['n']");
		Leer (Dat);

	Fin mientras

	Si (Dat='s') Entonces 

		ValidacionCaracter:=True;

		Sino

			ValidacionCaracter:=False;

	Fin si

Fin Funcion 






















Procedimiento ListaSimple() Es
Ambiente

Dato: AN(1);





Algoritmo

	primS:=nil;


	Mientras (Band) Hacer
		
		Nuevo (qS);
		Esc ("Ingrese El dato que desea encolar");
		Leer (*qS.Dato);
		
		Si (prim=nil) Entonces
			*qS.prox:=nil;
			primS:=qS;
			

			Sino

				*pS.prox:=qS;
				*qS.prox:=nil;

		Fin si

		*pS:=qS;

		Esc ("Desea Cargar Otro Dato? [Si = 's'] - [No = 'n']");
		Leer (Dato);
		Band:= ValidacionCaracter(Dato); #La funcion ValidacionCaracter, solo sirve para saber
										 # Si ingreso 's' o 'n' Devuelve un booleano

	Fin mientras


	Esc ("Fin del programa")


Fin Procedimiento


























Procedimiento ListaDobleSimple() Es
Ambiente
Dato: AN(1);



Algoritmo 
	PrimD:=nil;
	ult:=nil;
	Mientras (Band) Hacer
		
		Nuevo(qD);
		Esc ("Ingrese Los datos: ");
		Leer (*qD.Dato);

		Si ( PrimD = nil ) Entonces

			#Inserto el primer nodo
			primD:=qD;
			ult:=primD;
			*prim.ant:=nil;
			*ult.prox:=nil;

			Sino

				*ult.prox:=qD;
				*qD.prox:=nil;
				*qD.ant:=ult;
				ult:=qD;

		Fin si



		Esc ("Desea Cargar mas Datos? [Si='s'] - [No='n'] ");+
		Leer (Dato);
		Band:= ValidacionCaracter(Dato);

	Fin mientras

Fin Procedimiento 































Procedimiento ListaCircularSimple() ES
Ambiente
Dato: AN(1);

Algoritmo



	PrimC:=nil;
	Mientras (Band) Hacer
		
		Nuevo(qC);
		Esc ("Ingrese Los datos: ");
		Leer (*qC.Dato);

		Si ( PrimC = nil ) Entonces

			#Inserto el primer nodo
			primC:=qC;
			*qC.prox:=qC;
			
			Sino

				*pC.prox:= qC;
				*qC.prox:= prim;
				

				

		Fin si
		pC:=qC;


		Esc ("Desea Cargar mas Datos? [Si='s'] - [No='n'] ");+
		Leer (Dato);
		Band:= ValidacionCaracter(Dato);

	Fin mientras



Fin Procedimiento


































Procedimiento ListaCircularDoble () ES 
Ambiente
Dato: AN(1);



Algoritmo



	PrimCD:=nil;

	Mientras (Band) Hacer
		
		Nuevo(qCD);
		Esc ("Ingrese Los datos: ");
		Leer (*qCD.Dato);

		Si ( PrimCD = nil ) Entonces

			#Inserto el primer nodo
			primCD:= qCD;
			*qCD.prox:= qCD;
			*qCD.ant:= qCD;
			
			
			Sino

				*ultCD.prox:= qCD;
				*qCD.ant:= ultCD;
				*qCD.prox:= primCD;
				*primCD.ant:= qCD;

		

		Fin si
		ultCD:= qCD;

		Esc ("Desea Cargar mas Datos? [Si='s'] - [No='n'] ");+
		Leer (Dato);
		Band:= ValidacionCaracter(Dato);

	Fin mientras

Fin Procedimiento 












Algoritmo


Band:=True;
Esc ("Este programa Encola de 4 formas con Listas diferentes");
x:=0;
Mientras (band) Hacer	

Esc ("Con que tipo de Lista desea Encolar: ")
Leer (x);
Validacion(x);

Fin mientras

Band:=True;
Segun (x) Hacer

	=1:
		Esc ("Encolar con una Lista Simple");ListaSimple();
	=2:
		Esc ("Encolar con una Lista Doble Simple");ListaDobleSimple();
	=3:
		Esc ("Encolar con una Lista Circular Simple");ListaCircularSimple();
	=4:
		Esc ("Encolar con una Lista Circular Doble");ListaCircularDoble();


Fin segun






Fin accion