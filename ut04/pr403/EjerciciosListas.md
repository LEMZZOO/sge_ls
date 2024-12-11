Ordenando elementos: Mostrar los nombres ordenados alfabéticamente en orden inverso.


```python
nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]
nombres.sort()
print(nombres)
```

    ['Adela', 'Adrián', 'Agustín', 'Ainhoa', 'Alberto', 'Alejandra', 'Alejandro', 'Alfonso', 'Alfredo', 'Alicia', 'Amalia', 'Amparo', 'Ana', 'Andrea', 'Andrés', 'Antonio', 'Aníbal', 'Araceli', 'Ariadna', 'Baltasar', 'Beatriz', 'Belén', 'Berta', 'Blanca', 'Braulio', 'Candela', 'Carla', 'Carlos', 'Carmen', 'Carolina', 'Celia', 'Claudia', 'Consuelo', 'Cristina', 'Cristina', 'César', 'Daniel', 'Daniela', 'David', 'Diego', 'Dolores', 'Eduardo', 'Elena', 'Elisa', 'Elsa', 'Emilia', 'Emilio', 'Enrique', 'Esperanza', 'Esteban', 'Esther', 'Eugenio', 'Eva', 'Fabián', 'Fausto', 'Federico', 'Fernando', 'Francisco', 'Fátima', 'Félix', 'Gabriela', 'Gema', 'Gemma', 'Gloria', 'Gonzalo', 'Gregorio', 'Guillermo', 'Hugo', 'Humberto', 'Héctor', 'Inmaculada', 'Inés', 'Irene', 'Isabel', 'Ismael', 'Iván', 'Javier', 'Jesús', 'Joaquín', 'Joaquín', 'Jorge', 'Juan', 'Julia', 'Julio', 'Julián', 'Laura', 'Leandro', 'Lidia', 'Lorena', 'Lourdes', 'Lucía', 'Luis', 'Manuel', 'Manuela', 'Marcelo', 'Marcos', 'Marcos', 'Mariano', 'Marina', 'Mario', 'Marta', 'María', 'Mercedes', 'Miguel', 'Milagros', 'Miriam', 'Mónica', 'Natalia', 'Nicolás', 'Noelia', 'Nuria', 'Olga', 'Pablo', 'Patricia', 'Paula', 'Pedro', 'Pilar', 'Rafael', 'Ramón', 'Raquel', 'Raúl', 'Ricardo', 'Roberto', 'Rocío', 'Rosa', 'Rubén', 'Salvador', 'Santiago', 'Sara', 'Sebastián', 'Sergio', 'Silvia', 'Sofía', 'Tamara', 'Teresa', 'Tomás', 'Valentín', 'Verónica', 'Vicente', 'Victoria', 'Víctor', 'Álex', 'Álvaro', 'Ángel', 'Ángela', 'Óscar']


Contando elementos: Contar el número de nombres que comienzan con la letra a


```python
nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]
contador = 0
for i in nombres:
    if (i[0].lower() == "a"):
        contador += 1
print(f"hay {contador} nombres que comienzan por A")
```

    hay 19 nombres que comienzan por A


Buscar un elementos: Pregunte al usuario su nombre y le indique si está en la lista, y en caso afirmativo, en qué posición está.


```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]
nombreUsuarios = input("introduce tu nombre: ")


if nombreUsuarios in nombres: print(f"Tu nombre ya existe en la lista, en la posicion {str(nombres.index(nombreUsuarios))}")
else: print("Tu no nombre no está en la lista")
```

    introduce tu nombre:  Javier


    Tu nombre ya existe en la lista, en la posicion 2


Primeros elementos: Pregunte al usuario su nombre y le muestre el listado de todos los nombres que se encuentran delante del suyo.

nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]
entrada = input("introduce tu nombre: ")
if (entrada in nombres): 
    nombresDelante = nombres[0:nombres.index(entrada)]
    print(nombresDelante)
else: print("Tu nombre no esta la lista")


Obtener número de nombres de una longitud: Pregunte al usuario un número y le diga cuántos nombres hay en la lista con la misma longitud que el número indicado


```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]
entrada = int(input("introduce una longitud: "))
numeroNombres = 0
for nombre in nombres:
    if (len(nombre) == entrada):
        numeroNombres += 1
print(f"Hay {numeroNombres} nombres con {entrada} de longitud")
```

    introduce una longitud:  5


    Hay 35 nombres con 5 de longitud



```python
Nombres cortos: Muestre todos los nombres cuya longitud sea igual o inferior a 4 caracteres
```


```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]
entrada = int(input("introduce una longitud: "))
numeroNombres = 0
nombresMismaLongitud = []
for nombre in nombres:
    if (len(nombre) == entrada):
        numeroNombres += 1
        nombresMismaLongitud += [nombre]
print(f""""Hay {numeroNombres} nombres con {entrada} de longitud
Nombres: {nombresMismaLongitud} """)
```

    introduce una longitud:  5


    "Hay 35 nombres con 5 de longitud
    Nombres: ['María', 'Lucía', 'Sofía', 'Pedro', 'Jorge', 'Elena', 'Laura', 'David', 'Marta', 'Paula', 'Pablo', 'Irene', 'Diego', 'Jesús', 'Ángel', 'Julia', 'Pilar', 'Ramón', 'Lidia', 'Óscar', 'Rubén', 'Nuria', 'Berta', 'Elisa', 'Mario', 'Félix', 'Rocío', 'Celia', 'Tomás', 'Belén', 'Gemma', 'Julio', 'Carla', 'Adela', 'César'] 


