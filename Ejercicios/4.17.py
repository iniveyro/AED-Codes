Accion Secuencias+Lista Es
Ambiente

Sal,Sec1,Sec2: Secuencia de caracter;
v1,v2: caracter;



#Sal = Sec1 [Las palabras que empizan y terminan con la misma letra]
#Sal = Sec2 [las palabras que tengan al menos un digito numero y los digitos esten en posicion par]

#Usar una Lista Como auxiliar
auxiliar= registro
	Letra: An(1);
	prox: Puntero a auxiliar;
	ult: Puntero a auxilia;
Fin registro

ult,prim,p,q:Puntero a auxiliar;


Procedimiento EliminarNodos( prim:Puntero a auxiliar) ES
	
	p:=prim;
	Mientras (p <> nil ) Hacer

			prim:=*p.prox;
			
			Si (p=ult) Entonces 
				ult:=nil;
			Fin si
			
			disponer (p);
			p:=prim;

	Fin mientras 


Fin Procedimiento  














Procedimiento Secuencia1 (prim:Puntero a auxiliar) ES
Ambiente
#Solo copio en la Lista la palabra y verifico si tienen mismo inicio y final





Algoritmo
	prim:=nil;
	ult:= nil;
	Mientras (v1 = ' ') hacer
		avz (sec1,v1);
	Fin mientras
	Mientras (v1<> ' ') y (NOFDS(sec1)) Hacer
		Nuevo (q);
		*q.dato:=v1;
		*q.prox:=nil;

		#Carga de nodos
		Si (prim = nil) Entonces
			*q.prox:=nil;
			*q.ant:=nil;
			prim:=q;
			ult:=q;
			Sino

				*ult.prox:=q;
				*q.ant:=ult;
				ult:=q;

		Fin si
		avz (sec1,v1);

	Fin mientras
	

	#Si la primer letra es igual a ultima letra d ela palabra
	Si (*prim.Letra = *ult.Letra) Entonces
		p:=prim;
		#Mientras recorre la Lista, va eliminandola
		Mientras (p <> ult) Hacer

			esc (Sal,*prim.Letra);
			prim:=*p.prox;
			disponer (p);
			p:=prim;

		Fin mientras
		Esc (Sal,*prim.Letra);
		prim:=nil;
		ult:=nil;

		Sino
			#En el caso que no sean igual, elimino los nodos [Linea 22]
			EliminarNodos();

	Fin si

Fin Procedimiento
















Procedimiento Secuencia2() Es
Ambiente
Band:booleano;
Num = ('1','2','3','4','5','6','7','8','9','0');
Pos:entero;

Algoritmo
	Band:=False;
	Pos:=0;
	prim:=nil;
	ult:= nil;

	Mientras (v2 = ' ') hacer
		avz (sec1,v1);
	Fin mientras

	Mientras (v2<> ' ') y (NOFDS(sec2)) Hacer
		Nuevo (q);
		*q.dato:=v2;
		*q.prox:=nil;

		#Carga de nodos
		Si (prim = nil) Entonces
			*q.prox:=nil;
			*q.ant:=nil;
			prim:=q;
			ult:=q;
			Sino

				*ult.prox:=q;
				*q.ant:=ult;
				ult:=q;

		Fin si
		Pos:=Pos+1;
		Si (v2 en Num) y ((2 mod Pos)=0) Entonces

			Band:=True;

		Fin si
		avz (sec2,v2);
	Fin mintras


	#Si la palabra contiene al menos un digito numerico y esta posicion par entonces
	Si (band) Entonces
		p:=prim;
		#Mientras recorre la Lista, va eliminandola
		Mientras (p <> ult) Hacer

			esc (Sal,*prim.Letra);
			prim:=*p.prox;
			disponer (p);
			p:=prim;

		Fin mientras
		Esc (Sal,*prim.Letra);
		prim:=nil;
		ult:=nil;

		Sino
			#en el caso que no cumpla la condicion, elimino los nodos [Linea 22]
			EliminarNodos();

	Fin si



Fin Procedimiento












Algoritmo
Arr (Sec1); Avz (Sec1,v1);
Arr (Sec2); Avz (Sec1,v2);
Crear (Sal);

Mientras (NOFDS(Sec1) y NOFDS(Sec2)) Hacer
	

	Secuencia1();
	Secuencia2();
	




Fin mientras
Secuencia1();
Secuencia2();




Cerrar (Sec1); 
Cerrar (Sec2);
Cerrar (Sal);
Fin accion