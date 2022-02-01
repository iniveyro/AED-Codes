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
 	char Provincia[20];
  	float Peso;
  	char TipoDeResiduo[1];
};

struct RegistroResiduos reg;

float PrepararMatriz (float arr[25][7][37]){
	int i,j,k;
	for(k = 0; k <= 36; ++k) {
		for(j = 0; j <= 6; ++j) {
			for (i = 0; i <= 24; i++){
				arr[i][j][k]=0;
			}		
		}
	}

	printf(" * Matriz Inicializada en 0 * \n");
}

int NumeroMes (struct RegistroResiduos reg){
	switch (reg.fecha.mm){
		case 2019: return reg.fecha.dd;break;
		case 2020: switch (reg.fecha.mm){
						case 1: return 13;break;
						case 2: return 14;break;
						case 3: return 15;break;
						case 4: return 16;break;
						case 5: return 17;break;
						case 6: return 18;break;
						case 7: return 19;break;
						case 8: return 20;break;
						case 9: return 21;break;
						case 10: return 22;break;
						case 11: return 23;break;
						case 12: return 24;break;
					}
		case 2021: switch (reg.fecha.mm){
						case 1: return 25;break;
						case 2: return 26;break;
						case 3: return 27;break;
						case 4: return 28;break;
						case 5: return 29;break;
						case 6: return 30;break;
						case 7: return 31;break;
						case 8: return 32;break;
						case 9: return 33;break;
						case 10: return 34;break;
						case 11: return 35;break;
						case 12: return 36;break;
					}
	}
}

int NumeroProvincia (struct RegistroResiduos reg){
	if (reg.Provincia=="Buenos Aires"){return 1;}
	if (reg.Provincia=="Ciudad Autonoma Bs As"){return 2;}
	if (reg.Provincia=="Catamarca"){return 3;}
	if (reg.Provincia=="Chaco"){return 4;}
	if (reg.Provincia=="Chubut"){return 5;}
	if (reg.Provincia=="Cordoba"){return 6;}
	if (reg.Provincia=="Corrientes"){return 7;}
	if (reg.Provincia=="Entre Rios"){return 8;}
	if (reg.Provincia=="Formosa"){return 9;}
	if (reg.Provincia=="Jujuy"){return 10;}
	if (reg.Provincia=="La Pampa"){return 11;}
	if (reg.Provincia=="La Rioja"){return 12;}
	if (reg.Provincia=="Mendoza"){return 13;}
	if (reg.Provincia=="Misiones"){return 14;}
	if (reg.Provincia=="Neuquen"){return 15;}
	if (reg.Provincia=="Rio Negro"){return 16;}
	if (reg.Provincia=="Salta"){return 17;}
	if (reg.Provincia=="San Juan"){return 18;}
	if (reg.Provincia=="San Luis"){return 19;}
	if (reg.Provincia=="Santa Fe"){return 20;}
	if (reg.Provincia=="Santiago del Estero"){return 21;}
	if (reg.Provincia=="Santa Cruz"){return 22;}
	if (reg.Provincia=="Tierra del Fuego"){return 23;}
	if (reg.Provincia=="Buenos"){return 24;}
}

int NumeroResiduo (struct RegistroResiduos reg){
		if (reg.Provincia=="P"){return 1;}
		if (reg.Provincia=="M"){return 2;}
		if (reg.Provincia=="O"){return 3;}
		if (reg.Provincia=="T"){return 4;}
		if (reg.Provincia=="V"){return 5;}
		if (reg.Provincia=="E"){return 6;}
}

const char* NombreResiduo (int x){
  switch (x){
    case 1:return"Plastico";break;
    case 2:return"Metalico";break;
    case 3:return"Organico";break;
    case 4:return"Textil";break;
    case 5:return"Vidrio";break;
    case 6:return"Electronica";break;
  }
}

const char* NombreMes (int x){
	switch (x){
		case 1:return "Enero";break;
		case 2:return "Febrero";break;
		case 3:return "Marzo";break;
		case 4:return "Abril";break;
		case 5:return "Mayo";break;
		case 6:return "Junio";break;
		case 7:return "Julio";break;
		case 8:return "Agosto";break;
		case 9:return "Septiembre";break;
		case 10:return "Octubre";break;
		case 11:return "Noviembre";break;
		case 12:return "Diciembre";break;
	}
}

const char* NombreProvincia (int x){
  switch (x){
    case 1:return"Buenos Aires"; break;
    case 3:return"Ciudad Autonoma Bs As";break;
    case 4:return"Catamarca";break;
    case 5:return"Chaco";break;
    case 6:return"Chubut";break;
    case 7:return"Cordoba";break;
    case 8:return"Corrientes";break;
    case 9:return"Entre Rios";break;
    case 10:return"Formosa";break;
    case 11:return"Jujuy";break;
    case 12:return"La Pampa";break;
    case 13:return"La Rioja";break;
    case 14:return"Mendoza";break;
    case 15:return"Misiones";break;
    case 16:return"Neuquen";break;
    case 17:return"Rio Negro";break;
    case 18:return"Salta";break;
    case 19:return"San Juan";break;
    case 20:return"San Luis";break;
    case 21:return"Santa Fe";break;
    case 22:return"Santiago del Estero";break;
    case 23:return"Tierra del Fuego";break;
    case 24:return"Tucuman";break;

  }
}

