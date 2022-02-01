/*

Como es sabido, los impactos ambientales más graves en los alimentos se producen en la fase de 
producción, pero sobre todo también en los hogares influyen en estos impactos a través de sus 
hábitos y elecciones dietéticas. Esto, en consecuencia, afecta el medio ambiente a través del 
consumo de energía relacionada con los alimentos y la generación de residuos.

Por ende, el gobierno nacional cuenta con el registro de los distintos tipos de residuos (plastico, 
metalico, organico, vidrio, textil, electrónica) de los últimos 3 años de cada provincia incluyendo
la Ciudad Autonoma de Bs As, en donde se desea realizar un proceso estadístico para saber:

*Cuanto es el promedio general de residuos.
*Cuanto es el excedente total de residuos del tipo Organico.
*Cuanto porcentaje representa los residuos Organicos con respecto a los demas.
*Cuantas toneladas de residuos organicos tiene excedente cada provincia.
*Segun el tipo de residuo, cuanto es el promedio que cada provincia genero en cada año.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>

struct RegistroFecha{
		int dd;
		int mm;
		int aa;
};

struct RegistroResiduos{
	struct RegistroFecha fecha;
 	char Provincia[25];
  	int Peso;
  	char TipoDeResiduo[1];
};

struct RegistroResiduos reg;

int NumeroMes (struct RegistroResiduos reg){
	switch (reg.fecha.aa){
		
		case 2019: return reg.fecha.mm - 1;break;
		
		case 2020: switch (reg.fecha.mm){
						case 1: return 12;break;
						case 2: return 13;break;
						case 3: return 14;break;
						case 4: return 15;break;
						case 5: return 16;break;
						case 6: return 17;break;
						case 7: return 18;break;
						case 8: return 19;break;
						case 9: return 20;break;
						case 10: return 21;break;
						case 11: return 22;break;
						case 12: return 23;break;
					}
		
		case 2021: switch (reg.fecha.mm){
						case 1: return 24;break;
						case 2: return 25;break;
						case 3: return 26;break;
						case 4: return 27;break;
						case 5: return 28;break;
						case 6: return 29;break;
						case 7: return 30;break;
						case 8: return 31;break;
						case 9: return 32;break;
						case 10: return 33;break;
						case 11: return 34;break;
						case 12: return 35;break;
					}
	}
}

int NumeroProvincia (struct RegistroResiduos reg){

	if (strcmp("Buenos Aires", reg.Provincia)==0){return 0;}
	if (strcmp("Ciudad Autonoma Bs As", reg.Provincia)==0){return 1;}
	if (strcmp("Catamarca", reg.Provincia)==0){return 2;}
	if (strcmp("Chaco", reg.Provincia)==0){return 3;}
	if (strcmp("Chubut", reg.Provincia)==0){return 4;}
	if (strcmp("Cordoba", reg.Provincia)==0){return 5;}
	if (strcmp("Corrientes", reg.Provincia)==0){return 6;}
	if (strcmp("Entre Rios", reg.Provincia)==0){return 7;}
	if (strcmp("Formosa", reg.Provincia)==0){return 8;}
	if (strcmp("Jujuy", reg.Provincia)==0){return 9;}
	if (strcmp("La Pampa", reg.Provincia)==0){return 10;}
	if (strcmp("La Rioja", reg.Provincia)==0){return 11;}
	if (strcmp("Mendoza", reg.Provincia)==0){return 12;}
	if (strcmp("Misiones", reg.Provincia)==0){return 13;}
	if (strcmp("Neuquen", reg.Provincia)==0){return 14;}
	if (strcmp("Rio Negro", reg.Provincia)==0){return 15;}
	if (strcmp("Salta", reg.Provincia)==0){return 16;}
	if (strcmp("San Juan", reg.Provincia)==0){return 17;}
	if (strcmp("San Luis", reg.Provincia)==0){return 18;}
	if (strcmp("Santa Fe", reg.Provincia)==0){return 19;}
	if (strcmp("Santiago del Estero", reg.Provincia)==0){return 21;}
	if (strcmp("Santa Cruz", reg.Provincia)==0){return 20;}
	if (strcmp("Tierra del Fuego", reg.Provincia)==0){return 22;}
	if (strcmp("Tucuman", reg.Provincia)==0){return 23;}
}	

int NumeroResiduo (struct RegistroResiduos reg){
		if (strcmp("P",reg.TipoDeResiduo)==0){return 0;}
		if (strcmp("M",reg.TipoDeResiduo)==0){return 1;}
		if (strcmp("O",reg.TipoDeResiduo)==0){return 2;}
		if (strcmp("T",reg.TipoDeResiduo)==0){return 3;}
		if (strcmp("V",reg.TipoDeResiduo)==0){return 4;}
		if (strcmp("E",reg.TipoDeResiduo)==0){return 5;}
}

const char* NombreResiduo (int x){
  switch (x){
    case 0:return"Plastico";break;
    case 1:return"Metalico";break;
    case 2:return"Organico";break;
    case 3:return"Textil";break;
    case 4:return"Vidrio";break;
    case 5:return"Electronica";break;
  }
}

int Anio(int x){
	if (x>=1 && x<=12){
		return 2019;
	}
	if (x>12 && x<=24){
		return 2020;
	}
	if (x>24 && x<=36){
		return 2021;
	}
}

const char* NombreMes (int x){
	switch (x){
		case 0:return "Enero";break;
		case 1:return "Febrero";break;
		case 2:return "Marzo";break;
		case 3:return "Abril";break;
		case 4:return "Mayo";break;
		case 5:return "Junio";break;
		case 6:return "Julio";break;
		case 7:return "Agosto";break;
		case 8:return "Septiembre";break;
		case 9:return "Octubre";break;
		case 10:return "Noviembre";break;
		case 11:return "Diciembre";break;
	}
}

const char* NombreProvincia (int x){
  switch (x){
    case 0:return"Buenos Aires"; break;
    case 1:return"Ciudad Autonoma Bs As";break;
    case 2:return"Catamarca";break;
    case 3:return"Chaco";break;
    case 4:return"Chubut";break;
    case 5:return"Cordoba";break;
    case 6:return"Corrientes";break;
    case 7:return"Entre Rios";break;
    case 8:return"Formosa";break;
    case 9:return"Jujuy";break;
    case 10:return"La Pampa";break;
    case 11:return"La Rioja";break;
    case 12:return"Mendoza";break;
    case 13:return"Misiones";break;
    case 14:return"Neuquen";break;
    case 15:return"Rio Negro";break;
    case 16:return"Salta";break;
    case 17:return"San Juan";break;
    case 18:return"San Luis";break;
    case 19:return"Santa Cruz";break;
    case 20:return"Santa Fe";break;
    case 21:return"Santiago del Estero";break;
    case 22:return"Tierra del Fuego";break;
    case 23:return"Tucuman";break;

  }
}

int MatrizA0 (int arr[26][8][36]){
	int i,j,k;
	for (int k = 0; k < 36; ++k)
	{
		for (int j = 0; j < 8 ; ++j)
		{
			for (int i = 0; i < 26; ++i)
			{
				arr[i][j][k]=0;
			}
		}
	}
	printf("Matriz Inicializada\n");
}

void promedioT (int x, int y, int arr[26][8][36],int j,int anio){
	float promx=0;
	for (int k = x; k < y; ++k)
	{
		promx=promx+arr[25][j][k];
	}
	printf("	El promedio en %d fue de: %f Toneladas\n",anio,promx/12);
}

int main()
{
	int i,j,k,c,r,resprov=0;
	float promT,promM,promO,totO;
	int arr[26][8][36];
	int band=0;
	FILE *arch;
   	struct RegistroResiduos reg;  
   	MatrizA0(arr);
	
	printf(" ----------------------------------------------------------------------\n");
	printf(" ----------------- Laboratorio C - Grupo: NBM Team - ISI A ------------\n");
	printf(" --------------------- Niveyro, Ivan y Brites, Agustin ----------------\n");
	printf(" ----------------------------------------------------------------------\n");
	printf("\n");

	
	arch = fopen ("datos.dat", "rb");
	if (arch == NULL) {
	    fprintf(stderr, " * Error al abrir el archivo *\n");
	    exit (1);
	}
	printf("-------------------------CONTENIDO DEL ARCHIVO-------------------------\n");
	r=0;
	while (!feof(arch)){
		fread(&reg,sizeof(struct RegistroResiduos),1,arch);
		printf ("RegNro: %d - %d/%d/%d: Provincia = %s | Peso = %d | Residuo Tipo = %s \n",++r,reg.fecha.dd,reg.fecha.mm,reg.fecha.aa,reg.Provincia,reg.Peso,reg.TipoDeResiduo);
		//Por alguna razon, cuando creo el archivo data.dat el primer registro toma valores que no corresponden, de esta manera no tomo en cuenta ese primer registro.
		if (band == 0){
			i= NumeroProvincia(reg);
			j= NumeroResiduo(reg);
			k= NumeroMes(reg);
			
			arr[i][j][k]= 0;
			band=1;
		}
		else
		{
		
			i= NumeroProvincia(reg);
			//printf("Provincia numero: %d\n",i );

			j= NumeroResiduo(reg);
			//printf("Tipo de residuo: %d\n", j);
				
			k= NumeroMes(reg);
			//printf("Nro de Matriz que le corresponde (segun mes): %d\n", k);
			
					
			arr[i][j][k]= reg.Peso+arr[i][j][k];
			//arr[25]prov[7]tipo residuo[36]tabla x mes
			arr[i][7][k]=reg.Peso+arr[i][7][k]; //Guado en la ultima fila
			arr[25][j][k]=reg.Peso+arr[25][j][k]; //Guardo en la ultima columna
			arr[25][7][k]= reg.Peso+arr[25][7][k]; //Guardo en la esquina inferior izq el total
			}
	}
	printf("-----------------------------------------------------------------------\n");
	printf("\n");
	fclose (arch);

	
	for (int k = 0; k < 36; ++k)
	{
		promT=promT+arr[25][7][k];
		totO=totO+arr[25][2][k];	
	}
	printf("* El promedio total de residuos recolectados en general es de: %f Toneladas\n",promT/36);
	printf("\n");
	printf("* El exedente total de residuos Organicos es de: %f Toneladas\n",totO);
	printf("\n");
	promO=totO*100;
	promO=promO/promT;
	printf("* El total de residuos Organicos representa un: %f porciento de los residuos\n",promO);
	printf("\n");


	
	printf("* Cada Provincia tienen los siguientes excedentes de reciduos: \n");
	for (int i = 0; i < 24; ++i)
	{
		for (int k = 0; k < 36; ++k)
		{
			resprov=arr[i][2][k]+resprov;
		}
		printf("La provincia de %s genero: %d toneladas \n",NombreProvincia(i),resprov);
		resprov=0;
		
		if (i==23){
			printf("\n");
			printf("* El promedio de tipo residuos recolectados en cada Provincia por anio es: \n");
			for (int j = 0; j < 8; ++j)
			{
			printf("Promedio de Residuos %s:\n",NombreResiduo(j));
			promedioT (0, 12, arr, j,2019);
			promedioT (12, 24, arr, j,2020);
			promedioT (24, 36, arr, j,2021);			
			}
		}
	}

	return 0;
}
