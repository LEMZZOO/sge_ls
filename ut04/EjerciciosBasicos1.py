while True:  
    numero = input("Introduce un número: ") 
    if numero.isdigit():  
        numero = int(numero)  # Cast de numero a entero
        print(f"{numero}, es un número válido")
        break  # Sale del bucle si es válido
    else:
        print("No es un número válido. Inténtalo de nuevo.")
