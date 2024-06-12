def solicitarDatos():
    print("\n")
    n1 = int(input("Número #1: "))
    n2 = int(input("Número #2: "))
    ope = input("Operación: ").upper()
    return n1, n2, ope

def getCalculadora(num1, num2, operacion):
    resultado = None
    if operacion in ["1", "+", "SUMA"]:
        resultado = f"{num1} + {num2} = {num1 + num2}"
    elif operacion in ["2", "-", "RESTA"]:
        resultado = f"{num1} - {num2} = {num1 - num2}"
    elif operacion in ["3", "*", "MULTIPLICACION"]:
        resultado = f"{num1} * {num2} = {num1 * num2}"
    elif operacion in ["4", "/", "DIVISION"]:
        resultado = f"{num1} / {num2} = {num1 / num2}"
    elif operacion in ["5", "**", "POTENCIA"]:
        resultado = f"{num1} ** {num2} = {num1 ** num2}"
    elif operacion in ["6", "RAIZ", "RAIZ CUADRADA"]:
        resultado = f"Raíz cuadrada de {num1} = {num1 ** 0.5} "
    else:
        resultado = "Operación no válida."
    return resultado

def esperaTecla():
    input("Presiona ENTER para continuar...")

while True:
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicación \n 4.- División \n 5.- Potencia \n 6.- Raíz Cuadrada \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()
    if opcion == "7":
        break