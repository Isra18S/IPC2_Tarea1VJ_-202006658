class Prof:
    def __init__(self):
        self.profesores = []

    def crear_profe(self):
        nombre = input("Ingrese el nombre del profesor: ")
        curso = input("Ingrese el curso del profesor: ")
        id = input("Ingrese el ID del profesor: ")
        profesion = input("Ingrese la profesión del profesor: ")

        nuevo_profesor = {'nombre': nombre, 'curso': curso, 'id': id, 'profesion': profesion}
        self.profesores.append(nuevo_profesor)
        print("Profesor creado con éxito.")

    def leer_profe(self):
        if not self.profesores:
            print("No hay profesores registrados.")
            return
        print("Lista de profesores:")
        for i, profesor in enumerate(self.profesores, start=1):
            print(f"Profesor {i}:")
            print(f"Nombre: {profesor['nombre']}")
            print(f"Curso: {profesor['curso']}")
            print(f"ID: {profesor['id']}")
            print(f"Profesión: {profesor['profesion']}")
            print()

    def actualizar_profe(self):
        if not self.profesores:
            print("No hay profesores registrados.")
            return
        self.leer_profe()
        idx = int(input("Ingrese el número del profesor a actualizar: ")) - 1

        if 0 <= idx < len(self.profesores):
            print("Deja en blanco los campos que no quieras cambiar.")
            nombre = input("Ingrese el nuevo nombre del profesor: ")
            curso = input("Ingrese el nuevo curso del profesor: ")
            id = input("Ingrese el nuevo ID del profesor: ")
            profesion = input("Ingrese la nueva profesión del profesor: ")

            if nombre:
                self.profesores[idx]['nombre'] = nombre
            if curso:
                self.profesores[idx]['curso'] = curso
            if id:
                self.profesores[idx]['id'] = id
            if profesion:
                self.profesores[idx]['profesion'] = profesion

            print("Profesor actualizado con éxito.")
        else:
            print("Número de profesor inválido.")

    def eliminar_profe(self):
        if not self.profesores:
            print("No hay profesores registrados.")
            return
        self.leer_profe()
        idx = int(input("Ingrese el número del profesor a eliminar: ")) - 1

        if 0 <= idx < len(self.profesores):
            self.profesores.pop(idx)
            print("Profesor eliminado con éxito.")
        else:
            print("Número de profesor inválido.")



class Estudiantes:
    def __init__(self):
        self.estudiantes = []

    def crear_estudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        curso = input("Ingrese el curso del estudiante: ")
        id = input("Ingrese el ID del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")

        nuevo_estudiante = {'nombre': nombre, 'curso': curso, 'id': id, 'carrera': carrera}
        self.estudiantes.append(nuevo_estudiante)
        print("Estudiante creado con éxito.")

    def leer_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        print("Lista de estudiantes:")
        for i, estudiante in enumerate(self.estudiantes, start=1):
            print(f"Estudiante {i}:")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Curso: {estudiante['curso']}")
            print(f"ID: {estudiante['id']}")
            print(f"carrera: {estudiante['carrera']}")
            print()

    def actualizar_estudiante(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        self.leer_estudiantes()
        idx = int(input("Ingrese el número del estudiante a actualizar: ")) - 1

        if 0 <= idx < len(self.estudiantes):
            print("Deja en blanco los campos que no quieras cambiar.")
            nombre = input("Ingrese el nuevo nombre del estudiante: ")
            curso = input("Ingrese el nuevo curso del estudiante: ")
            id = input("Ingrese el nuevo ID del estudiante: ")
            carrera= input("Ingrese la nueva carrera del estudiante: ")

            if nombre:
                self.estudiantes[idx]['nombre'] = nombre
            if curso:
                self.estudiantes[idx]['curso'] = curso
            if id:
                self.estudiantes[idx]['id'] = id
            if carrera:
                self.estudiantes[idx]['carrera'] = carrera

            print("Estudiante actualizado con éxito.")
        else:
            print("Número de estudiante inválido.")

    def eliminar_estudiante(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return
        self.leer_estudiantes()
        idx = int(input("Ingrese el número del estudiante a eliminar: ")) - 1

        if 0 <= idx < len(self.estudiantes):
            self.estudiantes.pop(idx)
            print("Estudiante eliminado con éxito.")
        else:
            print("Número de estudiante inválido.")

    
    
    


    
