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

const char* NombreResiduo (int x){
  switch (x){
    case 1:return"P";break;
    case 2:return"M";break;
    case 3:return"O";break;
    case 4:return"T";break;
    case 5:return"V";break;
    case 6:return"E";break;
  }
}


const char* NombreProvincia (int x){
  switch (x){
    case 1:return"Buenos Aires"; break;
    case 2:return"Ciudad Autonoma Bs As";break;
    case 3:return"Catamarca";break;
    case 4:return"Chaco";break;
    case 5:return"Chubut";break;
    case 6:return"Cordoba";break;
    case 7:return"Corrientes";break;
    case 8:return"Entre Rios";break;
    case 9:return"Formosa";break;
    case 10:return"Jujuy";break;
    case 11:return"La Pampa";break;
    case 12:return"La Rioja";break;
    case 13:return"Mendoza";break;
    case 14:return"Misiones";break;
    case 15:return"Neuquen";break;
    case 16:return"Rio Negro";break;
    case 17:return"Salta";break;
    case 18:return"San Juan";break;
    case 19:return"San Luis";break;
    case 20:return"Santa Fe";break;
    case 21:return"Santa Cruz";break;
    case 22:return"Santiago del Estero";break;
    case 23:return"Tierra del Fuego";break;
    case 24:return"Tucuman";break;

  }
}

int Random (int M, int N){
  return rand () % (N-M+1) + M;   // Este está entre M y N
}

int main () {

   FILE *arch;
   struct RegistroResiduos reg; 
   int regs;
   struct RegistroResiduos RegistroResiduos[2000];
   for (int i = 1; i <= 2000; ++i)
   {
      
      RegistroResiduos[i].fecha.dd=Random(1,29);
      RegistroResiduos[i].fecha.mm=Random(1,12);
      RegistroResiduos[i].fecha.aa=Random(2019,2021);
      //RegistroResiduos[i].Provincia=NombreProvincia(Random(1,24));
      strcpy(RegistroResiduos[i].Provincia,NombreProvincia(Random(1,24)));
      RegistroResiduos[i].Peso=Random(1,100);
      strcpy(RegistroResiduos[i].TipoDeResiduo,NombreResiduo(Random(1,6)));
      //RegistroResiduos[i].TipoDeResiduo=NombreResiduo(Random(1,6)); 
   }
   
   arch = fopen ("datos.dat", "wb");

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
   return 0;
}