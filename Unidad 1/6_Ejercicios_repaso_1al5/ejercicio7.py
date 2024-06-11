n1 = int(input('Ingresa el primer número: '))
n2 = int(input('Ingresa otro número: '))

num = n1 + 1 if n1 % 2 == 0 else n1 + 2 
while num < n2:
    print(num)
    num += 2
