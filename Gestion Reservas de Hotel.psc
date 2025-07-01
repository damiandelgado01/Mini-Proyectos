Algoritmo ReservaHotel
	//Indicamos datos a recopilar para realizar una reserva
	Definir cliente, tipohabitacion, estadohabitacion, habitacionasignada Como Texto
	Definir opcionmenu, rutcliente, numhabitacion, habitaciondisponible, preciodia, precionoche, preciototal, reservashechas, i, j Como Entero
	Definir fechaentrada, fechasalida Como Real
	Definir cancelarreserva Como Logico
	
	//El maximo de reservas a realizar son 3 reservas
	Dimension numhabitacion[3], tipohabitacion[3], preciodia[3], precionoche[3], estadohabitacion[3], fechaentrada[3], fechasalida[3], reservashechas[3]
	
	Para i=1 Hasta 3 Con Paso 1 Hacer
		estadohabitacion[i]="Disponible"
	FinPara
	
	i=1
	j=1
	
	//Menu de Opciones para seleccionar una operacion de la reserva
	Repetir
		Escribir "BIENVENIDO A LA RESERVA DE HOTEL"
		Escribir "1. Realizar una nueva reserva"
		Escribir "2. Consultar disponibilidad de la Habitacion"
		Escribir "3. Cancelar reserva"
		Escribir "4. Mostrar reservas activas"
		Escribir "5. Salir"
		
		Escribir "Seleccione una Opcion del Menu"
		Leer opcionmenu
		
		Segun opcionmenu Hacer
			//Al seleccionar la Opcion N°1 el cliente indica: su Nombre, su RUT y el Tipo de Habitacion a reservar junto al N°
			Caso 1:
				Escribir "Indique su Nombre"
				Leer cliente
				Escribir "Indique su RUT"
				Leer rutcliente
				Escribir "¿Que tipo de habitacion desea reservar?"
				Leer tipohabitacion[i]
				
				Segun tipohabitacion[i] Hacer
					Caso "Individual":
						preciodia[i]=200
						precionoche[i]=300
						Escribir "La habitacion Individual tiene un valor de reserva de $", preciodia[i], " durante el dia y el precio durante la noche es $", precionoche[i]
					Caso "Doble":
						preciodia[i]=500
						precionoche[i]=700
						Escribir "La habitacion Doble tiene un valor de reserva de $", preciodia[i], " durante el dia y el precio durante la noche es $", precionoche[i]
					Caso "Premium":
						preciodia[i]=1000
						precionoche[i]=1200
						Escribir "La habitacion Premium tiene un valor de reserva de $", preciodia[i], " durante el dia y el precio durante la noche es $", precionoche[i]
					De Otro Modo:
						Escribir "Este tipo de Habitacion no existe en el Hotel"
				FinSegun
				
				Escribir "¿Que numero de habitacion desea reservar?"
				Leer numhabitacion[i]
				
				Si numhabitacion[i]>=101 Y numhabitacion[i]<=103 Entonces
					Si estadohabitacion[numhabitacion[i]-100]="Disponible" Entonces
						estadohabitacion[numhabitacion[i]-100]="Ocupado"
						preciototal=preciodia[i]
						
						habitacionasignada=tipohabitacion[i]
						
						Escribir "Indique una fecha de entrada"
						Leer fechaentrada[i]
						Escribir "Indique una fecha de salida"
						Leer fechasalida[i]
						
						//Se muestran todos los datos recopilados al realizar la reserva
						Escribir "Cliente registrado: ", cliente
						Escribir "Tipo de Habitacion reservada: ", habitacionasignada
						Escribir "N° Habitacion: ", numhabitacion[i]
						Escribir "Estado de la Habitacion: ", estadohabitacion[i]
						Escribir "Fecha de Entrada y Salida de la reserva: ", fechaentrada[i]," | ", fechasalida[i]
						Escribir "Valor total de la reserva: ", preciototal
						
						Escribir "Reserva Exitosa"
						
						reservashechas[i]=1
						i=i+1
					SiNo
						Escribir "La Habitacion ", numhabitacion[i], " no esta disponible"
					FinSi
				SiNo
					Escribir "N° de Habitacion invalido"
				FinSi
				
			//Al seleccionar la Opcion N°2 el cliente consulta si alguna habitacion esta disponible mediante el N° de Habitacion
			Caso 2:
				Escribir "¿Que N° de Habitacion desea saber si esta disponible? 101 | 102 | 103"
				Leer habitaciondisponible
				
				Si habitaciondisponible>=101 Y habitaciondisponible<=103 Entonces
					Si estadohabitacion[habitaciondisponible-100]="Disponible" Entonces
						Escribir "La habitacion ", numhabitacion[i], " si esta disponible"
					SiNo
						Escribir "La habitacion ", numhabitacion[i], " no esta disponible"
					FinSi
				SiNo
					Escribir "N° de habitacion invalido"
				FinSi
				
			//Al seleccionar la Opcion N°3 el cliente indica que reserva va a cancelar segun el N° de habitacion por el cual hizo la reserva
			Caso 3:
				Escribir "¿Que N° de habitacion desea cancelar?"
				Leer habitaciondisponible
				
				Si habitaciondisponible>=101 Y habitaciondisponible<=103 Entonces
					estadohabitacion[habitaciondisponible-100]="Disponible"
					Escribir "Reserva cancelada"
				SiNo
					Escribir "El N° de habitacion es invalido"
				FinSi
				
			//Al seleccionar la Opcion N°4 se muestran todas las reservas realizadas
			Caso 4:
				Si i=1 Entonces
					Escribir "No hay reservas registradas"
				SiNo
					Para j=1 Hasta i-1 Con Paso 1 Hacer
						Si reservashechas[j]=1 Entonces
							Escribir "Habitacion: ", numhabitacion[j], " | ", "Tipo de Habitacion: ", tipohabitacion[j], " | ", "Cliente: ", cliente
						FinSi
					FinPara
				FinSi
				
			//Al seleccionar la Opcion N°5 el cliente abandona el programa de reserva de un Hotel
			Caso 5:
				Escribir "Saliendo de la Reserva de Hoteles"
		FinSegun
	Hasta Que (opcionmenu=5)
FinAlgoritmo