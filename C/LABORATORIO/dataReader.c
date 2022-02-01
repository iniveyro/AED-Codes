#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct 
{
  char nombre[30]; 
  int pob_urb;
  int hacin_urb;
  int pob_rur_agrup;
  int hacin_rur_agrup;
  int pob_rur_disp;
  int hacin_rur_disp;
  int pob_total;
} Depto;

int main(int argc, char const *argv[])
{
  FILE *fh = fopen(argv[1], "rb"); // read binary!!! not normal text reading
  if (!fh)
  {
    fprintf(stderr, "Error abriendo el archivo '%s'\n", argv[1]);
    return EXIT_FAILURE;
  }

  Depto *depto = malloc(sizeof(Depto));
  while( fread(depto, sizeof(Depto), 1, fh) > 0) 
  {
    printf("Leido: %s", depto->nombre);
    printf(" %d", depto->pob_urb);
    printf(" %d", depto->hacin_urb);
    printf(" %d", depto->pob_rur_agrup);
    printf(" %d", depto->hacin_rur_agrup);
    printf(" %d", depto->pob_rur_disp);
    printf(" %d", depto->hacin_rur_disp);
    printf(" %d\n", depto->pob_total);

  }

  return EXIT_SUCCESS;
}
