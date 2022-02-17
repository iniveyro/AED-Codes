#include <stdio.h>

int max;
int arr[9]={11,32,43,24,15,6,37,19,11};
int resultado=0;
int i;

int FMax(int arr[],int i, int max){
	if (i==9){
		return max;
	}
	else{
		if (max < arr[i]){
			max=arr[i];
			return FMax(arr,i+1,max);
		}
		else{
			return FMax(arr,i+1,max);
		}
	}
}

int main(void){

	i=0;
	resultado=FMax(arr,i,max);
	printf("El numero maximo encontrado en el arreglo es: %d",&resultado);

	return 0;
}