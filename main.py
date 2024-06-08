from clases import Prof
from clases import Estudiantes
prof = Prof()
es = Estudiantes()




def mostrar_menupr():
        print("--"*20)
        print("1. Crear profesor")
        print("2. Leer profesores")
        print("3. Actualizar profesor")
        print("4. Eliminar profesor")
        print("5. Regresar al menu principal")
        print("--"*20)

def mostrar_menues():
        print("--"*20)
        print("1. Crear estudiante")
        print("2. Leer estudiante")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Regresar al menu principal")
        print("--"*20)

def menupr():
    
    while True:
        mostrar_menupr()
        try:  
            opcion = int(input("Selecciona una opción: "))
        
            match opcion:
                case 1:
                    prof.crear_profe()
                case 2:
                    prof.leer_profe()
                case 3:
                    prof.actualizar_profe()
                case 4:
                    prof.eliminar_profe()
                    
                case 5:
                    print("Voliendo al menu principal")
                    return  
                case _:
                    print("Opción no válida. Por favor, selecciona una opción válida.")
        except ValueError:
            print("ingrese una opcion valida ")

def menues():
    
    while True:
        mostrar_menues()   
        try:
            opcion = int(input("Selecciona una opción: "))
        
            match opcion:
                case 1:
                    es.crear_estudiante()
                case 2:
                    es.leer_estudiantes()
                case 3:
                    es.actualizar_estudiante()
                case 4:
                    es.eliminar_estudiante()
                    
                case 5:
                    return  
                case _:
                    print("Opción no válida. Por favor, selecciona una opción válida.")
        except:
            print("ingrese una opcion valida ")


def mp ():
    opcion = 0
    while True:
        print("--"*20)
        print("Menu principal ")
        print("1. Crud de profesores")
        print("2. Crud de estudiantes")
        print("3. Salir")
        print("--"*20)
        try:
            opcion = int(input("Selecciona una opción: "))

            
            match opcion:
                case 1:
                    menupr()
                case 2:
                    menues()
                case 3:
                    print("Saliendo del programa...")
                    break 
            
                case _:
                    print("Opción no válida. Por favor, selecciona una opción válida.")
        except ValueError:
            print("ingrese una opcion valida ")



if __name__ == "__main__":
    mp()





