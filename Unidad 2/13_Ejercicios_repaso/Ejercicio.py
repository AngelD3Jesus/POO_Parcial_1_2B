#Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

# a.- Recorrer la lista y mostrarla
# b.- hacer una funcion que recorra la lista de numeros y devuelva un string
# c.- ordenarla y mostrarla
# d.- mostrar su longitud
# e.- buscar algun elemento que el usuario pida por teclado

# Definir la lista de números
lista = [2, 8, 3, 5, 9, 1, 7, 4]

# a.- Recorrer la lista y mostrarla
print("a.- Lista de números:")
for numero in lista:
    print(numero, end=" ")
print()

# b.- Función que recorre la lista y devuelve un string
def listaStr(lista):
    return ' '.join(str(numero) for numero in lista)

print("b.- Lista como string:", listaStr(lista))

# c.- Ordenar la lista y mostrarla
numeros_ordenados = sorted(lista)
print("c.- Lista ordenada:")
for numero in numeros_ordenados:
    print(numero, end=" ")
print()

# d.- Mostrar la longitud de la lista
print("d.- Longitud de la lista:", len(lista))

# e.- Buscar un elemento que el usuario pida por teclado
elemento_buscar = int(input("e.- Ingrese el número que desea buscar en la lista: "))
if elemento_buscar in lista:
    print(f"El número {elemento_buscar} está en la lista.")
else:
    print(f"El número {elemento_buscar} no está en la lista.")
