def isAnagrama(cadena1, cadena2):
    if(sorted(cadena1.lower()) == sorted(cadena2.lower())): print("Es anagrama")
    else: print("No es anagrama")
isAnagrama(input("Introduce la primera cadena: "), input("Introduce la segunda cadena: "))
    
    