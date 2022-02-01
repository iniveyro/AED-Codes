#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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


int main () {

   FILE *arch;
   struct RegistroResiduos reg;  
   int regs;
   int a=0;
   arch = fopen ("datos.dat", "rb");

   if (arch == NULL) {
      fprintf(stderr, "\nError al abrir el archivo\n");
      exit (1);
   }

   while(fread(&reg, sizeof(struct RegistroResiduos), 1, arch)){
      printf ("%d - %d/%d/%d: Provincia = %s | Peso = %d | Residuo Tipo = %s \n",++a,reg.fecha.dd,reg.fecha.mm,reg.fecha.aa,reg.Provincia,reg.Peso,reg.TipoDeResiduo);
   }


   fclose (arch);

   return 0;
}