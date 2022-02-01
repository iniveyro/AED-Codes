Ejercicio 5.2.1
Imprimir las cifras de un número n (siendo n >= 0) en orden inverso al original. Por ej.: el inverso de 254 es 452.

Ejercicio 5.2.2
Leer una palabra (una cadena de caracteres) y la cantidad de caracteres y generar su palíndromo. El palíndromo de “Venezuela” es “aleuzeneV”.

Ejercicio 5.2.3
Dada una lista de nombres ordenada en forma ascendente, construir un procedimiento recursivo que imprima como salida la misma lista, pero en orden descendente, sin modificar la lista original.

Ejercicio 5.2.4
Para convertir un número decimal a binario, simplemente debe dividirse sucesivas veces por dos (2) hasta quedarnos con el cociente cero (0). Todos los restos de las divisiones, tomados en orden inverso, forman el número binario objetivo. Escribir un procedimiento recursivo que, recibiendo como parámetro un número entero positivo, muestre en pantalla el mismo número codificado en binario.

//////////////////////////////////////////////6

Procedimiento ejer1 (n:entero) es

    Si (n < 10) y (n >= 0) entonces
        Esc(n)
    Sino  
        Esc(n MOD 10)
        ejer1(n DIV 10)
    FinSi
    
FinProcedimiento

Procedimiento ejerc2 (Arr: arreglo [1...10] de caracteres, i: entero)es
    Si i = 10 entonces
        Esc(arr[i])
    Sino
        ejerc2(arr,i+1)
        Esc(arr[i])
    FinSi
FinProcedimiento


Procedimiento ejerc3 (p:puntero a Nodo) es
    Si *p.prox = null entonces
        Esc(*p.dato)
    Sino
        ejerc3(*p.prox)
    FinSi
FinProcedimiento

Procedimiento ejerc3 (p:puntero a Nodo) es // otra forma
    Si *p.prox <> null entonces
        ejerc3(*p.prox)
    FinSi
    Esc(*p.dato)
FinProcedimiento