cadena = input("Introduce la cadena: ")
print(cadena.swapcase())

    
#otra forma de hacerlo menos eficiente:
cadenaNueva = ""
def isCadena(cadena):
    for i in cadena:
        if (i.islower()):
            cadenaNueva += i.upper()
        elif (i.isupper()):
            cadenaNueva += i.lower()
print(cadenaNueva)