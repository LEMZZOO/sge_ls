from random import *
import random

opciones = ["Piedra", "Papel", "Tijeras"]
reglas = {"Piedra": ["Tijeras"], "Papel": ["Piedra"], "Tijeras": ["Papel"]}

puntosUsuario = 0
puntosPC = 0

while puntosUsuario < 5 and puntosPC < 5:
    usuario = input("Elige: Piedra, Papel, Tijeras:  ")
    pc = random.choice(opciones)
    print(f"PC elige: {pc}")
    
    if usuario == pc:
        print("Empate")
    elif pc in reglas[usuario]:
        print("Ganas esta ronda")
        puntosUsuario += 1
    else:
        print("Pierdes esta ronda")
        puntosPC += 1
    
    print(f"Usuario: {puntosUsuario} || PC: {puntosPC}")

if puntosUsuario == 5: print("Has ganado el juego!") 
else: print("Te ha ganado el PC pringado")

#21 LINEAS