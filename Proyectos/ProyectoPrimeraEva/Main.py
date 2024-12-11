import Tarea
import GuardarCargarTarea
# Esta clase es la que me permite cambiar los colores y el fondo.
from colorama import Back, Fore, Style, init
# Para que los colores vuelvan a su estado original despues de cada mensaje, para evitar el uso constante de reset.
# He probado lo de los colores sin poner el init() y funciona igualmente, pero en internet dice que hay que ponerlo para que funcione.
init(autoreset=True)

#
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

# Cargo las tareas antes de iniciar el menu al principio del programa
Tarea.listaTareas.extend(GuardarCargarTarea.cargarDesdeCSV("tareas.csv"))
# Inicio el menu
menu()
