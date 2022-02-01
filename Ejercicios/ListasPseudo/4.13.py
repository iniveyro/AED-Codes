Accion Entradas_Repetidas  (Prim: Puntero a Entradas) Es

Ambiente


Entradas = Registro
	
	Num: Entero;
	prox: Puntero a Entradas;
	ant: Puntero a Entradas;

Fin registro


x,prim,p,ult: puntero a Entradas;


band: booleano;


Procedimiento Validar_Orden() Es


Algoritmo

	band:=True;
	x:=prim;
	p:=*x.prox;

	Mientras ( p <> nill ) y ( band ) Hacer

		Si ( *p.Num < *x.Num) Entonces

			band:=False;

			Sino 

				x:=p;

		Fin si

		p:=*p.prox;
		
	Fin mientras

Fin procedimiento



procedimiento Recorrer() Es
	#No existe el (P=prim) Dado que P siempre se movera al segundo lugar
	#No existe el (Prim=ult), dado que como p siempre se mueve al segundo lugar, en el caso que sea 
	#un unico elemento es decir prim=ult, entonces P automaticamente aputara a nil, y no entrara al mientras
	Si (p=ult) Entonces

		ult:=x;
		*ult.prox:=nil;

		Sino
			#Eliminacion Intermedia

			*x.prox:=*p.prox;
			*(*p.prox).ant:=x;

	Fin si
	Disponer(p);

Fin procedimiento







Algoritmo


Validar_Orden();

Si (Band) Entonces #Esta todo ordenado

	x:=prim;
	p:=*x.prox;
	Mientras(p<>nill) Hacer


		Mientras (*x.Num = *p.Num) y (p <> nil) Hacer
						
			Recorrer();
			p:=*x.prox;


		Fin mientras			


		x:=p;
		p:=*p.prox;
	Fin Mientras


Sino 

Esc ("La Lista se encuentra Desordenada ERROR");

Fin si



Fin Accion









































Fin Accion
