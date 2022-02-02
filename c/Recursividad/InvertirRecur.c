#include <stdio.h>

int numero;

int Inversa(int n){
	if (n<10){
		return n;
	}
	else{
		return (n % 10)*10 + Inversa(n/10);
	}
}

int main(void){
	printf("Ingrese un numero: ");
	scanf("%d",&numero);

	printf("El numero invertido es: %d",Inversa(numero));

	return 0;
}