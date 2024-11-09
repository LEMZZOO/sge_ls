def frecuencia_caracteres(cadena):
    frecuencias = {}
    for i in cadena:
        frecuencias[i] = frecuencias.get(i, 0) + 1
    print(frecuencias)
frecuencia_caracteres(input("Introduce la cadena: "))
