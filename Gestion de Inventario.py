#El cliente indica la cantidad de productos que quiere llevar
numeroproducto=int(input("¿Cuantos productos quiere llevar?: "))

productos=[]

i=0
preciototal=0

#Segun la cantidad de productos que el cliente quiere llevar, se le consulta
#el nombre del producto, la cantidad de unidades a llevar y el precio unitario
#del producto
for i in range(numeroproducto):
    nombreproducto=input("¿Como se llama el producto que quiere llevar?: ")
    stockproducto=int(input(f"¿Cual es el stock que llevara del producto {nombreproducto}?: "))
    precioproducto=float(input(f"¿Cual es el valor del producto {nombreproducto} que llevara?: "))

    #Una vez ingresado el producto que el cliente quiere llevar se agrega al
    #listado de productos
    productos.append({
        "Nombre": nombreproducto,
        "Stock": stockproducto,
        "Precio": precioproducto
    })

#Una vez agregado los productos, se despliega un menu de opciones en el que el
#cliente podra gestionar su inventario
while True:
    print("Seleccione una opcion")
    print("1. Ver inventario")
    print("2. Modificar stock")
    print("3. Calcular el valor total")
    print("4. Salir del Programa")

    opcion=int(input("Selecciona una opcion: "))

    #Si el cliente selecciona la Opcion N°1 puede revisar los productos que tiene
    #en su inventario actualmente
    if opcion==1:
        print("Inventario actual")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto['Nombre']} - Stock: {producto['Stock']} - Precio: ${precioproducto}")
    
    #Si el cliente selecciona la Opcion N°2 podra modificar la cantidad de unidades
    #que quiere llevar de un producto
    elif opcion==2:
        print("Modificar el sotck")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto['Nombre']} - Stock: {producto['Stock']} - Precio: ${producto['Precio']}")

        productoindex=int(input("Indique el N° del producto que va a modificar: "))-1

        if 0<=productoindex<len(productos):
            cantidadmodificar=int(input("Ingrese la cantidad de productos que desea llevar: "))
            productos[productoindex]['Stock']+=cantidadmodificar
            print(f"El nuevo stock {productos[productoindex]['Nombre']}: {productos[productoindex]['Stock']}")
        else:
            print("La cantidad es invalida")
    
    #Si el cliente selecciona la Opcion N°3 revisa el monto total a pagar de todos
    #los productos comprados
    elif opcion==3:
        print("Calcule el valor total")
        preciototal=preciototal+(stockproducto*precioproducto)
        print(f"El precio total de todos los productos es de: {preciototal}")
    
    #Si el cliente selecciona la Opcion N°4 sale de su inventario
    elif opcion==4:
        print("Salir del programa")
        break
    
    else:
        print("Opcion seleccionada invalida")