numeroMax, numeroMin = 0, 0
for i in range(1, 6):
    numero = int(input(f"Introduce el {i} numero: "))
    if i == 1: numeroMax = numero
    if i == 1: numeroMin = numero
    if (numero > numeroMax): numeroMax = numero
    if (numero < numeroMin): numeroMin = numero
print(f"El numero mayor es {numeroMax} y el numero menor es {numeroMin}")
