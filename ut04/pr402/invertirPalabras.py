cadena = input("Introduce una cadena: ")
#separo la cadena por espacios con split y le doy la vuelva
print(" ".join(cadena.split(" ")[::-1]))