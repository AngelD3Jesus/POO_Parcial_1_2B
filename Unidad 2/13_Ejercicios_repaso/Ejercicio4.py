#4.- 

# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
# y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista = [1, 2, 3]
cadena = "Que onda"
entero = 42
logico = True

def Imprimir(Var):
    tipo = type(Var).__name__ 
    print(f"La variable es de tipo {tipo}.")

Imprimir(lista)
Imprimir(cadena)
Imprimir(entero)
Imprimir(logico)