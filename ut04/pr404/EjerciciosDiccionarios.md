1.- Buscar valor en un diccionario
Crea un diccionario de frutas y precios. Permite al usuario ingresar el nombre de una fruta y muestra su precio si existe en el diccionario, o un mensaje de que no está disponible en caso contrario.


```python
frutas = {
    "manzana": 0.50,
    "banana": 0.30,
    "naranja": 0.40,
    "pera": 0.45
}

entrada = input("Ingresa el nombre de la fruta: ").lower()

if entrada in frutas:
    print(f"El precio de {entrada} es ${frutas[entrada]:0.2f}")
else:
    print("Lo siento, esa fruta no está disponible.")

```

    Lo siento, esa fruta no está disponible.


2.- Contar elementos en un diccionario
Suponiendo un diccionario con al siguiente estructura, crea un programa que calcule cuántas categorías hay, cuántos productos tiene cada categoría y cuántos productos hay en total.


```python
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

totalCategorias = len(productos)
productosPorCategoria = {categoria: len(items) for categoria, items in productos.items()}
total_productos = sum(productosPorCategoria.values())

print(f"Total de categorías: {totalCategorias}")
print("Productos por categoría:")
for categoria, cantidad in productos_por_categoria.items():
    print(f"{categoria}: {cantidad}")
print(f"Total de productos: {total_productos}")

```

    Total de categorías: 5
    Productos por categoría:
    Electrónica: 5
    Hogar: 5
    Ropa: 5
    Deportes: 5
    Juguetes: 5
    Total de productos: 25


3.- Contador de frecuencias de palabras
Escribe un programa que tome una frase y use un diccionario para contar la frecuencia de cada palabra.


```python
frase = input("Ingresa una frase: ").lower()
palabras = frase.split()

frecuenciaPalabras = {palabra: palabras.count(palabra) for palabra in set(palabras)}

print("Frecuencia de palabras:")
for palabra, frecuencia in frecuenciaPalabras.items():
    print(f"{palabra}: {frecuencia}")

```

    Frecuencia de palabras:
    hola: 3


4.- Diccionario de listas
Supón un diccionario donde cada clave es una asignatura y el valor correspondiente una lista de estudiantes matriculados, tal como se muestra en el diccionario de ejemplo. Crea un programa que tenga un menú con tres opciones:

Listar estudiantes matriculados en una asignatura
Matricular un estudiante en una asignatura
Dar de baja un estudiante de una asignatura.
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}


```python
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

def listar_estudiantes(asignatura):
    if asignatura in asignaturas:
        print(f"Estudiantes en {asignatura}: {', '.join(asignaturas[asignatura])}")
    else:
        print("La asignatura no existe.")

def matricular_estudiante(asignatura, estudiante):
    if asignatura in asignaturas:
        if estudiante not in asignaturas[asignatura]:
            asignaturas[asignatura].append(estudiante)
            print(f"{estudiante} ha sido matriculado en {asignatura}.")
        else:
            print(f"{estudiante} ya está matriculado en {asignatura}.")
    else:
        print("La asignatura no existe.")

def dar_baja_estudiante(asignatura, estudiante):
    if asignatura in asignaturas:
        if estudiante in asignaturas[asignatura]:
            asignaturas[asignatura].remove(estudiante)
            print(f"{estudiante} ha sido dado de baja de {asignatura}.")
        else:
            print(f"{estudiante} no está matriculado en {asignatura}.")
    else:
        print("La asignatura no existe.")

while True:
    print("\nMenú:")
    print("1. Listar estudiantes matriculados en una asignatura")
    print("2. Matricular un estudiante en una asignatura")
    print("3. Dar de baja un estudiante de una asignatura")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        asignatura = input("Ingresa el nombre de la asignatura: ")
        listar_estudiantes(asignatura)
    elif opcion == "2":
        asignatura = input("Ingresa el nombre de la asignatura: ")
        estudiante = input("Ingresa el nombre del estudiante: ")
        matricular_estudiante(asignatura, estudiante)
    elif opcion == "3":
        asignatura = input("Ingresa el nombre de la asignatura: ")
        estudiante = input("Ingresa el nombre del estudiante: ")
        dar_baja_estudiante(asignatura, estudiante)
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
```

    
    Menú:
    1. Listar estudiantes matriculados en una asignatura
    2. Matricular un estudiante en una asignatura
    3. Dar de baja un estudiante de una asignatura
    4. Salir
    Estudiantes en Matemáticas: Ana, Carlos, Luis, María, Jorge
    
    Menú:
    1. Listar estudiantes matriculados en una asignatura
    2. Matricular un estudiante en una asignatura
    3. Dar de baja un estudiante de una asignatura
    4. Salir
    Saliendo del programa.


