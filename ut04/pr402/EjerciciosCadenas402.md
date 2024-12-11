```python
1. Contar vocales y consonantes
Escribe una función que reciba una cadena y cuente cuántas vocales y consonantes contiene.
```


```python
cadena = input("Introduce una cadena: ")
vocales = "aeiou"
consonantes = "bcdfghjklmnñpqrstvxzwy"
vocal = 0
consonante = 0
for i in cadena.lower():
    if (i in vocales):
        vocal = vocal +1
    else:
        consonante = consonante + 1
print(f"la cadena {cadena} tiene {int(vocal)} vocales y {int(consonante)} consonantes")
```


```python
2. Invertir una cadena
Crea un programa que invierta una cadena.
```


```python
cadena = input("Introduce una cadena: ")
print(cadena[::-1]))
```


```python
3. Verificar palíndromo
Escribe un programa que verifique si una cadena es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).
```


```python
def esPalindromo(cadena):
    cadenaInversa = cadena[::-1]
    
    if (cadenaInversa == cadena):
        print("Es palindromo!")
    else:
        print("No es palindromo!")
esPalindromo(input("Introduce una cadena: "))
```


```python
4. Contar palabras
Crea una función que cuente cuántas palabras hay en una cadena, suponiendo que las palabras están separadas por espacios.
```


```python
cadena = input("Introduce la cadena: ")
print(f"la cadena {cadena} tiene {len(cadena.split())} palabras")
```


```python
5. Eliminar caracteres repetidos
Escribe una función que elimine los caracteres duplicados en una cadena, manteniendo solo la primera aparición de cada uno.
```


```python
def eliminarRepetida(cadena):
    cadenaNueva = ""
    for i in cadena:
        if (i not in cadenaNueva): cadenaNueva += i
    return cadenaNueva
print(eliminarRepetida(input("Introduce la cadena: ")))
```


```python
6. Mayúsculas y minúsculas
Escribe un programa que convierta las letras minúsculas de una cadena en mayúsculas y viceversa.
```


```python
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
```


```python
7. Invertir palabras de una cadena
Escribe un programa que invierta el orden de las palabras de una cadena, manteniendo las palabras originales intactas.
```


```python
cadena = input("Introduce una cadena: ")
#separo la cadena por espacios con split y le doy la vuelva
print(" ".join(cadena.split(" ")[::-1]))
```


```python
8. Anagrama
Crea un programa que verifique si dos cadenas son anagramas. Se considera que dos palabras son anagramas si tienen las mismas letras en diferente orden, por ejemplo, lácteo y coleta.
```


```python
def isAnagrama(cadena1, cadena2):
    if(sorted(cadena1.lower()) == sorted(cadena2.lower())): print("Es anagrama")
    
    else: print("No es anagrama")
isAnagrama(input("Introduce la primera cadena: "), input("Introduce la segunda cadena: "))
```


```python
9. Frecuencia de caracteres
Crea una función que reciba una cadena y devuelva un diccionario con la frecuencia de cada carácter.
```


```python
def frecuencia_caracteres(cadena):
    frecuencias = {}
    for i in cadena:
        frecuencias[i] = frecuencias.get(i, 0) + 1
    print(frecuencias)
frecuencia_caracteres(input("Introduce la cadena: "))
```


```python
10. Quitar caracteres alfanuméricos
Escribe un programa que elimine todos los caracteres no alfanuméricos (como signos de puntuación) de una cadena.
```


```python
cadena = input("introduce una cadena: ")
cadenaNueva = ""
for i in cadena:
    if(i.isalnum()): cadenaNueva += i
print(f"La cadena sin numeros alfanumericos es {cadenaNueva}")
```


```python
11. Transformar a camelCase
Escribe un programa que transforme una cadena de palabras separadas por espacios o guiones en formato camelCase (la primera letra de cada palabra, excepto la primera, debe ser mayúscula y no debe haber espacios ni guiones).
```


```python
def transformarACamelCase(cadena):
    palabras = cadena.lower().split(" ")
    resultado = palabras[0]
    for palabra in palabras[1:]:
        resultado += palabra.title()
    print(resultado)
transformarACamelCase(input("Introduce la cadena: "))
```


```python
12. Codificación RLE (Run-Length Enconding)
Escribe una función que implemente la codificación por longitud de ejecución (RLE), que consiste en comprimir una cadena representando las secuencias consecutivas de caracteres iguales con el carácter seguido de la cantidad de repeticiones.

Por ejemplo, la cadena aaron la reemplazaría por a2r1o1n1. Por simplicidad, puedes asumir que un carácter no se va a repetir más de 9 veces consecutivas.
```


```python

```


```python
13. Decodificar RLE
Crea una función que decodifique una cadena que ha sido comprimida usando el método RLE.
```


```python

```


```python
14. Formateo de cadenas con plantillas
Escribe un programa que tome una plantilla de cadena y un diccionario, y reemplace los marcadores en la plantilla por los valores correspondientes en el diccionario.

Ejemplo: la cadena "Hola, {nombre}" con el diccionario {"nombre": "Victor"} debería devolver "Hola, Victor"
```


```python

```


```python
15. Comparar cadenas por valor ASCII
Escribe una función que compare dos cadenas sumando el valor ASCII de cada carácter y devuelva cuál tiene un mayor valor total. Para este ejercicio ten en cuenta que la función integrada ord() devuelve el valor ASCII de un carácter
```


```python
def getValorAscii(cadena):
    return (sum([ord(i) for i in cadena]))
def compararValores(cadena1, cadena2):
    if (getValorAscii(cadena1) > getValorAscii(cadena2)): print (f"{cadena1} es mayor que {cadena2}")
    if (getValorAscii(cadena2) > getValorAscii(cadena1)): print (f"{cadena2} es mayor que {cadena1}")
compararValores(input("Introduce la primera cadena: "), input("Introduce la segunda cadena: "))
```


```python
16. Contar la longitud de palabra más larga
Escribe un programa que reciba una cadena y devuelva la longitud de la palabra más larga
```


```python
palabraMasLarga = 0
def palabraMasLarga(cadena):
    
    
```


```python
17. Formatear número con separador de miles
Escribe una función que tome un número de forma de cadena y le agregue separadores de miles.

Ejemplo: "123456756" debería convertirse en "123.456.789".
```


```python

```


```python
18. Rotar caracteres de una cadena
Escribe una función que rote una cadena hacia la izquierda un número dado de veces.

Ejemplo: "abcdef" rotado 2 veces convierte la cadena en "cdefab".
```


```python

```
