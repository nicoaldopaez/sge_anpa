ListaTareas=[]


def comprobarNombre(nombreIntroducido):
        while True:
            tarea = nombreIntroducido.strip()
            if(tarea):
                return tarea
            else:
                print("El campo no puede estar vacío")
                nombreIntroducido = input("Intriduce el nombre de la tarea: ")
    
def comprobarPrioridad(prioridadIntroducida):
        while True:
            try:
                prioridad = int(prioridadIntroducida.strip())
                if 1 <= prioridad <= 5:
                    return prioridad
                else:
                    print("La prioridad debe ser un número entero entre 1 y 5")
            except ValueError:
                    print("Debes introducir un número entero")
            prioridadIntroducida = input("Indica la prioridad de la tarea: ")

def comprobarFecha(fechaIntroducida):
        while True:
            fecha = fechaIntroducida.strip()
        if fecha:
            return fecha
        else:
            ("El campo fecha no puede estar vacío")
            fechaIntroducida = input("Indica una fecha límite: ")

terminadaIntroducida =input("Indica si ha sido terminada la tarea introduciendo si o no: ")  
def comprobarTerminada(terminadaIntroducida):
        
        terminada = terminadaIntroducida.strip().lower()
        if terminada != "no":
            completada = True
        else:
             completada = False
        return completada
    


def addTarea():
    nombre = comprobarNombre(input("Introduce el nombre de la tarea: "))
    prioridad = comprobarPrioridad(input("Indica la prioridad de la tarea (1 a 5): "))
    fecha = comprobarFecha(input("Indica una fecha límite: "))
    completada = comprobarTerminada(input("Indica si ha sido terminada la tarea introduciendo si o no: "))

    
    d={
        "nombre :":tarea,
        "prioridad :":prioridad,
        "fecha :":fecha,
        "Completada: ":completada
    }



    ListaTareas.append(d)


def listarTareas():
    print(ListaTareas)


    
def marcarComoCompletada():
    if not ListaTareas:
        print("No hay tareas para marcar como completadas.")
        return

    listarTareas() 
    try:
        indice = int(input("Introduce el número de la tarea que quieres marcar como completada: ")) - 1
        if 0 <= indice < len(ListaTareas):
            ListaTareas[indice]["completada"] = True
            print(f"Tarea '{ListaTareas[indice]['nombre']}' marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor, introduce un número válido.")



def eliminarTarea():
    if not ListaTareas:
        print("No hay tareas para eliminar.")
        return

    listarTareas()  # Mostrar tareas con sus índices
    try:
        indice = int(input("Introduce el número de la tarea que quieres eliminar: ")) - 1
        if 0 <= indice < len(ListaTareas):
            tarea_eliminada = ListaTareas.pop(indice)  # Eliminar tarea
            print(f"Tarea '{tarea_eliminada['nombre']}' eliminada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Por favor, introduce un número válido.")

while True:
    print("1 - añadir")
    print("2 - listar")
    print("3 - Marcar como completada")
    print("4 - Eliminar tarea")
    opcion = input("Dime una opción: ")
    print(opcion)
    if opcion == '1':
        addTarea()
    elif opcion == '2':
        listarTareas()
    elif opcion == '3':
         marcarComoCompletada()
    elif opcion == '4':
         eliminarTarea()
    elif opcion == '5':
         print("Saliendo")
         break
    else:
         print("Opción no válida")