int main()
{
	int i,j,k=0;
	int Total,Total3=0;
	float arr[25][7][37];
	FILE *arch;
   	struct RegistroResiduos reg;  
	arch = fopen ("datos.dat", "rb");

	PrepararMatriz(arr);

	printf(" ---------------------------------------------------\n");
	printf(" ----- Laboratorio C - Grupo: NBM Team - ISI A -----\n");
	printf(" ---------- Niveyro Ivan y Brites, Agustin ---------\n");
	printf(" ---------------------------------------------------\n");
	printf("\n");

	if (arch == NULL) {
	    fprintf(stderr, " * Error al abrir el archivo *\n");
	    exit (1);
	}

	while (!feof(arch)){
		fread(&reg,sizeof(reg),1,arch);
		//printf ("%d/%d/%d: Provincia = %s | Peso = %f | Residuo Tipo = %s \n",reg.fecha.dd,reg.fecha.mm,reg.fecha.aa,reg.Provincia,reg.Peso,reg.TipoDeResiduo);
		i= NumeroProvincia(reg);
		j= NumeroResiduo(reg);
		k= NumeroMes(reg);
		 
		arr[i][j][k]= reg.Peso;
		//arr[25]prov[7]tipo residuo[37]tabla x mes
		arr[24][j][k]= reg.Peso+arr[24][j][k];//Guardo masa x tipo de residuo
		arr[i][6][k]= reg.Peso+arr[i][6][k]; //Guardo masa x provincia
		arr[24][6][k]= reg.Peso + arr[24][6][k]; // Acumulo total x mes 
	}

	///*El Promedio de residuos recolectados en cada provincia discriminados por Tipo de Residuo,anual y total.
	for (int k = 0; k <= 23; ++k){
	 	for (int j = 0; j <= 5; ++j){
	 		for (int i = 0; i <= 11; ++i)
	 		{
	 			Total = Total + arr[i][j][k];
	 		}
	 		
			Total3=Total;
			Total=0;
	 		printf ("%d - %d - %d - Promedio: %d \n",NombreProvincia(k+1),NombreResiduo(j+1),NombreMes(i+1),Total/12);
	 		
	 		for (int i = 12; i <= 23; ++i)
	 		{
	 			Total = Total + arr[i][j][k];
	 		}
	 		
	 		Total3=Total+Total3;
			Total=0;
	 		printf ("%d - %d - %d - Promedio: %d \n",NombreProvincia(k+1),NombreResiduo(j+1),NombreMes(i-11),Total/12);
	 	
	 		for (int i = 24; i <= 35; ++i)
	 		{
	 			Total = Total + arr[i][j][k];
	 		}

	 		Total3=Total+Total3;
	 		printf ("%d - %d - %d - Promedio: %d \n",NombreProvincia(k+1),NombreResiduo(j+1),NombreMes(i-23),Total/12);
	 		printf("-------------------------------------------------------------------------\n");
	 		printf ("%d - %d - %d - Promedio Anual: %d \n",NombreProvincia(k),NombreResiduo(j),NombreMes(i-24),Total3/36);
	 		Total=0;
	 	}
	} 
	
	////Cuál fue el departamento que más desechos del tipo comestibles alnanzo en los tres años y cuanto es su masa en toneladas en total.
	int K,z;
	for (int i = 0; i <= 35; ++i)
	 {
	 	if (K <= arr[i][36][2])
	 	{
	 		K = arr[i][36][2];
			z = i; 
	 	}
	 } 
	printf("El departamento con toneledas acumuladas en tres años es: %s con %d Toneladas \n",NombreProvincia(z+1),K );
	
	///*Del departamento con más desechos en los tres años, ¿Cuál es el tipo de desecho que más abunda?
	K = 0;
	z=0;
	for (int j = 0; j <= 23; ++j)
	{
		if (K<=arr[36][j][2])
		{
			K=arr[36][j][2];
			z=j;
		}
	}
	int T;
	for (int k = 0; k <= 5; ++k)
	{
		if (T<=arr[36][z][k])
		{
			T=arr[36][z][k];
			i=k;
		}
	}
	printf("De la Provincia con mas desechos, el que mas abunda es el: %s con %d Toneladas\n",NombreResiduo(i+1),T );

	//////*Cantidad total de Metales 
	printf("------------------------------------------------------------------------\n");
	printf("La cantidad total de Residuos metalicos es de: %d Toneladas",arr[36,24,1]);
	printf("-------------------------------------------------------------------------\n");
	fclose (arch);
	return 0;



	
}
