a=0
r=0
for cont in range (1,16):
    n1 = int(input('Ingresa el primer número: '))
    if n1 >= 80:
        a = a + 1
    else:
        r = r + 1

print(f"Alumnos aprobados : {a} ")
print(f"Alumnos reprobados: {r}")
