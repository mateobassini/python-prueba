def mostrar_tareas(pendientes, terminadas):
    print("Tareas pendientes:")
    for tarea in pendientes:
        print("- " + tarea)
    print("\nTareas terminadas:")
    for tarea in terminadas:
        print("- " + tarea)

def agregar_tarea(pendientes):
    tarea_nueva = input("Ingrese la nueva tarea: ")
    pendientes.append(tarea_nueva)
    print("Tarea agregada correctamente.")

def marcar_como_terminada(pendientes, terminadas):
    if not pendientes:
        print("No hay tareas pendientes para marcar como terminadas.")
        return

    mostrar_tareas(pendientes, terminadas)
    idx = int(input("Ingrese el índice de la tarea que desea marcar como terminada: "))

    if idx < 0 or idx >= len(pendientes):
        print("Índice inválido.")
        return

    tarea_terminada = pendientes.pop(idx)
    terminadas.append(tarea_terminada)
    print("Tarea marcada como terminada correctamente.")

tareas_pendientes = []
tareas_terminadas = []

while True:
    print("\nSeleccione una opción:")
    print("1. Mostrar tareas")
    print("2. Agregar nueva tarea")
    print("3. Marcar tarea como terminada")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        mostrar_tareas(tareas_pendientes, tareas_terminadas)
    elif opcion == "2":
        agregar_tarea(tareas_pendientes)
    elif opcion == "3":
        marcar_como_terminada(tareas_pendientes, tareas_terminadas)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. seleccione una opción válida.")
