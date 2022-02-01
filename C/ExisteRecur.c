#include <stdio.h>
#include <stdbool.h>

int numero;
int arr[10]={19, 10, 8, 17, 9, 1, 3, 4, 6, 20};
int i;

int ExisteNum(int arr[],int i, int numero){
	if (arr[i]==numero){
		return true;
	}
	else{
		if (i<11){
			return ExisteNum(arr,i+1,numero);
		}
		else{
			return false;
		}
	}
}

int main(void){
	numero=0;
	i=0;
	printf("Ingrese el numero que desea saber su existencia: ");
	scanf("%d",&numero);
	
	if (ExisteNum(arr,i,numero)==true){
		printf("El numero %d EXISTE",&numero);
	}
	else{
		printf("El numero %d NO EXISTE",&numero);
	}
	return 0;
}