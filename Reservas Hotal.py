estadohabitacion=["Disponible"]*3
reservas=[]

#Creamos un menu con diferentes opciones para que el cliente realice
#una operacion dentro del hotel
while(True):
    print("BIENVENIDO A LA RESERVA DE HOTEL HIERBAS BUENAS")
    print("1. Realizar una nueva reserva")
    print("2. Consultar disponibilidad de la Habitacion")
    print("3. Cancelar Reserva")
    print("4. Mostrar reservas activas")
    print("5. Salir del Hotel")

    try:
        opcionmenu=int(input("Seleccione una opcion del menu: "))
    except ValueError:
        print("Seleccione una de las Opciones que es muestra en el menu")

    match opcionmenu:
        #Al seleccionar la Opcion N°1 el cliente realiza una reserva indicando
        #sus datos que son: Nombre, RUT, Tipo de Habitacion e indica que numero
        #quiere reservar
        case 1:
            if len(reservas) < 3:
                cliente = {
                    "Nombre Cliente": input("Indique su Nombre: "),
                    "RUT Cliente": int(input("Indique su RUT: ")),
                    "Tipo de Habitacion": input("¿Qué tipo de habitación va a reservar? (Individual | Doble | Premium): ")
                }

                tipo = cliente["Tipo de Habitacion"]

                if tipo == "Individual":
                    preciodia = 200
                    precionoche = 300
                    print(f"La habitación Individual tiene un valor de reserva de ${preciodia} durante el día y ${precionoche} durante la noche.")
                elif tipo == "Doble":
                    preciodia = 500
                    precionoche = 700
                    print(f"La habitación Doble tiene un valor de reserva de ${preciodia} durante el día y ${precionoche} durante la noche.")
                elif tipo == "Premium":
                    preciodia = 1000
                    precionoche = 1200
                    print(f"La habitación Premium tiene un valor de reserva de ${preciodia} durante el día y ${precionoche} durante la noche.")
                else:
                    print("El tipo de habitación que indicó no está disponible.")

                numhabitacion = int(input("Indique el N° de Habitación que desea reservar (101 | 102 | 103): "))

                if 101 <= numhabitacion <= 103:
                    index = numhabitacion - 101
                    if estadohabitacion[index] == "Disponible":
                        estadohabitacion[index] = "Ocupado"
                        preciototal = preciodia
                        habitacionasignada = tipo

                        fechaentrada = input("Indique la fecha de entrada (dd/mm/aaaa): ")
                        fechasalida = input("Indique la fecha de salida (dd/mm/aaaa): ")

                        print(f"Cliente registrado: {cliente['Nombre Cliente']}")
                        print(f"Tipo de Habitación reservada: {habitacionasignada}")
                        print(f"N° Habitación: {numhabitacion}")
                        print(f"Estado de Habitación: {estadohabitacion[index]}")
                        print(f"Fecha Entrada y Salida: {fechaentrada} y {fechasalida}")
                        print(f"Valor total de la Reserva: ${preciototal}")
                        print("Reserva Exitosa")

                        # Guardamos la reserva
                        cliente["N° Habitacion"] = numhabitacion
                        cliente["Fecha Entrada"] = fechaentrada
                        cliente["Fecha Salida"] = fechasalida
                        cliente["Precio Total"] = preciototal
                        reservas.append(cliente)
                    else:
                        print(f"La habitación {numhabitacion} no está disponible.")
                else:
                    print("Número de habitación inválido.")
            else:
                print("Limite de reservas superado")

        #Al seleccionar la Opcion N°2 el consulta si una habitacion esta disponible
        #segun su numero
        case 2:
            habitaciondisponible=int(input("¿Que N° de Habitacion quiere saber si esta disponible?: "))

            if 101 <= habitaciondisponible <= 103:
                index=habitaciondisponible-101
                if estadohabitacion[index]=="Disponible":
                    print(f"La Habitacion {habitaciondisponible} si esta disponible")
                else:
                    print(f"La Habitacion {habitaciondisponible} no esta disponible")
            else:
                print("N° de Habitacion invalido")

        #Al seleccionar la Opcion N°3 el cliente puede cancelar una reserva indicando
        #el N° habitacion de la habitacion que reservo inicialmente
        case 3:
            habitacioncancelada=int(input("¿Que N° de Habitacion quiere cancelar?: "))

            if 101 <= habitacioncancelada <= 103:
                index=habitacioncancelada-101
                estadohabitacion[index]="Disponible"
                reservas=[r for r in reservas if r["N° Habitacion"]!=habitacioncancelada]
                print("Reserva cancelada")
            else:
                print("El N° de Habitacion es invalido")

        #Al seleccionar la Opcion N°4 se muestran todas las reservas realizadas
        case 4:
            if len(reservas)==0:
                print("No hay reservas hechas")
            else:
                print("Reservas Activas")
                for reserva in reservas:
                    print(f"Habitacion: {reserva['N° Habitacion']}")
                    print(f"Tipo de Habitacion: {reserva['Tipo de Habitacion']}")
                    print(f"Cliente: {reserva['Nombre Cliente']}")

        #Al seleccionar la Opcion N°5 el cliente abandona el Hotel
        case 5:
            print("Saliendo de la Reserva de Hoteles")
            break