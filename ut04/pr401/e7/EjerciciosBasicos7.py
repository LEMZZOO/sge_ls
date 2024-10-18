from random import *
numeroAAdivinar = randint(0, 100)
numeroUsuario = (int(input("Adivina el número: ")))
while (numeroUsuario != numeroAAdivinar):
    if numeroAAdivinar < numeroUsuario: numeroUsuario = (int(input("El numero es mas bajo ")))
    if numeroAAdivinar > numeroUsuario: numeroUsuario = (int(input("El numero es mas alto ")))

print("¡Felicidades, lo has logrado!")