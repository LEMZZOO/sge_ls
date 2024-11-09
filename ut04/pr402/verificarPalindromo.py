def esPalindromo(cadena):
    cadenaInversa = cadena[::-1]
    
    if (cadenaInversa == cadena):
        print("Es palindromo!")
    else:
        print("No es palindromo!")
esPalindromo(input("Introduce una cadena: "))