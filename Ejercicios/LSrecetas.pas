
###LISTAS SIMPLEMENTE ENLAZADAS###
ACCION EJER ES
AMBIENTE
	nodo=registro
		dato:entero
		prox:puntero a nodo
	fin registro
	p,a,prim,q:puntero a nodo	
	valor:entero

PROCESO #BUSQUEDA
	Esc("ingrese valor")
	Leer(valor)
	p:=prim
	Si (prim =nil) Entonces
		Esc("lista vacia")
	Sino
		Mientras (p <> nil) ^ (p*.dato <> valor) hacer
			p:=p*.prox 
		fin Mientras
		Si (p*.dato = valor) Entonces // p<> nil 
			Esc("elemento encontrado")
		Sino
			Esc("elementono no encontrado")
		fin Si
	fin Si

PROCESO #INSERCION
	p:=prim
	Esc("ingrese valor")
	Leer(valor)
	Nuevo(q)
	q*.dato:=valor
	Si (prim = nil) Entonces
		prim:=q
		q*.prox:=nil
	Sino
		Mientras (p*.prox <> nil) ^ (p*.dato < valor) hacer//recorre
			a:=p
			p:=p*.prox
		fin Mientras
		Si (p= prim) Entonces//insercion antes del primer elemento
			q*.prox:=prim
			prim:=q
		Sino//en el medio o ultimo
			q*.prox:=p //o q*.prox:=nil si se inserta desp del ultimo nodo
			a*.prox:=q	
		fin Si
	fin Si
	
PROCESO #ELIMINACION
	p:=prim
	Esc("ingrese valor")
	Leer(valor)
	Si (prim = nil) Entonces
		Esc("lista vacia")
	Sino	
		Mientras (p*.prox o p<>nil) ^ (valor <> p*.dato) hacer//busco elto a eliminar
			a:=p 
			p:=p*.prox 
		fin Mientras
		Si(valor = p*.dato)	Entonces
			Si (p=prim) Entonces//unico nodo o el primer elto de la lista
				prim:=p*.prox(1er nodo) o prim:=nil(unico nodo)
				Disponer(p)
			Sino//si es el del medio o el ultimo
				a*.prox:=p*.prox	
				Disponer(p)
			fin Si
		Sino
			Esc("no se encontró el elto")
		fin Si
	fin Si

##CARGA APILADA>>se recupera de forma inversa, se accede al ultimo elemento cargado
PROCESO
	ingresar(valor)
	prim:=nil
	Mientras (valor <> tope) hacer
		Nuevo(p)
		p*.dato:=valor
		p*.prox:=prim 
		prim:=p 
		ingresar(valor)
	fin Mientras


##CARGA ENCOLADA>>se accede al 1er elemento cargado. se mantiene el orden de la carga
PROCESO
	prim:=nil 
	ingresar(valor)
	Mientras (valor <> tope) hacer
		Nuevo(p)
		p*.dato:=valor
		p*.prox:=nil 
		Si (prim = nil) Entonces		
			prim:=p 
		Sino
			a*.prox:=p 
		fin Si
		ingresar(valor)
	fin Mientras
	
				