SubProceso carta = Jugador(primera)
	cont2 = 0
	des = 0
	carta = 0
	Mientras des <> 2 Hacer
		cont2 = cont2 + 1
		P = Aleatorio(1,10)
		Si P = 1 Entonces
			Si carta <= 10 Entonces
				P = 11
			SiNo
				P = 1
			Fin Si
		Fin Si
		Escribir sin saltar "Revelando tu carta"
		Esperar 1 segundo
		Escribir sin saltar  "."
		Esperar 1 segundo
		Escribir sin saltar"."
		Esperar 1 segundo
		Escribir "."
		Esperar 1 segundo
		Limpiar pantalla 
		Escribir "Carta del repartidor: " primera 
		Escribir " "
		Escribir "Tu carta número " cont2 " es de: " P
		carta = carta + p
		Escribir "Tu total es de: " carta 
		Si carta >= 21 Entonces
			des = 2
		SiNo
			Escribir " "
			Esperar 2 segundos 
			Escribir "¿Deseas otra carta? (1 = Si, 2 = No)"
			Leer des
			Limpiar pantalla 
		Fin Si
	Fin Mientras
	
FinSubProceso

SubProceso x = Repartidor (primera,f1)
	x = primera 
	cont = 2
	Escribir "El valor de la carta número 1 es de: " x 
	Repetir
		esperar 3 segundos 
		Escribir sin saltar "El valor de la carta número " cont " es de: "
		z = Aleatorio(1,10)
		Si z = 1 Entonces
			Si x <= 10 Entonces
				z = 11
			SiNo
				z = 1
			Fin Si
		Fin Si
		cont = cont + 1
		Escribir z
		x = x + z 
	Hasta Que x >= f1 | x > 17
	Esperar 3 segundos
	Escribir "Total del repartidor: " x 
FinSubProceso



Proceso Blackjack
	desicion = 0
	Escribir "¡Bienvenido, juguemos BlackJack!"
	Escribir " "
	Esperar 3 segundo
	Escribir "Tú comienzas sacando las cartas. "
	escribir "Estaras jugando contra el repartidor."
	Escribir " "
	Esperar 3 segundo
	Repetir
		Escribir "¡Comencemos!"
		Escribir " "
		Primera = Aleatorio (1,10)
		Si primera = 1 Entonces
			primera = 11
		FinSi
		Escribir "El repartidor mostro su primera carta que es " primera 
		Escribir " "
		Esperar 5 segundos 
		f1 = Jugador(primera)
		Si F1 > 21 Entonces
			Escribir "Te has pasado de 21" 
			Esperar 3 segundos 
			Escribir " "
			Escribir "Has perdido..." 
		SiNo
			Esperar 2 segundos 
			Escribir " "
			Escribir "Ahora es turno del repartidor" 
			Escribir " "
			Esperar 2 segundos 
			f2 = Repartidor(primera,f1)
			
			Esperar 3 Segundos
			Limpiar pantalla 
			Escribir "Tu total fue de: " f1
			Esperar 2 segundos 
			Escribir "El del repartidor fue de: " f2 
			Si f2 > 21 Entonces
				Esperar 2 segundos 
				Escribir "El repartidor se ha pasado de 21"
				Esperar 2 segundos 
				Escribir " "
				Escribir "Has ganado"
			SiNo
				Si f2 = f1 Entonces
					Escribir "Empataste con el repartidor" 
				SiNo
					Si f1 > f2 Entonces
						Escribir " "
						Escribir "¡Has Ganado!"
					SiNo
						Escribir " "
						Escribir "Has perdido..."
					Fin Si
					
				Fin Si
			Fin Si
			Esperar 1 segundos 
		Fin Si
		Escribir " "
		Escribir " "
		Esperar 3 segundos 
		Escribir "Deseas jugar de nuevo (1 = Si, 2 = No)"
		Leer desicion 
		Limpiar pantalla 
		Esperar 2 segundos 
	Hasta Que desicion = 2 
	Escribir "Gracias por jugar."
FinProceso
//Juego elaborado por Moisés Arturo Badillo Álvarez 
// A00834306
//Solo Dios y mi yo de ese entonces saben como se hizo este codigo.
