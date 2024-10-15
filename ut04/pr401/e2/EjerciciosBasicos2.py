n = input("Introduce el primerNumero: ")
k = input("Introduce el segundoNumero: ")
n = int(n)
k = int(k)

for i in range(1, k + 1 ):
    resultado = n * i
    print(f"{n} * {i} = {resultado}")
print("||Fin||")