Número de vocales: Indique cuántas veces se repite cada una de las vocales entre todos los nombres (ignorando mayúsculas y minúsculas)


```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]
vocales = ["a", "e", "i", "o", "u"]
nombresJuntados = "".join(nombres).lower()
numVocales = {vocal: nombresJuntados.count(vocal) for vocal in vocales}
print(f"Numero de veces que se repite cada vocal: {numVocales}")


```

    Numero de veces que se repite cada vocal: {'a': 152, 'e': 78, 'i': 75, 'o': 65, 'u': 29}


Número de letras: Imprima el número de veces que se repite cada letra del abecedario entre todos los elementos de la lista.


```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

nombresJuntados = "".join(nombres).lower()
numLetras = {letra: nombresJuntados.count(letra) for letra in nombresJuntados}
print(numLetras)
```

    {'a': 152, 'l': 70, 'e': 78, 'j': 11, 'n': 62, 'd': 28, 'r': 79, 'o': 65, 'm': 32, 'í': 10, 'v': 12, 'i': 75, 'u': 29, 'c': 34, 's': 41, 'f': 11, 'g': 20, 'b': 17, 'p': 7, 't': 27, 'q': 4, 'é': 7, 'ó': 4, 'á': 12, 'h': 5, 'ú': 2, 'z': 3, 'x': 2}


Sumar elementos de una lista: Dada una lista de números, escribe un programa que calcule y muestre la suma de todos sus elementos.


```python
numero = [1, 2 ,3 ,4 ,5 ,6 ,7 ,8]
total = sum(numero)
print(total)
```

    36


Contar elementos específicos: Dada una lista de palabras, permite al usuario ingresar una palabra y cuenta cuántas veces aparece en la lista.


```python
nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

entrada = input("Introduce una palabra: ")
numVeces = 0
if(entrada in nombres): numVeces += 1
print (numVeces)
```

    Introduce una palabra:  a


    0


Eliminar duplicados: Dada una lista de números, elimina todos los elementos duplicados y muestra la lista con solo valores únicos.


```python
numero = [1, 1, 1, 2 ,3 ,4 ,5 ,6, 6 ,7 ,8]
numeroFiltado = set(numero)
print(numeroFiltado)
```

    {1, 2, 3, 4, 5, 6, 7, 8}


Máximo y mínimo: Escribe una función que tome una lista de números y devuelva el valor máximo y mínimo de la lista.


```python
numero = [1, 1, 1, 2 ,3 ,4 ,5 ,6, 6 ,7 ,8]
print(f"El numero mas alto es {max(numero)}")
print(f"El numero mas bajo es {min(numero)}")
```

    El numero mas alto es 8
    El numero mas bajo es 1


Filtrar números pares: Dada una lista de números, genera una nueva lista que contenga solo los números pares.


```python
numeros = [1, 1, 1, 2 ,3 ,4 ,5 ,6, 6 ,7 ,8]
numerosPares = set([num for num in numeros if num %2 == 0])
print(numerosPares)
        
```

    {8, 2, 4, 6}


Revertir una lista: Escribe una función que tome una lista y devuelva una nueva lista con los elementos en orden inverso, sin utilizar el método .reverse().


```python
numerosInvert = numeros[::-1]
print(numerosInvert)
```

    [8, 7, 6, 6, 5, 4, 3, 2, 1, 1, 1]


Concatenar listas: Dadas dos listas de números, crea una función que devuelva una tercera lista que contenga los elementos de ambas listas intercalados.


```python
def intercalar_listas(lista1, lista2):
    resultado = []

    for elem1, elem2 in zip(lista1, lista2):
        resultado.append(elem1)
        resultado.append(elem2)
    
    resultado.extend(lista1[len(lista2):])
    resultado.extend(lista2[len(lista1):])
    
    return resultado

lista1 = [1, 3, 5]
lista2 = [2, 4, 6, 8, 10]
print(intercalar_listas(lista1, lista2))
```

    [1, 2, 3, 4, 5, 6, 8, 10]


Encuentra elementos comunes: Escribe un programa que tome dos listas y devuelva una nueva lista con los elementos que son comunes en ambas.


```python
def encontrar_comunes(lista1, lista2):
    
    comunes = set(lista1) & set(lista2)
    return list(comunes)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print(encontrar_comunes(lista1, lista2)) 

```

    [4, 5]


Dividir una lista: Dada una lista de números, crea dos listas: una con los números mayores o iguales a la media y otra con los números menores a la media.


```python

```

Lista de listas: Crea una lista de listas que represente una matriz de números y escribe una función que devuelva la suma de cada fila y columna.


```python

```
