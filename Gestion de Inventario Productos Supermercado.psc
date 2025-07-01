Algoritmo GestordeInventario
	Definir NumeroProducto, i, SeleccionOpcion, CantidadModificar, StockProducto Como Entero
	Definir NombreProducto Como Caracter
	Definir PrecioProducto, PrecioTotal Como Real
	
	//Consultamos al cliente cuantos productos queremos llevar
	Escribir "¿Cuantos productos desea llevar?"
	Leer NumeroProducto
	
	//Segun la cantidad de productos que el cliente quiere llevar se le consulta el
	//nombre del producto, la cantidad de unidades a llevar de ese producto y su valor
	Para i<-1 Hasta NumeroProducto Hacer
		Escribir "¿Como se llama el producto que desea llevar y cuanto stock necesita"
		Leer NombreProducto
		Leer StockProducto
		Escribir "Indique el valor de ese producto"
		Leer PrecioProducto
	FinPara
	
	Escribir "Seleccione una opcion"
	
	//Se despliega un menu de opciones para que el cliente realice una operacion
	Repetir
		Escribir "1. Ver inventario"
		Escribir "2. Modifica Stock"
		Escribir "3. Calcula el valor total"
		Escribir "4. Salir"
		
		Escribir "Seleccione una opcion"
		Leer SeleccionOpcion
		
		Segun SeleccionOpcion Hacer
			//Si el cliente selecciona la Opcion N°1 este podra revisar los productos
			//que lleva, la cantidad de unidades x producto y el precio unitario
			Caso 1:
				Escribir "Inventario actual"
				Para i<-1 Hasta NumeroProducto Hacer
					Escribir i, ". ", NombreProducto, " - Stock: ", StockProducto, " - Precio: $", PrecioProducto
				FinPara
				
			//Si el cliente selecciona la Opcion N°2 este podra modificar la cantidad
			//de unidades que va a llevar de un producto
			Caso 2:
				Escribir "Modificar Stock"
				Para i<-1 Hasta NumeroProducto Hacer
					Escribir i, ". ", NombreProducto, " - Stock: ", StockProducto
				FinPara
				
				Leer i
				Si i>=1 Y i<=NumeroProducto Entonces
					Escribir "Ingrese la cantidad de productos que va a llevar (Si es positivo utiliza + y si es negativo utiliza -: )"
					Leer CantidadModificar
					StockProducto=StockProducto+CantidadModificar
					Escribir "El nuevo stock de productos a llevar es de: ", StockProducto
				SiNo
					Escribir "Cantidad invalida"
				FinSi
				
			//Si el cliente selecciona la Opcion N°3 este calculara el valor total de
			//todos los productos que lleva
			Caso 3:
				Escribir "Calcula el valor total"
				PrecioTotal=0
				Para i<-1 Hasta NumeroProducto Hacer
					Escribir "Calcule el valor total de todos los productos que va a llevar"
					PrecioTotal=PrecioTotal+(StockProducto*PrecioProducto)
					Escribir "El valor total de todos los productos ha llevar es de: ", PrecioTotal
				FinPara
				
			//Si el cliente selecciona la Opcion N°4 se finaliza la interaccion con el programa
			Caso 4:
				Escribir "Saliendo del programa"
				
			De Otro Modo:
				Escribir "La opcion seleccionada no es valida"
		FinSegun
		
	Hasta Que SeleccionOpcion=4
FinAlgoritmo