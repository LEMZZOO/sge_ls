while True:
        n = int(input("Introduce un número impar: "))
        if n % 2 != 0: break
for i in range(1, n + 1, 2):
    espacio = ((n - i) / 2)
    print(" " * int(espacio) + "*" * i)



# base = int(print("Introduce un numero impar: "))
# while (base % 2 == 0):
#     print("el numero no es impar")
#     base = int(print("Introduce un numero impar: "))
# for i in range(1, base + 1, 2):
#     espacios = (base - i) / 2
#     print(" " * int(espacios) + "*" * i)