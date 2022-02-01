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
  FILE *fh_in = fopen(argv[1], "r");
  if (!fh_in)
  {
    fprintf(stderr, "Error abriendo el archivo '%s'\n", argv[1]);
    return EXIT_FAILURE;
  }
  FILE *fh_out = fopen(argv[2], "wb"); // write binary!!! not normal text writing

  Depto *depto = malloc(sizeof(Depto));

  char *line = NULL;
  size_t line_size = 0;
  getline(&line, &line_size, fh_in); // skip the csv headers
  while(getline(&line, &line_size, fh_in) >= 0) 
  {
    printf("Formateado: %s", line);

    // parto la linea en substrings divididos por ";"
    char *token = strtok(line, ";");
    strcpy(depto->nombre, token);

    // strtok(NULL, ";") lee el siguiente substring
    depto->pob_urb = atoi(strtok(NULL, ";"));
    depto->hacin_urb = atoi(strtok(NULL, ";"));
    depto->pob_rur_agrup = atoi(strtok(NULL, ";"));
    depto->hacin_rur_agrup = atoi(strtok(NULL, ";"));
    depto->pob_rur_disp = atoi(strtok(NULL, ";"));
    depto->hacin_rur_disp = atoi(strtok(NULL, ";"));
    depto->pob_total = atoi(strtok(NULL, ";"));

    fwrite(depto, sizeof(Depto), 1, fh_out);
  }

  return EXIT_SUCCESS;
}
