Algoritmo CalculadoraGastosSemanales
	Definir Trabajadores, HorasTrabajo, HorasExtra, SueldoTotalEmpresa Como Entero
	Definir NombreTrabajador Como Caracter
	Definir GananciasHora, Sueldo Como Real
	
	TrabajoHora=0
	HorasTrabajo=0
	HorasExtra=0
	Sueldo=0
	SueldoTotalEmpresa=0
	
	//Se consulta al empresario cuantos trabajadores tiene dentro de su
	//empresa
	Escribir "¿Cuantos trabajadores tiene en su empresa?"
	Leer Trabajadores
	
	//Segun la cantidad de trabajadores que el empresario tiene en su empresa
	//este indica el nombre de cada trabajador, las horas que trabaja y las
	//ganancias que generan por hora
	Para i<-1 Hasta Trabajadores Hacer
		Escribir "Como se llama el Empleado ", i, ":"
		Leer NombreTrabajador
		Escribir "Cuantas horas trabaja el Empleado ", NombreTrabajador, "?"
		Leer HorasTrabajo
		Escribir "Cual es el sueldo por hora del Empleado ", NombreTrabajador, "?"
		Leer GananciasHora
		
		//Segun las horas de trabajo de cada trabajador se obtienen sus
		//ganancias totales generadas
		Si HorasTrabajo<=40 Entonces
			Sueldo=(HorasTrabajo*GananciasHora)
		SiNo
			HorasExtra=HorasTrabajo-40
			Sueldo=(40*GananciasHora)+(HorasExtra*GananciasHora*1.5)
		FinSi
		
		SueldoTotalEmpresa=SueldoTotalEmpresa+Sueldo
		
		Escribir "El sueldo total del empleado", NombreTrabajador, " es de: $", Sueldo
	FinPara
	
	Escribir "El total de ingreso que genera la empresa es: ", SueldoTotalEmpresa
FinAlgoritmo