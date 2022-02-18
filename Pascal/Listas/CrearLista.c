#include <stdio.h>
#include <stdlib.h>

typedef struct regnodo{
	int dato;
	struct regnodo *prox;
}Nodo;

Nodo *cargar(Nodo *prim){
	Nodo *p = NULL;
	Nodo *ult = NULL;
	int num;

	while (num != -1){
		printf("Ingrese el valor a cargar (-1 para salir): \n");
		scanf("%d",&num);
		
		if (num == -1){
			break;
		}

	    p = (Nodo *) malloc(sizeof(Nodo));
	    
	    p->dato = num;
	    p->prox = NULL;
	    
	    if (prim == NULL){
	    	prim=p;
	    	ult=p;
	    }
	    else{
	    	ult->prox = p;
	    	ult=p;
	    }
	}
    return prim;

}

Nodo *imprimir(Nodo *prim){
	Nodo *p = NULL;
	p=prim;

	while (p != NULL){
		printf("Valor: %d\n", p->dato);
		p=p->prox;
	}
}

Nodo *borrar(Nodo *prim){
	Nodo *p = NULL;
	p=prim;
	while (prim != NULL){
		prim=p->prox;
		free(p);
		p->prox=prim;
	}
}


int main(void){
	Nodo *prim = NULL;
	
	cargar(prim);
	imprimir(prim);
	borrar(prim);

	return 0;
}