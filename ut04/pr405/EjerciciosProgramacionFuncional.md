1.- Filtrado de una lista de números
Usa filter para obtener solo los números pares de una lista de enteros


```python
# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Resultado esperado: [2, 4, 6, 8, 10]

def es_par(x):
    return x % 2 == 0

# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
           
pares = list(filter(es_par, numeros))
print(pares)
```

    [2, 4, 6, 8, 10]


2.- Mapeo de temperaturas
Dada una lista de temperaturas en Celsius, usa map para convertirlas a Fahrenheit.


```python
# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(x):
    return x * 9/5 + 32

# Ejemplo de lista de entrada
celsius = [0, 20, 37, 100]

fahrenheit = list(map(celsius_a_fahrenheit, celsius))
print(fahrenheit) 
```

    [32.0, 68.0, 98.6, 212.0]



```python
3.- Suma acumulativa
Utiliza reduce para obtener la suma acumulativa de una lista de números.
```


```python
from functools import reduce

# Función para sumar dos números
def sumar(x, y):
    return x + y

# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5]

suma = reduce(sumar, numeros)
print(suma)
```

    15



```python
4.- Palabras con cierta longitud
Dada una lista de palabras, usa filter para encontrar las que tienen más de cinco letras y luego map para convertirlas en mayúsculas.
```


```python
# Función para verificar longitud de palabra
def mas_de_cinco_letras(palabra):
    return len(palabra) > 5

# Función para convertir a mayúsculas
def convertir_a_mayusculas(palabra):
    return palabra.upper()

# Ejemplo de lista de entrada
palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

#convierto en majusculas las que tengan mas de 5 letras
palabras_filtradas = list(map(convertir_a_mayusculas, filter(mas_de_cinco_letras, palabras)))
print(palabras_filtradas)
```

    ['ELEFANTE', 'JIRAFA']



```python
5.- Multiplicación de pares
Dada una lista de números, utiliza filter, map y reduce para obtener el producto de los números pares.
```


```python
from functools import reduce

# Función para verificar si un número es par
def es_par(x):
    return x % 2 == 0

# Función para multiplicar dos números
def multiplicar(x, y):
    return x * y

# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5, 6]

#multiplico los que sean pares uno tras otro con reduce
producto = reduce(multiplicar, filter(es_par, numeros))
print(producto)  # Resultado esperado: 48 (producto de 2, 4 y 6)
```

    48



```python
6.- Combinar operaciones en listas anidadas
Dada una lista de listas de enteros, usa map, filter, y reduce para obtener la suma de todos los números positivos.
```


```python
# Función para verificar si un número es positivo
def es_positivo(x):
    return x > 0

# Ejemplo de lista de entrada
numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]
# Solución usando una comprensión para filtrar positivos
positivos = sum([num for sublist in numeros for num in sublist if es_positivo(num)])
print(positivos)  # Resultado esperado: 30 (suma de 2, 7, 10, 3, y 8)
```

    30



```python
7.- Frecuencia de palabras
Dado un texto, crea una función que use map y reduce para obtener la frecuencia de cada palabra. Ignora las mayúsculas y minúsculas y supón que no hay símbolos de puntuación.
```


```python
from functools import reduce

# Función para actualizar el diccionario de frecuencia
def actualizar_frecuencia(diccionario, palabra):
    diccionario[palabra] = diccionario.get(palabra, 0) + 1
    return diccionario

# Ejemplo de texto de entrada
texto = "Hola hola mundo mundo cruel"
# Solución
palabras = texto.lower().split()
frecuencia = reduce(actualizar_frecuencia, palabras, {})
print(frecuencia)  # Resultado esperado: {'hola': 2, 'mundo': 2, 'cruel': 1}
```

    {'hola': 2, 'mundo': 2, 'cruel': 1}



```python
8.- Intersección de conjuntos
Dadas dos listas de números, usa filter para obtener una lista de los elementos que están en ambas listas (sin usar conjuntos).
```


```python
# Función para verificar si un número está en la segunda lista
def en_lista2(x):
    return x in lista2

# Ejemplo de listas de entrada
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
# Solución
interseccion = list(filter(en_lista2, lista1))
print(interseccion)  # Resultado esperado: [3, 4, 5]
```

    [3, 4, 5]



```python
9.- Agrupación de palabras por longitud
Dada una lista de palabras, crea un diccionario donde la clave es la longitud de la palabra y el valor es una lista de palabras de esa longitud. Usa map y filter.
```


```python
from functools import reduce

# Función para agrupar palabras por longitud
def agrupar_por_longitud(diccionario, palabra):
    longitud = len(palabra)
    if longitud in diccionario:
        diccionario[longitud].append(palabra)
    else:
        diccionario[longitud] = [palabra]
    return diccionario

# Ejemplo de lista de entrada
palabras = ["sol", "luna", "estrella", "cielo", "mar"]
# Solución
agrupadas = reduce(agrupar_por_longitud, palabras, {})
print(agrupadas)  # Resultado esperado: {3: ['sol', 'mar'], 4: ['luna', 'cielo'], 8: ['estrella']}
```

    {3: ['sol', 'mar'], 4: ['luna'], 8: ['estrella'], 5: ['cielo']}



```python
10.- Concatenación de listas de caracteres
Dadas dos listas de caracteres, usa reduce para concatenarlas en una sola lista sin utilizar + o métodos de concatenación.
```


```python
from functools import reduce

# Función para concatenar dos listas de caracteres usando `extend` en lugar de `+`
def concatenar_listas(lista1, lista2):
    return reduce(lambda acc, elem: acc.extend(elem) or acc, [lista1, lista2], [])

# Ejemplo de listas de caracteres
lista1 = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']

# Concatenación de listas
resultado = concatenar_listas(lista1, lista2)
print(resultado)  # Resultado esperado: ['a', 'b', 'c', 'd', 'e', 'f']

```

    ['a', 'b', 'c', 'd', 'e', 'f']



```python
11.- Calificación de alumnos
Dada una lista de tuplas con el nombre del alumno y su calificación, utiliza map y filter para obtener una lista con los nombres de los alumnos que han aprobado (nota >= 5).
```


```python
# Ejemplo de lista de entrada
alumnos = [("Ana", 4), ("Luis", 7), ("Marta", 5), ("Juan", 3), ("Elena", 8)]

# Función para verificar si el alumno ha aprobado
def ha_aprobado(alumno):
    return alumno[1] >= 5

# Función para obtener solo el nombre del alumno
def obtener_nombre(alumno):
    return alumno[0]

# Filtramos los alumnos que han aprobado y extraemos sus nombres
aprobados = list(map(obtener_nombre, filter(ha_aprobado, alumnos)))
print(aprobados)  # Resultado esperado: ['Luis', 'Marta', 'Elena']
```


