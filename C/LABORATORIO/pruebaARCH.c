#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Ventas {
   int id;
   char tipo[1]; //C: Contado, T: Cuenta Corriente
   int fecha; //aaaammdd
   char cliente[30];
   int vendedor; //1..15
   float monto;
};
int main () {

   FILE *arch;
   struct Ventas reg; 
   int regs;
/*
   struct Ventas ventas[5] = {
                                {1, "C", 20200801, "Juan Carlos", 12, 88.123},
                                {1, "C", 20200801, "asdasdx", 8, 100.123},
                                {1, "T", 20200801, "sdxxxxds", 12, 818.55},
                                {1, "C", 20200802, "ASd", 9, 258.23},
                                {1, "T", 20200802, "Condorito", 2, 456.9},
                              };

   arch = fopen ("datosprueba.dat", "w");

   if (arch == NULL) {
      fprintf(stderr, "\nError al abrir el archivo\n");
      exit (1);
   }

   regs = fwrite (ventas, sizeof(ventas), 1, arch);

   //printf("%d\n", regs);

   if(regs != 0)
      printf("Se han guardado correctamente los datos!\n");
   else
      printf("Error al guardar!\n");

   fclose (arch);
*/

   arch = fopen ("datosprueba.dat", "r");
   if (arch == NULL) {
      fprintf(stderr, "\nError al abrir para leer el archivo...\n");
      exit (1);
   }

   while(fread(&reg, sizeof(struct Ventas), 1, arch))
      printf ("Id = %d Fecha = %d Nombre = %s Monto = %f\n", reg.id, reg.fecha, reg.cliente, reg.monto);

   fclose (arch);

   return 0;
}