#2.- 
#Escribir un programa  que añada valores a una lista mientras que su longitud 
#sea menor a 120, y luego mostrar la lista: Usar un while y for


lista1 = [] #creamos la lista
contador = 0
while len(lista1) < 120: #cuenta si el tamaño de la lista es menor a 120 (len saca el tamaño de la lista)
    lista1.append(contador) #el comando append agrega los numeros al final de la lista 
    contador += 1

for lista2 in lista1:
    print(lista2)
print()
