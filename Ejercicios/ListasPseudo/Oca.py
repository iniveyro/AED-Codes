Accion Oca (Prim,ult: Puntero a OCA) Es // Lista Circular
Ambiente

OCA = Registro
	
	Salto: -5..5;
	Puntaje: 0..100;
	Prox:Puntero a OCA;
	Ant: Puntero a OCA;

Fin Registro

//Tirar, devuelve la cantidad de Casilleros que debo moverme
p: Puntero a OCA;

Band,Sigue: Booleano

Nombre: AN(40);













Procedimiento Avanzar-Retroceder (p: Puntero a OCA, Dadito:Entero, Var Bandera:  ) Es



Algooritmo






	

Fin Procedimiento





















Algooritmo
	


	Esc ("Ingrese su nombre de Jugador:  "); Leer (Nombre); //Podriamos validarlo pero no es necesario

	Puntaje:=0;
	p:=Prim;
	Mientras ((Tiradas < > 50) y (p < > null))  Hacer

		Dado = Tirar();
		Band:= True;
		Sigue:= True;

		Mientras ( ( Dado < > 0 ) )  Hacer 
			
			

			Si  ( Dado > 1 )  Entonces // Quiere decir que va a dar un salto a null, y luego a un nodo anterior


				Si ( p = ult ) Entonces 

					band:= False; // Retrocedemos Hasta prim					
	
					Sino 

						Si ( p = Prim)  Entonces 

							Band = True; // Avanzamos hacia Delante;
					
						Fin si

				Fin si

				Sino

				Si (Dado = 1) Entonces
								
					Si ( ( ( p = Prim ) o ( p = ult ) ) Entonces  // Quire decir que Termina el juego, porque si es =1, entonces solo existe un salto mas y va a ser hacia null

						Sigue:= False; // Vamos a seguir Moviendonos
					
					Fin si
					

				Fin si


			Fin si


			Si ( Sigue ) Entonces // Si es Verdadero es para decirnos que aun sigue jugando y segun Band, avanza hacia atras o delante


				Si ( Band ) Entonces

					//Avanzamos hacia Delante
					p:=*p.prox;

					Sino 
						//Retrocedemos
						p:= *p.ant;

				Fin si 

				Dado:= Dato-1; // Es para restar el salto hacia Null

				Sino

				Esc ("Fin del Juego");
				
					
			Fin si

		Fin mientras

		









		Si ( p < > Null ) Entonces
			Puntaje:= Puntaje + *p.Puntaje;
			Dado:= *p.Salto;
		Fin si



		Sigue:= True;
		Mientras ( ( p < > Null ) Y ( Dado < > 0 ) ) Hacer // Para analizar los saltos

			Si (Dado < 0 ) Entonces // Retrocede en Saltos, Quiere Decir Que el Salto es un numero Negativo


				Si ( p = prim ) Entonces 

					// Quiere decir que avanzamos hacia delante no hacia atras pero restandole la posicion de l Null

					band = True;


					Sino

						Si ( p = Ult ) Entonces // Quiere decir que retrocedemos hasta prim nuevamente de ser necesario

							band = False;

						Fin si

						

				Fin si

				Sino


					Si ( Dado = -1 ) Entonces  // Quiere decir que existe un solo salto mas, y veremos si p=prim, el unico salto que falta es hacia null, entonces termina

						Si ( ( p = Pirm ) o ( p = Ult ) ) Entonces 

							Sigue:= False; // Quiere decir que termina el juego						

						Fin si




					Fin si



					Si ( Sigue ) Entonces // Si es Verdadero es para decirnos que aun sigue jugando y segun Band, avanza hacia atras o delante


						Si ( Band ) Entonces

							//Avanzamos hacia Delante
							p:=*p.prox;

							Sino 
								//Retrocedemos
								p:= *p.ant;

						Fin si 

					Fin si

					Dado:= Dato + 1; // Es para restar el salto hacia Null
				
				Sino 

				 	Si ( Dado > 0 ) Entonces


						Si ( p = prim ) Entonces 

							// Quiere decir que avanzamos hacia delante no hacia atras pero restandole la posicion de l Null

							band = True;


							Sino

								Si ( p = Ult ) Entonces // Quiere decir que retrocedemos hasta prim nuevamente de ser necesario

									band = False;

								Fin si

						

						Fin si

						Sino


						Si ( Dado = 1 ) Entonces  // Quiere decir que existe un solo salto mas, y veremos si p=prim, el unico salto que falta es hacia null, entonces termina

							Si ( ( p = Pirm ) o ( p = Ult ) ) Entonces 

								Sigue:= False; // Quiere decir que termina el juego						

							Fin si


						

						Fin si



						Si ( Sigue ) Entonces // Si es Verdadero es para decirnos que aun sigue jugando y segun Band, avanza hacia atras o delante


							Si ( Band ) Entonces

								//Avanzamos hacia Delante
								p:=*p.prox;

								Sino 
									//Retrocedemos
									p:= *p.ant;

						Fin si 

						Dado:= Dato-1; // Es para restar el salto hacia Null

		




				 	Fin si


			Fin si





		Fin mientras





		Si ( Band ) Entonces

			//Avanzamos hacia Delante
			p:=*p.prox;

			Sino 
				//Retrocedemos
				p:= *p.ant;

		Fin si 


	Fin Mientras



Esc ("Puntaje: ",Puntaje);



Fin Accion


