import csv
""" En este modulo aplico mis conocimientos avanzados de ficheros
    para escribir y leer el fichero tareas.csv"""

""" Metodo para guardar las tareas en el archivo csv, 
    uso with para que se cierre solo al terminar el bloque, 
    se podria hacer solo con open pero habria que cerrar """

""" DictWriter facilita escribir diccionarios, en este caso csv, por lo visto tiene varios modulos, asi que lo use.
    Hay que pasar el archivo que tiene que escribir y los nombres de las columnas del mismo,
    en este caso son el nombre, la prioridad, la fecha-limite y el estado.
    
    Lo siguiente es escribir los encabezados con *writeheader()*, despues ya escribimos las filas con *writerows(listaTAreas)*"""
def guardarEnCSV(nombreArchivo, listaTareas):
    with open(nombreArchivo, "w") as archivo:

        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "prioridad", "fecha_limite", "completada"])
        escritor.writeheader()
        escritor.writerows(listaTareas)

""" Metodo que invoco antes de iniciar el menu, carga todas las tareas, lee el fichero csv, 
    tambien uso DictReader, en este caso solo hay que pasarle el nombre del archivo. """
def cargarDesdeCSV(nombreArchivo):
    try:
        with open(nombreArchivo, "r") as archivo:
            lector = csv.DictReader(archivo)
            return [dict(tarea) for tarea in lector]
    except FileNotFoundError:
        return []
