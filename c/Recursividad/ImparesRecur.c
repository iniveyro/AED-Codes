#include <stdio.h>

int entrada;

int Impares(int n){
	if (n<10){
        if (n%2 == 0){
            return 0;
        }
        else{
            return n;
        }
    }
    else{
        return Impares(n%10) + Impares (n/10);
    }
}

int main(void){

	printf("Ingrese un numero: ");
	scanf("%d",&entrada);
	
	printf("El resultado de la suma de digitos impares es: %d",Impares(entrada));

	return 0;
}