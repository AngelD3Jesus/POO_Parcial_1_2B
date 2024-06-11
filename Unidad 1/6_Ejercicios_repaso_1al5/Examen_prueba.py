totCal = 0
totAl = 0

while True:
    nomAl = input("Ingresa el nombre del alumno: ")
    nomCarr = input("Ingresa el nombre de la carrera: ")
    calif1 = int(input("Ingresa la primera calificacion: "))
    calif2 = int(input("Ingresa la segunda calificacion: "))
    calif3 = int(input("Ingresa la tercera calificacion: "))
    proy = int(input("Ingrese la calificacion del proyecto:  "))

    promPar = (calif1 + calif2 + calif3) / 3
    promPar2 = promPar / 2 
    proyeccion = proy / 2

    caliFin = promPar2 + proyeccion
    
    print(f"El promedio de los parciales es de {promPar}")
    print(f"La calificacion final es de {caliFin}")
    
    if caliFin < 80:
        print("El alumno necesita tomar un examen extraordinario.")
    
    totCal += caliFin
    totAl += 1
    
    respuesta = input("¿Deseas otra captura? (s/n): ")
    if respuesta.lower() != "s":

        promTot = totCal / totAl
        print(f"El promedio total de los alumnos es: {promTot}")
        print("¡Programa terminado!")
        break
