#3.- 

#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
# palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
# el contenido de la lista en mayusculas


lista = []

# la lista esta vacia 
if not lista:
    print("La lista está vacía.")

    # 
    while True:
        palabra = input("Ingrese una palabra o frase (o presione Enter para salir): ")
        if palabra == "":
            break
        lista.append(palabra)

    # Imprimir el contenido de la lista en mayúsculas
    print("Contenido de la lista en mayúsculas:")
    for elemento in lista:
        print(elemento.upper(),end=" ")
else:
    # Imprimir mensaje si la lista no está vacía
    print("La lista no está vacía.")