#include <stdio.h>

int base;
int exponente;

int Potencia(int a, int b){
	if (b==1){
		return a;
	}
	else{
		return a * Potencia(a,b-1);
	}
}

int main(void){
	printf("Ingrese la base: ");
	scanf("%d",&base);
	printf("Ingrese la exponente: ");
	scanf("%d",&exponente);
	
	printf("El resultado de la potencia es: %d",Potencia(base,exponente));

	return 0;
}