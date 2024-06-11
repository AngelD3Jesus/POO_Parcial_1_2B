calculos_imc = 0

while True:
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))

    imc = peso / (altura * altura)

    if imc < 18.5:
        composicion = "Peso inferior al normal"
    elif 18.5 <= imc <= 24.9:
        composicion = "Normal"
    elif 25.0 <= imc <= 29.9:
        composicion = "Peso superior al normal"
    else:
        composicion = "Obesidad"

    pregunta = input("¿Quiere calcular otro IMC? (si/no): ")

    if pregunta == "si":
        print("Tu IMC es:", imc)
        print("Composición corporal:", composicion)
        calculos_imc += 1
    else:
        print("Tu IMC es:", imc)
        print("Composición corporal:", composicion)
        print("Programa finalizado")
        break

print("Se realizaron", calculos_imc, "cálculos de IMC.")

    