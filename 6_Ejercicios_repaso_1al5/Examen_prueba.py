total_calificaciones = 0
total_alumnos = 0

while True:
    nomAl = input("Ingresa el nombre del alumno: ")
    nomCarr = input("Ingresa el nombre de la carrera: ")
    calif1 = int(input("Ingresa la primera calificacion: "))
    calif2 = int(input("Ingresa la segunda calificacion: "))
    calif3 = int(input("Ingresa la tercera calificacion: "))
    proy = int(input("Ingrese la calificacion del proyecto: "))

    promedio_parciales = (calif1 + calif2 + calif3) / 3
    promedio_parciales2 = promedio_parciales / 2 
    proyeccion_proyecto = proy / 2

    calificacion_final = promedio_parciales2 + proyeccion_proyecto
    
    print(f"El promedio de los parciales es de {promedio_parciales}")
    print(f"La calificacion final es de {calificacion_final}")
    
    if calificacion_final < 80:
        print("El alumno necesita tomar un examen extraordinario.")
    
    total_calificaciones += calificacion_final
    total_alumnos += 1
    
    respuesta = input("¿Deseas otra captura? (s/n): ")
    if respuesta.lower() != "s":

        promedio_total = total_calificaciones / total_alumnos
        print(f"El promedio total de los alumnos es: {promedio_total}")
        print("¡Programa terminado!")
        break
