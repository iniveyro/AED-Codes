Accion DELIVERY VAMOS-RAPIDO es

Ambiente

Delivery = Registro
	Nombre: AN (30);
	Direccion: AN (50);
	Telefono: Entero;
	Estado: AN (1);
	Total: real;
	prox: Puntero a Delivery;
	ant: Puntero a Delivery;
fin Registro

prim,p,q,ult: Puntero a Delivery;

Letra: Caracter;
Nom: AN (30);
Dir: AN (50);
Tel: Entero;
Ped: AN (1);
Total: real;

procedimiento Agregar ();
		nuevo(q);
		Esc("Ingrese Datos del primer cliente");
		Esc("Nombre: ");	Leer(*q.Nombre);
		Esc("Direccion");	Leer(*q.Direccion);
		Esc("Telefono"); 	Leer(*q.Telefono);
		Esc("Estado Del Pedido: ");	*q.Estado:="P";
		Esc("Total: ");		Leer(*q.Total);

	si (prim=nill) entonces
		Prim:=q;
		Ult:=q;
		*q.ant:=nill;
		*q.prox:=nill;
		
	Sino
		p:=prim;
		Mientras (*p.Nombre<*q.Nombre) y (p <> nill) Hacer
			p:=*p.prox;
		fin mientras

		Si (p=prim) entonces
			
			*q.prox:=p;
			*p.ant:=q;
			prim:=q;
			*q.ant:=nill;


			Sino

				Si (*p.Nombre<*q.Nombre) Entonces

					*q.ant:=*p.ant;
					*(*p.ant).prox:=q;
					*q.prox:=p;
					*p.ant:=q;


					Sino

						Si (p=nill) Entonces

							*ult.prox:=q;
							*q.ant:=ult;
							ult:=q;
							*q.prox:nill;

						Fin si
				fin si

		Fin si

	Fin si


Fin procedimiento

procedimiento Actualizar();
Ambiente

Nom: AN(30);

procedimiento

	Esc("Ingrese Nombre del cliente: "); 
	Leer (Nom);
	Mientras (Nom <> *p.Nombre) y (p<>nill) Hacer

		p:=*p.prox;

	Fin mientras

	Si (Nom = *p.Nombre) entonces

		*p.Pedido:="E";
	
		Sino 
			Esc("El cliente no Existe, Vuelva a escribir el nombre Ingrese nuevamente al Menu");

	Fin si

fin procedimiento

procedimiento Eliminar() es

Ambiente
x:AN (30);

procedimiento


	Esc ("Ingrese nombre Del  cliente Para la eliminacion: ");
	Leer (x);
	p:=prim;
	Mientras (p<>nill)  y  (*p.Nombre <> x)  Hacer 

		p:=*p.prox;

	Fin mientras

	Si (prim=nill) Entonces
		Esc ("Lista Vacia");
		Sino 
			
			Si (prim = ult) Entonces
				#Eliminacion de un unico nodo;
				prim := nill;
				ult:=nill;

				Sino 

					Si (p=prim) entonces
						#Eliminacion del primer elemento (Cuidado con el segundo);
						prim:=*p.prox;
						*prim.ant:=nill;

						Sino

							Si (p=ult) Entonces 

								ult:=*p.ant;
								*ult.prox:=nill;


								Sino

									Si (*p.Nombre = x) Entonces
										#Eliminacion del elemento intermedio;

Una ayudita: 

<-[ant[ prim ]prox]-><-[ant[ p ]prox]-><-[ant[ ]prox]-><-[ant[ ult ]prox]->

<-[ant[ prim (*p.ant)]prox ]-><-[ant[ p ]prox]-><-[ant[ (*p.prox) ]prox]-><-[ant[ ult ]prox]->

<-[ant[ prim ]prox]*(*p.ant).prox:=*p.prox->     			<-(*p.prox).ant:=*p.ant[ant[ ]prox]-><-[ant[ ult rox]->
										 <-[ant[ p ]prox]->#elimino p; Enlazar primero

<-[ant[ prim ]prox]*(*p.ant).prox:=*p.prox-><-(*p.prox).ant:=*p.ant[ant[ ]prox]-><-[ant[ ult ]prox]->

<-[ant[ prim ]prox]-><-[ant[ ]prox]-><-[ant[ ult ]prox]->


										*(*p.ant).prox:= *p.prox;
										*(*p.prox).ant:= *p.ant;

									Fin si



							Fin si

					Fin si

			Fin si


			Disponer (p);

			Esc ("cliente Eliminado satisfactoriamente")
	Fin si




Fin procedimiento






procedimiento Menu (op);


	Segun (op) Hacer
		=1: Agregar();
		=2: Actualizar();
		=3: Eliminar();
	Fin Segun


Fin procedimiento




procedimiento Validacion();

	Mientras (Letra <> 's') o (Letra <> 'n') Hacer

		Esc ("Debe ingresar Solo un caracter [s]  o  [n]");
		Leer (Letra);

	Fin mientras

Fin procedimiento


Algoritmo

prim=nill;
ult=nill;
p:=prim;
Esc ("Desea Usar el programa? Si = 's'  o  No = 'n'");
leer (Letra);
Validacion();


Mientras (Letra = 's' ) Hacer
	



	Esc("1 - Agregar Pedido");
	Esc("2 - Actualizar estado de Pedido");
	Esc("3 - Eliminar Estado");
	leer (x);



	Menu(x);

	Esc("Desea Seguir Con el programa? Si = 's'  o  No = 'n'");
	Leer (Letra);
	
	Validacion();


Fin mientras


Fin Accion