n = int(input("Introduce el primerNumero: "))
k = int(input("Introduce el segundoNumero: "))

for linea in range(1, k + 1 ):
    resultado = n * linea
    print(f"{n} * {linea} = {resultado}")
print("||Fin||")