5.- Diccionario invertido
Escribe una función que tome un diccionario y devuelva otro con las claves y valores intercambiados (lo que antes eran valores ahora son claves, y viceversa).


```python
diccionario = {
    "manzana": "fruta",
    "zanahoria": "verdura",
    "salmon": "pescado",
    "pollo": "carne"
}

def invertir_diccionario(diccionario):
    return {valor: clave for clave, valor in diccionario.items()}
```

6.- Combinar dos diccionarios
Escribe un programa que tome dos diccionarios de productos y precios, y combine los productos comunes sumando sus precios, sin duplicar los elementos únicos.


```python
productos1 = {
    "manzana": 1.20,
    "banana": 0.50,
    "pera": 0.80,
}

productos2 = {
    "banana": 0.40,
    "naranja": 0.60,
    "manzana": 1.10,
}

def juntarDiccionarios(dic1, dic2):
    #copia para evitar modificar datos originales
    diccionarioJuntado = dic1.copy()
    
    for producto, precio in dic2.items():
        if producto in diccionarioJuntado:
            diccionarioJuntado[producto] += precio
        else:
            diccionarioJuntado[producto] = precio
            
    return diccionarioJuntado




productosJuntados = juntarDiccionarios(productos1, productos2)
print(productosJuntados)
```

7.- Filtrar claves y valores
Dado un diccionario de empleados y salarios, filtra e imprime solo los empleados con un salario mayor a un umbral definido.


```python
diccionario = {
    "Ana": 2500,
    "Carlos": 1800,
    "Luis": 3000,
    "María": 2200,
    "Jorge": 3500,
}

umbral = 2300

def filtrarEmpleados(diccionario, umbral):
    empleados_filtrados = {empleado: salario for empleado, salario in diccionario.items() if salario > umbral}
    return empleados_filtrados


print(filtrarEmpleados(diccionario, umbral))

```

    {'Ana': 2500, 'Luis': 3000, 'Jorge': 3500}


8.- Anidación de diccionarios
Partiendo de un diccionario donde las claves son nombres de departamentos y los valores, diccionarios de empleados y sus puestos, tal como se ve en el código de ejemplo, crea un programa que permita realizar las siguientes funciones:

Mostrar el listado de todos los empleados de un departamento
Añadir un empleado a un departamento
Eliminar un empleado de un departamento


