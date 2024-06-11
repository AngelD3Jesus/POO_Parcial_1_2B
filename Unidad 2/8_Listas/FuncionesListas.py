paises=["Mexico","USA","Brasil","Corea"]
numeros=[23,34,12.57,0.100]
texto=["hola",True,23,3.141516] #no se pueden combinar tipos de datos

#Oredenar una lista
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos
print(texto)
texto.insert(len(texto),"True")
print(texto)
texto.insert(len(texto),True)#insertar un valor pero al final de la lista 
print(texto)
texto.append(False)
print(texto)

#eliminar elementos
print(numeros)
numeros.remove(23)
print(numeros)
numeros.pop(0)#si  tengo valros numeros iguales, se encarga de eliminar solo el de la casilla

#dar la vuelta a una lista 

print(numeros)
numeros.reverse()
print(numeros)

#buscar los datos de una lista 

respuesta="Brasil" in paises
print(respuesta)

#Cuantas veces aparece un valor en una lista

print(numeros)
numeros.append(23)
cuantos=numeros.count(23)
print(f"el numero 2 se encontro {cuantos}")

#Unir listas
print(paises)
paises.extend(numeros)
print(paises)

