#Este programa consiste en un gestor de tareas simple.

#Lista de tareas
tareas = []

#Funcion nos permites mostrar las opciones en pantalla
def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Marcar tarea completa")
    print("5. Salir")

#Funcion que nos permite ingresar una nueva tarea
def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' agregada exitosamente.")   

#Funcion que muestra las tareas actuales
def ver_tareas():
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\nLista de Tareas:")
        for i, tarea in enumerate(tareas, start=1):
            estado = "✓" if tarea["completada"] else "✗"
            print(f"{i}. [{estado}] {tarea['descripcion']}")
               


#Funcion para eliminar una tarea.
def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar.")
        return
    ver_tareas()
    try:
        numero = int(input("Ingrese el número de la tarea a eliminar: "))
        indice = numero - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada exitosamente.")
        else:
            print("Número de tarea inválido.")

    except ValueError:
            print("Por favor, ingrese un número válido.")    


#Funcion para marcar una tarea como completa
def completar_tarea():
    if not tareas:
        print("No hay tareas para completar.")
        return
    ver_tareas()
    try:
        numero = int(input("Ingrese el número de la tarea a marcar como completa: "))
        indice = numero - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            print(f"Tarea  marcada como completa.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
            print("Por favor, ingrese un número válido.")             

#Funcion que maneja el flujo del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            ver_tareas()

        elif opcion == '3':
            eliminar_tarea() 

        elif opcion == '4':
            completar_tarea()   

        elif opcion == '5':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

main()

