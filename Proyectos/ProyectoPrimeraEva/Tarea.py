from datetime import datetime
from colorama import init, Fore
init()

listaTareas = []

# Metodo para agregar las tareas con el nombre, la prioridad y la fecha límite.
def agregarTarea(nombre, prioridad, fechaLimite):
    tarea = {
        "nombre": nombre,
        "prioridad": prioridad,
        "fecha_limite": fechaLimite,
        "completada": False
    }
    listaTareas.append(tarea)
# Metodo para listar las tareas.
def listarTareas():
    if len(listaTareas) != 0:
        for indice, tarea in enumerate(listaTareas, start=1):
            # Operador ternario para marcar las tareas como completadas o pendiente dependiendo que si se marco como completada
            estado = "Completada" if tarea["completada"] else "Pendiente"
            # Convierto la fecha de str a datetime para ver si esta vencida comprobando si es anterior a la fecha actual
            vencida = " (Vencida)" if datetime.strptime(tarea["fecha_limite"], "%Y-%m-%d") < datetime.now() else ""
            print(f"{indice}. {tarea['nombre']} - Prioridad: {tarea['prioridad']}, Fecha límite: {tarea['fecha_limite']}{vencida}, Estado: {estado}")
    else: print(Fore.RED + "No hay tareas")

# Metodo para marcar las tareas como completadas
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
