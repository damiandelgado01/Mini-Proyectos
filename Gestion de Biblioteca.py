#Indicamos que los Libros se guardaran en una Lista
librosguardados=[]
libroencontrado=False
solicitante=[]

#Se crea un Menu de Opciones
while(True):
    print("BIENVENIDO A LA BIBLIOTECA")
    print("1. Agregar un libro a la Biblioteca")
    print("2. Buscar un libro guardado en la Biblioteca")
    print("3. Mostrar todos los libros guardados en la Biblioteca")
    print("4. Prestar un Libro de la Biblioteca")
    print("5. Devolver un Libro de la Biblioteca")
    print("6. Salir de la Biblioteca")

    #El usuario selecciona una opcion del Menu para operar en la Biblioteca
    opcionmenu=int(input("Seleccione una Opcion de la Biblioteca: "))

    #Dependiendo la Opcion seleccionada por el usuario se ejecuta una operacion
    match opcionmenu:

        #Al seleccionar la Opcion N°1 el cliente agregara un nuevo libro en
        #la biblioteca en caso de que este vacia, sino simplemente indicamos
        #que la biblioteca esta llena
        case 1:
            if len(librosguardados)<5:
                libro={
                    "Nombre": input("Ingrese el Nombre del Libro: "),
                    "Autor": input("Ingrese el Autor del Libro: "),
                    "Año": input("Ingrese el Año publico del Libro: "),
                    "Estado": input("Ingrese el Estado de uso del Libro: ")
                }

                librosguardados.append(libro)
                print("Libro Guardado")
            else:
                print("Biblioteca llena")

        #Al seleccionar la Opcion N°2 el cliente buscara un libro guardado
        #en la biblioteca segun el nombre por el cual el libro fue guardado
        #inicialmente
        case 2:
            librobuscado=input("¿Que libro estas buscando?: ").lower()

            libroencontrado=False

            for libro in librosguardados:
                if libro["Nombre"].lower()==librobuscado:
                    print(f"Nombre: {libro['Nombre']}")
                    print(f"Autor: {libro['Autor']}")
                    print(f"Año: {libro['Año']}")
                    print(f"Estado: {libro['Estado']}")

                    if libro["Estado"].lower()=="Prestado":
                        print(f"El libro {libro['Nombre']} esta en uso")
                    else:
                        print(f"El libro {libro['Nombre']} esta disponible")
                        
                        libroencontrado=True
                        break

            else:
                print("El libro que buscas no esta en la Biblioteca")

        #Al seleccionar la Opcion N°3 se le muestra al cliente todos los
        #libros que han sido guardados en la Biblioteca
        case 3:
            if len(librosguardados)==0:
                print("No hay libros guardados en la Biblioteca")
            else:
                print("Si hay libros guardados en la Biblioteca")
                for i, libro in enumerate(librosguardados, 1):
                    print(f"Libros guardados en la Biblioteca: {i}")
                    print(f"Nombre del Libro: {libro['Nombre']} | Autor del Libro: {libro['Autor']} | Año de publicacion: {libro['Año']} | Estado de uso: {libro['Estado']}")

        #Al seleccionar la Opcion N°4 el cliente podra pedir un libro
        #prestado de la Bilioteca segun el nombre por el cual este se
        #agrego en la Biblioteca inicialmente
        case 4:
            librobuscado=input("¿Que libro desea llevar?: ").lower()

            libroencontrado=False

            for libro in librosguardados:
                if librobuscado==libro["Nombre"].lower():
                    libroencontrado=True

                    if libro["Estado"]=="Disponible":
                        libro["Estado"]="Prestado"

                        nombrecliente=input("Indique su Nombre: ")

                        print(f"El libro {libro["Nombre"]} ha sido prestado a {nombrecliente}")

        #Al seleccionar la Opcion N°5 el cliente podra devolver un libro
        #que pidio prestado por el nombre de dicho libro y este debe coincidir
        #con el nombre por el cual se agrego inicialmente en la Biblioteca
        case 5:
            librobuscado=input("¿Que libro vas a devolver?: ").lower()

            libroencontrado=False

            for libro in librosguardados:
                if libro["Nombre"].lower()==librobuscado:
                    if libro["Estado"]=="Prestado":
                        libroencontrado=True

                        print(f"Libro devuelto: {libro['Nombre']}")
                        print(f"Estado del Libro: {libro['Estado']}")
                        print(f"Devuelto por: {nombrecliente}")

                        libro["Estado"]="Disponible"
                        nombrecliente=" "
                    else:
                        print("El libro esta, pero ha sido prestado")
            
                        libroencontrado=True
                        break
            
            else:
                print("La biblioteca esta llena")

        #Al seleccionar la Opcion N°6 el cliente abandona la Biblioteca
        case 6:
            print("Saliendo de la Biblioteca")
            break