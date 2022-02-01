|Accion  Archivos+Listas() Es
|Ambiente
|
|	|Vendedor = Registro
|	|
|	|	ID_Vendedor: N(8);
|	|	|Mes = Registro
|	|	|	
|	|	|	mes: 1..12;
|	|	|	hs-reg: N(3);
|	|	|	hs-Extra: N(3);
|	|	|	Ventas: Real;
|	|	|
|	|	|Fin Registro
|	|
|	|Fin Registro
|
|	Vend: Archivo de Vendedor, ordenado por ( ID_Vendedor, Mes );
|	V: Vendedor;
|
|	|DatosPerdonales = Registro
|	|
|	|	ID_Vendedor: N(8);
|	|	ApYNom: AN(30);
|	|	Ganancias: Real;
|	|
|	|Fin Registro
|
|	Dat_Pers: Archivo de DatosPerdonales, Indexado por ( ID_Vendedor );
|	dt: DatosPerdonales;
|
|
|
|
|	// Usaremos una Lista para El ranking y luego mostrar al final, recorriendo toda la Lista;
|	// usaremos una Lista doble, porque es mejor.
|	// La consigna puede que pida una Lista simple, pero por conveniencia usaremos la Lista doble
|
|	|Salida = Registro
|	|
|	|	ID_Vendedor: N(8);
|	|	Relacion: Real;
|	|	prox: Puntero a Salida;
|	|	ant: Puntero a Salida;
|	|
|	|Fin Registro
|
|	Prim,Ult,p,q: Puntero a Salida;
|
|
|	|TotalCantidadVendedores|Total hs|Total Ventas|Total Comision|
|	Totales: Arreglo [1..4] de Entero;
|
|	Comision:= Real;
|	
|
|
|
|
|
|
|Algoritmo
|	
|	
|Abrir E/ (Vend); Leer (Vend,v);
|Abrir E/ (Dat_Pers);
|
|Prim:= Null;
|p:= Null;
|q:= Null; //conveniencia
|
| |Para (i:=0 Hasta 4) Hacer
| |	
| |	Totales[i]:= 0;
| |
| |Fin Para
|
|
|Escribir ( "			ID-Vendedor |  Nombre y Apellido  |   HS-REG   |   HS-EXTRAS   |   IMPORTE VENTAS    |   COMISION" )
||Mientras ( NoFDA (Vend) ) Hacer
||	#Leer (Vend,v);
||
||	|Segun ( v.Mes.mes ) Hacer	
||	|
||	|	=1:Escribir ("Enero         ");
||	|	=2:Escribir ("Febrero       ");
||	|	=3:Escribir ("Marzo         ");
||	|	=4:Escribir ("Abril         ");
||	|	=5:Escribir ("Mayo          ");
||	|	=6:Escribir ("Junio         ");
||	|	=7:Escribir ("Julio         ");
||	|	=8:Escribir ("Agosto        ");
||	|	=9:Escribir ("Septiembre    ");
||	|	=10:Escribir ("octubre      ");
||	|	=11:Escribir ("Noviembre    ");
||	|	=12:Escribir ("Diciembre    ");
||	|
||	|Fin Segun
||	
||	dt.ID-Vendedor:= v.ID-Vendedor;
||	#ResgID:= v.ID-Vendedor;
||	Leer (Dat_Pers,dt);
||
||
||	|Si Existe Entonces
||	|
||	|	Rank:= Rank + 1;
||	|	Escribir ("          ",dt.ID-Vendedor," |  ",dt.ApYNom,  "    |    ",v.Mes.hs-reg,"   |   ",v.Mes.hs-Extra , "   |  "v.Mes.Ventas,"   |   ");
||	|
||	|	Si ( (v.hs-reg >= 160) y (v.Ventas > 3200) ) Entonces
||	|
||	|		Comision:= ((reg_pers.gan / 1000) * (reg_vend.info[i].vtas - 3200));
||	|
||	|	Fin Si
||	|
||	|	Escribir (Comision);
||	|	Totales[3]:= Totales[3] + Comision;
||	|	Totales[3]:= Totales[2] + v.Ventas;
||	|	Totales[3]:= Totales[1] + v.hs-reg + v.hs-Extra;
||	|	Totales[3]:= Totales[0] + 1; //Cantidad De Vendedores Total General No por meses.
||	|
||	|	Relacion:= ( v.Mes.Ventas / (v.Mes.hs-reg + v.Mes.hs-Extra) );
||	|
||	|
||	|
||	|	//Creamos una Lista Para el ranking Ordenamos de mayor a menor (Mayor>meno) == (p>q)
||	|
||	|	Nuevo(q);
||	|	*q.ID-Vendedor:=v.ID-Vendedor;
||	|	*q.Relacion:= Relacion;
||	|
||	|	|Si ( Prim=Null ) Entonces // Agregamos primer Elemento
||	|	|
||	|	|	*q.prox:=Null;
||	|	|	*q.ant:=Null;
||	|	|	Prim:=q;
||	|	|	Ult:=q;
||	|	|
||	|	|	Sino 
||	|	|
||	|	|		p:=Prim;
||	|	|
||	|	|		|Mientras (p< > Null) y (*p.Relacion > *q.Relacion) Hacer
||	|	|		|
||	|	|		|	p:=*p.prox;
||	|	|		|
||	|	|		|Fin Mientras
||	|	|
||	|	|		|Si ( p=Prim ) Entonces
||	|	|		|
||	|	|		|	*q.prox:= Prim;
||	|	|		|	*p.ant:= q;
||	|	|		|	*q.ant:= Null;
||	|	|		|	Prim:= q;
||	|	|		|
||	|	|		|	Sino
||	|	|		|
||	|	|		|		|Si ( p=Null ) Entonces 
||	|	|		|		|
||	|	|		|		|	*q.ant:= Ult;
||	|	|		|		|	*Ult.prox:= q;
||	|	|		|		|	*q.prox:= Null;
||	|	|		|		|	Ult:= q;
||	|	|		|		|
||	|	|		|		|	Sino
||	|	|		|		|	
||	|	|		|		|		*(p.ant).prox:= q;
||	|	|		|		|		*q.ant:= *p.ant;
||	|	|		|		|		*q.prox:= p;
||	|	|		|		|		*p.ant:= q;
||	|	|		|		|
||	|	|		|		|Fin Si
||	|	|		|
||	|	|		|Fin Si
||	|	|
||	|	|
||	|	|Fin Si
||	|
||	|Fin si
||
||Leer (Vend,v);
||Fin mientras
|
|//Emitimos los Totales
|
|Escribir ( "Total Cantidad Vendedores   -    Total HS  -   Total Ventas   -    Total Comision" );
|Escribir (     Totales[0],"                 ",Totales[1],"    ",Totales[2], "      ",Totales[3]);
|
|//Emitimos el Rankin Mayor a menor
|
|p:=Prim;
|Escribir ( " Ranking   ID    IMPORTE");
|
|Mientras (p< > Null) Hacer
|	
|	Escribir (Rank, "   ", *p.ID-Vendedor, "   " , *p.Relacion);	
|	Rank:= Rank - 1;
|
|Fin Mientras
|
|// En el Ejercicio Resuelto elimina todos los nodos Ni en pedo borro 
|
|
|Cerrar (Vend); Cerrar (Dat_Pers);
|Fin Accion