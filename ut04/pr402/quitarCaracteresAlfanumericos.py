cadena = input("introduce una cadena: ")
cadenaNueva = ""
for i in cadena:
    if(i.isalnum()): cadenaNueva += i
print(f"La cadena sin numeros alfanumericos es {cadenaNueva}")