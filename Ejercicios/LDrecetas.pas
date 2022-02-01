
###LISTAS DOBLEMENTE ENLAZADAS###

ACCION EJER ES 
	AMBIENTE
		nodo=registro
			dato:entero 
			prox:puntero a nodo
			ant:puntero a nodo
		fin registro
		prim,ult,p,q:puntero a nodo
		valor:entero 

	PROCESO ## INSERCION 
		p:=prim 
		ult:=nil
		Ingresar(valor)
		Nuevo(q)
		q*.dato:=valor
		Si (prim=nil) Entonces 
			prim:=q 
			ult:=q
			q*.prox:=nil
			q*.ant:=nil
		Sino
			Mientras (p<> nil) ^ (q*.dato > p*.dato) hacer
				p:=p*.prox
			fin Mientras
			Si (p = prim) Entonces//insercion del 1er elto
				q*.prox:=p 	
				prim:=q
				p*.ant:=q
				q*.ant:=nil
			Sino
				Si(p =nil) Entonces//insercion desp del ult elemento
					p*.ant.prox:=q
					ult:=q
					*q.prox:=p
					*q.ant:=p*.ant 
				Sino 
					p*.ant.prox:=q 
					q*.prox:=p 
					p*.ant:=q 
					q*.ant:=p*.ant 
				fin si 
			fin Si
		fin Si
	
	PROCESO ## ELIMINACION 
		Ingresar(valor)
		p:=prim 
		ult:=nil 
		Si (prim = nil) Entonces
			Esc(lista vacia)
		Sino 
			Mientras (p*.dato <> valor) ^ (p <> nil) hacer
				p:=p.prox
			fin Mientras
			Si (prim = ult) Entonces//unico elemento
				prim:=nil 
				ult:=nil
			Sino	
				Si (p = prim ) Entonces//1er elemento
					prim:=p*.prox
					p*.prox.ant:=nil
				Sino	
					Si(p =ult) Entonces// ultimo elemento
						p*.ant.prox:=nil 
						ult:=p*.ant 
					Sino 
						p*.ant.prox:=p*.prox//elemento del medio 
						p*.prox.ant:=p*.ant 
					fin Si
				fin Si
			fin Si
			Disponer(p)
		fin Si
			
	PROCESO ## BÚSQUEDA
		Ingresar(valor)
		Si (prim = nil) Entonces
			Esc(error,lista vacia)
		Sino
			p:= prim
			Mientras (p*.dato <> valor)	^( p*.prox <> nil )
				p:=p*.prox
			fin Mientras
			Si (p*.dato <> valor) Entonces
				Esc("elemento no encontrado")
			Sino 
				Esc("elemento hallado", p*.dato)
			fin Si
		fin Si					


						




