#Consultamos al Empresario cuantos trabajadores tiene en su empresa
trabajadores=int(input("¿Cuantos trabajadores tiene en su empresa?: "))

ingresototalempresa=0

#Segun la cantidad de Trabajadores, el empresario indica sus nombres, horas
#de trabajo y ganancias generadas por hora
for i in range(0, trabajadores):
    nombretrabajador=input(f"¿Cual es el nombre del trabajador {i+1}?: ")
    horastrabajo=int(input(f"¿Cuantas horas trabaja el trabajador {nombretrabajador}?: "))
    gananciashora=float(input("Indique las ganancias que el trabajador genera por hora: "))
    
    #Dependiendo las horas de trabajo y las ganancias por hora obtenidas del
    #trabajador se obtiene su sueldo
    if horastrabajo<=40:
        sueldo=horastrabajo*gananciashora
    else:
        horasextra=horastrabajo-40
        sueldo=(40*gananciashora)+(horasextra*gananciashora*1.5)
    
    ingresototalempresa+=sueldo
    
    print(f"El sueldo total del trabajador {nombretrabajador} es de ${sueldo}")

print(f"El total de ingreso que genera la empresa es: {ingresototalempresa}")