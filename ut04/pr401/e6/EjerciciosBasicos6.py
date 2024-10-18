cantidad = (int(input("Introduce la cantidad: ")))
unidadActual = input("Introduce la unidad Actual: ")
unidadDestino = input("Introduce la unidad Destino: ")
if unidadActual == "mm":
    cantidadMetros = cantidad / 1000
elif unidadActual == "cm":
    cantidadMetros = cantidad / 100
elif unidadActual == "m":
    cantidadMetros = cantidad
elif unidadActual == "km":
    cantidadMetros = cantidad * 1000
else:
    print("Unidad de origen no válida.")
    
if unidadDestino == "mm":
    resultado = cantidadMetros * 1000
elif unidadDestino == "cm":
    resultado = cantidadMetros * 100
elif unidadDestino == "m":
    resultado = cantidadMetros
elif unidadDestino == "km":
    resultado = cantidadMetros / 1000
else :
    print("Unidad destino no valida")

print(f"{cantidad}{unidadActual} es igual a {resultado}{unidadDestino}")