```python
departamentos = {
    "Recursos Humanos": {
        "Ana": "Gerente de Recursos Humanos",
        "Luis": "Especialista en Reclutamiento",
        "Elena": "Asistente de Recursos Humanos"
    },
    "Tecnología": {
        "Carlos": "Desarrollador Backend",
        "María": "Desarrolladora Frontend",
        "Pedro": "Administrador de Sistemas"
    },
    "Marketing": {
        "Sofía": "Directora de Marketing",
        "Jorge": "Especialista en SEO",
        "Laura": "Community Manager"
    },
    "Finanzas": {
        "Juan": "Analista Financiero",
        "Lucía": "Contadora",
        "Raúl": "Asesor Financiero"
    }
}

def mostrar_empleados(departamentos, departamento):
    if departamento in departamentos:
        print(f"Empleados en {departamento}:")
        for empleado, puesto in departamentos[departamento].items():
            print(f"{empleado}: {puesto}")
    else:
        print("El departamento no existe.")

def añadir_empleado(departamentos, departamento, empleado, puesto):
    if departamento in departamentos:
        departamentos[departamento][empleado] = puesto
        print(f"{empleado} ha sido añadido al departamento de {departamento}.")
    else:
        print("El departamento no existe.")

def eliminar_empleado(departamentos, departamento, empleado):
    if departamento in departamentos:
        if empleado in departamentos[departamento]:
            del departamentos[departamento][empleado]
            print(f"{empleado} ha sido eliminado del departamento de {departamento}.")
        else:
            print(f"{empleado} no se encuentra en el departamento de {departamento}.")
    else:
        print("El departamento no existe.")


# Menu
while True:
    print("\nMenú:")
    print("1. Mostrar empleados de un departamento")
    print("2. Añadir empleado a un departamento")
    print("3. Eliminar empleado de un departamento")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        departamento = input("Ingresa el nombre del departamento: ")
        mostrar_empleados(departamentos, departamento)
    elif opcion == "2":
        departamento = input("Ingresa el nombre del departamento: ")
        empleado = input("Ingresa el nombre del empleado: ")
        puesto = input("Ingresa el puesto del empleado: ")
        añadir_empleado(departamentos, departamento, empleado, puesto)
    elif opcion == "3":
        departamento = input("Ingresa el nombre del departamento: ")
        empleado = input("Ingresa el nombre del empleado a eliminar: ")
        eliminar_empleado(departamentos, departamento, empleado)
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

```

    
    Menú:
    1. Mostrar empleados de un departamento
    2. Añadir empleado a un departamento
    3. Eliminar empleado de un departamento
    4. Salir
    Empleados en Finanzas:
    Juan: Analista Financiero
    Lucía: Contadora
    Raúl: Asesor Financiero
    
    Menú:
    1. Mostrar empleados de un departamento
    2. Añadir empleado a un departamento
    3. Eliminar empleado de un departamento
    4. Salir
    Saliendo del programa.


9.- Transformación de datos
Dado un diccionario con claves como nombres de estudiantes y valores como una lista de calificaciones, haz un programa que:

Cree un nuevo diccionario que contenga el promedio de calificaciones para cada estudiante
Crea otro diccionario que contengan la nota promedio en cada asignatura


```python
estudiantes = {
    "Ana": {"Matemáticas": 8.5, "Física": 9.0, "Programación": 7.8},
    "Carlos": {"Matemáticas": 9.2, "Física": 8.8, "Programación": 9.4},
    "Luis": {"Matemáticas": 7.6, "Física": 8.0, "Programación": 8.5},
    "María": {"Matemáticas": 9.5, "Física": 10.0, "Programación": 9.8},
    "Jorge": {"Matemáticas": 8.8, "Física": 8.4, "Programación": 7.9},
    "Sofía": {"Matemáticas": 9.1, "Física": 8.9, "Programación": 9.3}
}

def promedio_estudiantes(estudiantes):
    return {estudiante: sum(calificaciones.values()) / len(calificaciones) for estudiante, calificaciones in estudiantes.items()}

def promedio_asignaturas(estudiantes):
    asignaturas = {}
    for calificaciones in estudiantes.values():
        for asignatura, nota in calificaciones.items():
            if asignatura not in asignaturas:
                asignaturas[asignatura] = []
            asignaturas[asignatura].append(nota)
    
    return {asignatura: sum(notas) / len(notas) for asignatura, notas in asignaturas.items()}

promedio_por_estudiante = promedio_estudiantes(estudiantes)
promedio_por_asignatura = promedio_asignaturas(estudiantes)

print("Promedio por estudiante:")
for estudiante, promedio in promedio_por_estudiante.items():
    print(f"{estudiante}: {promedio:.2f}")

print("\nPromedio por asignatura:")
for asignatura, promedio in promedio_por_asignatura.items():
    print(f"{asignatura}: {promedio:.2f}")
```

    Promedio por estudiante:
    Ana: 8.43
    Carlos: 9.13
    Luis: 8.03
    María: 9.77
    Jorge: 8.37
    Sofía: 9.10
    
    Promedio por asignatura:
    Matemáticas: 8.78
    Física: 8.85
    Programación: 8.78

