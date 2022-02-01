ACCIÓN Concurso ES
AMBIENTE
	sec, sal1, sal2: secuencia de caracter
	v: caracter
	pais1, pais2, a1, a2, a3, a4: caracter
	p1_99, p2_99, total, totErr: entero
	num={"0","1","2","3","4","5","6","7","8","9"}
	Procedimiento ConvAño es  //procedimiento para resguardar los datos de la ventana que indican el año
		a1:=v 
		Avz(sec, v)
		a2:=v
		Avz(sec, v)
		a3:=v
		Avz(sec, v)
		a4:=v
		añoS:=Año(a1, a2, a3, a4)
		Avz(sec, v)
	Fin_Procedimiento
	Función Año(a1, a2, a3, a4: caracter):entero //funcion para convertir los caracteres año en un entero año 
		Según a1 hacer							 //(se ejecuta en el procedimiento ConvAño)
			="0": aux1:=0
			="1": aux1:=1
			="2": aux1:=2
			="3": aux1:=3
			="4": aux1:=4
			="5": aux1:=5
			="6": aux1:=6
			="7": aux1:=7
			="8": aux1:=8
			="9": aux1:=9
		Fin_Según
		Según a2 hacer
			="0": aux2:=0
			="1": aux2:=1
			="2": aux2:=2
			="3": aux2:=3
			="4": aux2:=4
			="5": aux2:=5
			="6": aux2:=6
			="7": aux2:=7
			="8": aux2:=8
			="9": aux2:=9
		Fin_Según
		Según a3 hacer
			="0": aux3:=0
			="1": aux3:=1
			="2": aux3:=2
			="3": aux3:=3
			="4": aux3:=4
			="5": aux3:=5
			="6": aux3:=6
			="7": aux3:=7
			="8": aux3:=8
			="9": aux3:=9
		Fin_Según
		Según a4 hacer
			="0": aux4:=0
			="1": aux4:=1
			="2": aux4:=2
			="3": aux4:=3
			="4": aux4:=4
			="5": aux4:=5
			="6": aux4:=6
			="7": aux4:=7
			="8": aux4:=8
			="9": aux4:=9
		Fin_Según
		Año:=aux4*1000+aux3*100+aux2*10+aux1
	Fin_Función
PROCESO
	Arr(sec); Avz(sec, v)
	Crear(sal1); Crear(sal2)
	cP1:=0; cP2:=0; total:=0; totErr:=0; p1_99:=0; p2_99:=0
	Esc("Ingrese dos países de los que se desea conocer la cantidad de escultores. Ej: 'A, P'.-")
	Leer(pais1, pais2)
	Mientras NFDS(sec) hacer
		Mientras v <> "|" hacer
			Si v <> pais1 y v <> pais2 entonces
				Mientras v no en num hacer
					Avz(sec, v)
				Fin_Mientras
				ConvAño
				Si 1900 < añoS o añoS > 2021 entonces
					totErr:=totErr+1
				Fin_Si
			Sino
				Si v = pais1 entonces
					Para i hasta 31 hacer
						Esc(sal1, v)
						Avz(sec, v)
					Fin_Para
					ConvAño
					Si 1900 < añoS o añoS > 2021 entonces
						totErr:=totErr+1
						Esc(sal1, a4)
						Esc(sal1, a3)
						Esc(sal1, a2)
						Esc(sal1, a1)
						Esc(sal1, "|")
					Sino
						Si añoS < 2000 entonces
							p1_99:=p1_99+1
						Fin_Si
						Esc(sal1, a1)
						Esc(sal1, a2)
						Esc(sal1, a3)
						Esc(sal1, a4)
						Esc(sal1, "|")
					Fin_Si
				Sino
					Para i hasta 31 hacer
						Esc(sal2, v)
						Avz(sec, v)
					Fin_Para
					ConvAño
					Si 1900 < añoS o añoS > 2021 entonces
						totErr:=totErr+1
						Esc(sal2, a4)
						Esc(sal2, a3)
						Esc(sal2, a2)
						Esc(sal2, a1)
						Esc(sal2, "|")
					Sino
						Si añoS < 2000 entonces
							p2_99:=p2_99+1
						Fin_Si
						Esc(sal2, a1)
						Esc(sal2, a2)
						Esc(sal2, a3)
						Esc(sal2, a4)
						Esc(sal2, "|")
					Fin_Si					
				Fin_Si
			Fin_Si
		Fin_Mientras
		total:=total+1
		Avz(sec, v)
	Fin_Mientras
	Esc("Del país ", pais1, " participan ", p1_99, " que comenzaron en la disciplina antes del año 2000.")
	Esc("Del país ", pais2, " participan ", p2_99, " que comenzaron en la disciplina antes del año 2000.")
	Esc("El porcentaje de escultores con información errónea es de ", totErr/total*100, "%.")
	Cerrar(sec); Cerrar(sal1); Cerrar(sal2)
FIN_ACCIÓN