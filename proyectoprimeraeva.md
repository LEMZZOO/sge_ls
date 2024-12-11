# Documentación del Sistema de Gestión de Tareas

Este proyecto implementa un sistema de gestión de tareas pendientes que permite agregar, listar, modificar, guardar y cargar tareas desde un archivo CSV.

## Índice
1. [Módulo Principal (`Main.py`)](#modulo-principal-mainpy)
2. [Módulo de Gestión de Tareas (`Tarea.py`)](#modulo-de-gestion-de-tareas-tareapy)
3. [Módulo de Guardar y Cargar Tareas (`GuardarCargarTarea.py`)](#modulo-de-guardar-y-cargar-tareas-guardarcargartareapy)

---

## Módulo Principal (`Main.py`)
Este módulo contiene la función principal del programa que inicia el menú de usuario. Incluye opciones para:
- Agregar una nueva tarea.
- Listar tareas pendientes y completadas.
- Cambiar el estado de las tareas.
- Eliminar tareas.
- Guardar las tareas en un archivo CSV.
- Salir del programa, guardando automáticamente las tareas.

### Código:
```python
import Tarea
import GuardarCargarTarea
# Esta clase es la que me permite cambiar los colores y el fondo.
from colorama import Back, Fore, Style, init
# Para que los colores vuelvan a su estado original despues de cada mensaje, para evitar el uso constante de reset.
# He probado lo de los colores sin poner el init() y funciona igualmente, pero en internet dice que hay que ponerlo para que funcione.
init(autoreset=True)

def menu():
    while True:
        print(Style.BRIGHT + Fore.GREEN + "\nSistema de Gestión de Tareas")
        print(Back.BLACK + Style.BRIGHT + Fore.LIGHTYELLOW_EX + "1. Agregar tarea")
        print(Back.BLACK + Style.BRIGHT + Fore.BLUE + "2. Listar tareas")
        print(Back.BLACK + Style.BRIGHT + Fore.CYAN + "3. Marcar tarea como completada")
        print(Back.BLACK + Style.BRIGHT + Fore.LIGHTBLUE_EX + "4. Marcar tarea como pendiente")
        print(Back.BLACK + Style.BRIGHT + Fore.RED + "5. Eliminar tarea")
        print(Back.BLACK + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "6. Guardar")
        print(Back.BLACK + Style.BRIGHT + Fore.MAGENTA + "0. Guardar y salir")
        opcion = input(Back.BLACK + Style.BRIGHT + Fore.LIGHTWHITE_EX + "Selecciona una opción: ")

        if opcion == "1":
            nombre = input(Back.BLACK + Style.BRIGHT + Fore.GREEN + "Nombre de la tarea: ")
            prioridad = input(Fore.GREEN + "Prioridad (alta, media, baja): ")
            fecha_limite = input(Fore.GREEN + "Fecha límite (YYYY-MM-DD): ")
            Tarea.agregarTarea(nombre, prioridad, fecha_limite)
        elif opcion == "2":
            Tarea.listarTareas()
        elif opcion == "3":
            Tarea.listarTareas()
            indice = int(input(Fore.CYAN + "Selecciona el índice de la tarea a completar: ")) - 1
            Tarea.marcarCompletada(indice)
        elif opcion == "4":
            Tarea.listarTareas()
            indice = int(input(Fore.CYAN + "Selecciona el índice de la tarea marcar como pendiente: ")) - 1
            Tarea.marcarPendiente(indice)
        elif opcion == "5":
            Tarea.listarTareas()
            indice = int(input(Fore.RED + "Selecciona el índice de la tarea a eliminar: ")) - 1
            Tarea.eliminarTarea(indice)
        elif opcion == "6":
            GuardarCargarTarea.guardarEnCSV("tareas.csv", Tarea.listaTareas)
            print(Fore.GREEN + "Tareas guardadas.")
        elif opcion == "0":
            GuardarCargarTarea.guardarEnCSV("tareas.csv", Tarea.listaTareas)
            print(Fore.GREEN + "Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción no válida. Inténtalo de nuevo.")

# Cargo las tareas antes de iniciar el menú al principio del programa
Tarea.listaTareas.extend(GuardarCargarTarea.cargarDesdeCSV("tareas.csv"))
# Inicio el menú
menu() 


```

## Módulo de Gestión de Tareas (`Tarea.py`)
Este módulo gestiona la lista de tareas mediante las siguientes funcionalidades:

- Agregar tarea: Permite registrar tareas con nombre, prioridad, y fecha límite.
- Listar tareas: Muestra todas las tareas con información de estado y vencimiento.
- Marcar como completada: Cambia el estado de una tarea a completada.
- Marcar como pendiente: Permite revertir una tarea completada a pendiente.
- Eliminar tarea: Elimina una tarea basada en su índice.

```python
from datetime import datetime
from colorama import init, Fore
init()

# Lista global para almacenar las tareas
listaTareas = []

# Método para agregar las tareas con el nombre, la prioridad y la fecha límite
def agregarTarea(nombre, prioridad, fechaLimite):
    tarea = {
        "nombre": nombre,
        "prioridad": prioridad,
        "fecha_limite": fechaLimite,
        "completada": False
    }
    listaTareas.append(tarea)

# Método para listar las tareas
def listarTareas():
    if len(listaTareas) != 0:
        for indice, tarea in enumerate(listaTareas, start=1):
            # Operador ternario para marcar las tareas como completadas o pendiente dependiendo que si se marco como completada
            estado = "Completada" if tarea["completada"] else "Pendiente"
            # Convierto la fecha de str a datetime para ver si esta vencida comprobando si es anterior a la fecha actual
            vencida = " (Vencida)" if datetime.strptime(tarea["fecha_limite"], "%Y-%m-%d") < datetime.now() else ""
            print(f"{indice}. {tarea['nombre']} - Prioridad: {tarea['prioridad']}, Fecha límite: {tarea['fecha_limite']}{vencida}, Estado: {estado}")
    else: 
        print(Fore.RED + "No hay tareas")

# Método para marcar las tareas como completadas
def marcarCompletada(indice):
    if 0 <= indice < len(listaTareas):
        listaTareas[indice]["completada"] = True
    else:
        print("Índice de tarea no válido.")

""" Metodo complementario que hice porque probando
    marque una tarea como completada y me di cuenta de
    que no habia forma de retroceder, asi que hice 
    este metodo para cambiar eso."""
def marcarPendiente(indice):
    if 0 <= indice < len(listaTareas):
        listaTareas[indice]["completada"] = False
    else:
        print("Índice de tarea no válido.")

""" Metodo para eliminar las tareas pasando su indice correspondiente
    He pensado en hacer pasando el nombre pero es mucho mas comodo e 
    inteligente usar el indice porque con el nombre habria que hacer
    muchas mas comprobaciones, como siempre decimos, el usuario el tonto"""
def eliminarTarea(indice):
    if 0 <= indice < len(listaTareas):
        listaTareas.pop(indice)
    else:
        print("Índice de tarea no válido.")

```

## Módulo de Guardar y Cargar Tareas (GuardarCargarTarea.py)
Este módulo gestiona la persistencia de datos, permitiendo guardar y cargar tareas desde un archivo CSV:

- Guardar en CSV: Almacena todas las tareas en un archivo CSV utilizando el módulo csv.
En este modulo aplico mis conocimientos avanzados de ficheros
para escribir y leer el fichero tareas.csv

Metodo para guardar las tareas en el archivo csv, 
uso with para que se cierre solo al terminar el bloque, 
se podria hacer solo con open pero habria que cerrar

DictWriter facilita escribir diccionarios, en este caso csv, por lo visto tiene varios modulos, asi que lo use.
Hay que pasar el archivo que tiene que escribir y los nombres de las columnas del mismo,
en este caso son el nombre, la prioridad, la fecha-limite y el estado.
    
Lo siguiente es escribir los encabezados con *writeheader()*, despues ya escribimos las filas con *writerows(listaTAreas)*

- Cargar desde CSV: Lee las tareas desde un archivo CSV al iniciar el programa.
Metodo que invoco antes de iniciar el menu, carga todas las tareas, lee el fichero csv, 
tambien uso DictReader, en este caso solo hay que pasarle el nombre del archivo.

```python
import csv

def guardarEnCSV(nombreArchivo, listaTareas):
    with open(nombreArchivo, "w") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "prioridad", "fecha_limite", "completada"])
        escritor.writeheader()
        escritor.writerows(listaTareas)

def cargarDesdeCSV(nombreArchivo):
    try:
        with open(nombreArchivo, "r") as archivo:
            lector = csv.DictReader(archivo)
            return [dict(tarea) for tarea in lector]
    except FileNotFoundError:
        return []

