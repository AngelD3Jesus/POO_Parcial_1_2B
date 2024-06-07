"""

List (Array)
son colecciones o conjunto de datos/valores bajo
un mismo nombre, para acceder a los valores se 
hace con un indice numerico

Nota: sus valores si son modificables 

La lista es una coleccion oredenada y modificable. Permite miembreos duplicados.

"""

#Ejemplo 1 crea una lista con datos numericos e imprimir el contenido 

lista=[23,34]
print(lista)

#recorrer la lista con el for

for i in lista:
    print(i)

#recorrer la lista con con el while
i=0
while i<=len(lista)-1: 
    print(lista[i])
    i+=1

#Ejemplo2 crear una lista de 4 palabras, solicitar una palabra y buscar  la 
#coincidencia en la lista e indicar si la encontro o no y en que posicion 

palabras=["hola","2024","bye","UTD"]
print(palabras)
palabra_buscar=input("ingresa la palabra a buscar: ")

encontre = True
for i in palabras:
    if palabra_buscar==i:
        print(f"Encontre la palabra {i}, en la posicion: {palabras.index(i)}")
        encontre=False

if encontre:
    print(f"no encontre la palabra")




#ejemplo 3 agregar y eliminar elementos de una lista 
os.system("clear")

numeros=[23,34]

print(numeros)

#agregar un elemento
numeros.append(100)
print(numeros)