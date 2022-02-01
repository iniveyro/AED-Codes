
###LISTA CIRCULAS SIMPLE###
	AMBIENTE
		nodo=registro
			dato:entero
			prox:=puntero a nodo	
		fin registro	
		p,q,t:puntero a nodo
		valor:entero

	PROCESO##INSERCION	

		Inserción por valor : (ascendente)
		Nuevo (q)
		LEER (q*.valor);
		Si PRIM = Nill entonces
			PRIM := q;
			*q.prox := q;
		sino
			Mientras (q*.valor > p*.valor) ^ (p*.prox <>PRIM) Hacer
				ant := p;
				p := p*.prox;
			FinMientras
			Si p = PRIM entonces
				k := PRIM;
				Mientras (k*.prox <> PRIM) hacer
					k := k*.prox;
				FinMientras
				k*.prox := q;
				q*.prox := PRIM
				PRIM := q;
			sino
				Si p*.prox = PRIM entonces
					q*.prox := PRIM;
					p*.prox := q;
				sino
					ant*.prox := q;
					q*.prox := p;
				FinSi
			FinSi
		FinSi
		Para cambiar el orden se inserción:
		Mientras (q*.valor < p*.valor) ^ (p*.prox <> PRIM) Hacer

	
	PROCESO ##ELIMINACION
		Si PRIM = Nill entonces
			ESC (“lista vacia”)
		sino
			LEER (valor); p := PRIM; ant := Nill;
			Mientras (valor <> *p.valor)^(p*.prox <>PRIM) Hacer
				ant := p;
				p := p*.prox;
			FinMientras
			Si p = p*.prox entonces
				PRIM := Nill
			sino
				Si p = PRIM entonces
					k := PRIM
					Mientras (k*.prox <> PRIM) hacer
						k := k*.prox;
					FinMientras
					k*.prox := p*.prox;
					PRIM := p*.prox;
				sino
					ant*.prox := p*.prox;
				FinSi
			FinSi
			Disponer (p);
		FinSi	

