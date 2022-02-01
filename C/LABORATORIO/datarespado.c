#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct RegistroFecha{
		int dd;
		int mm;
		int aa;
};

struct RegistroResiduos{ 
	char TipoDeResiduo[1];
	char Provincia[25];
	float Peso;
	struct RegistroFecha fecha;
};


int main () {

   FILE *arch;
   struct RegistroResiduos reg; 
   int regs;

   struct RegistroResiduos RegistroResiduos[10] = {
                                {"P","Chaco",20.3,13,2,2020},
                                {"M","Buenos Aires",22.1,1,12,2020},
                                {"C","Jujuy",336.1,3,2,2020},
                                {"V","Catamarca",56.8,1,2,2020},
                                {"T","Corrientes",99.1,27,2,2020},
                                {"O","Misiones",56.1,1,6,2020},
                                {"E","Formosa",78.8,2,6,2020},
                              };

   arch = fopen ("datosprueba.dat", "w");

   if (arch == NULL) {
      fprintf(stderr, "\nError al abrir el archivo\n");
      exit (1);
   }

   regs = fwrite (RegistroResiduos, sizeof(RegistroResiduos), 1, arch);

   //printf("%d\n", regs);

   if(regs != 0)
      printf("Se han guardado correctamente los datos!\n");
   else
      printf("Error al guardar!\n");

   fclose (arch);
/*
   //abro para leer
   FILE *inf;

   arch = fopen ("datos.dat", "r");
   if (arch == NULL) {
      fprintf(stderr, "\nError al abrir para leer el archivo...\n");
      exit (1);
   }

   while(fread(&reg, sizeof(struct Ventas), 1, arch))
      printf ("Id = %d Fecha = %d Nombre = %s Monto = %f\n", reg.id, reg.fecha, reg.cliente, reg.monto);

   fclose (arch);

   return 0;
*/
}