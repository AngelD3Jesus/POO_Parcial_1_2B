#·de acuerdo a los valores numericos establecidos 
#sintaxis
#for variable in elemento_iterable(Lista, rango, etc):

#	bloque de instucciones

#ejemplo 1 crear un programa que imprimia 5 veces el caracter @

#contador = 1
for contador in range(1,6):
	print("@")

#ejemplo 2 crear un programa que imprima los numeros del 1 al 5, los sume y al final imprima la suma

suma = 0
for numero in range (1,6):
	print(numero)
	suma += numero
print (f" La suma es: {suma}")	

#Ejemplo 3 Crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente

numero=int(input("Ingresa un numero: "))

multi=0
for i in range(1,11):
  multi=i*numero
  print(f"{numero} X {i} = {multi}")