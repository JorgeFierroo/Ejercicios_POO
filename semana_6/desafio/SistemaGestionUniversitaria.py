class Persona:
    def __init__(self,nombre,apellido,fecha_de_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def Presentarse(self):
        print(f"hola mi nombre es {self.nombre} {self.apellido} y naci {self.fecha_de_nacimiento}")


class Estudiante(Persona):
    def __init__(self, nombre, apellido, fecha_de_nacimiento,matricula,carrera,semestre):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        
    def Estudiar(self,materia,horas):
        return f"{self.nombre} estudio {materia} durante {horas}"
    
    def Presentarse(self):
        return f"hola mi nombre es {self.nombre} {self.apellido}, naci el {self.fecha_de_nacimiento}, me matricule el\n {self.matricula}, pertenezco a la carrera de {self.carrera} y voy en el {self.semestre}"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, nacido el {self.fecha_de_nacimiento}, matriculado en {self.matricula}, carrera: {self.carrera}, semestre: {self.semestre}"
    
jorge = Estudiante("Jorge", "Fierro", "01/27/2004", "2023", "Ingenieria Civil Informatica", "segundo semestre")
print(jorge.Estudiar("matematicas", "2 horas"))
print(jorge.Presentarse())

class Profesor(Persona):
    def __init__(self, nombre, apellido, fecha_de_nacimiento, numero_empleado, departamento):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self.numero_empleado = numero_empleado
        self.departamento = departamento
        
    def Enseñar(self, Materia):
        return f"El profesor esta enseñando {Materia}"
    
    def Presentarse(self):
        return f"hola mi nombre es {self.nombre} {self.apellido}, naci {self.fecha_de_nacimiento} y soy profesor de la {self.departamento}"
    
julian = Profesor("julian","Peña","08/05/1983","1042","Facultad de Ingenieria")

print(julian.Enseñar("Programacion"))
print(julian.Presentarse())

class Asignatura:
    def __init__(self,nombre,codigo,creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        
    def Mostrar_informacion(self):
        return f"Asignatura: {self.nombre} / Codigo: {self.codigo} / Creditos: {self.creditos}"
    
informatica = Asignatura("programacion","300","5")
print(informatica.Mostrar_informacion())

class Grupo:
    def __init__(self,numero_grupo,asignatura,profesor):
        self.numero_grupo = numero_grupo
        self.asignatura = asignatura
        self.profesor = profesor
        self.estudiantes = []
        
    def Agregar_estudiante(self,Agregarestudiante):
        self.estudiantes.append(Agregarestudiante)
        print(f"Se agrego el estudiante {Agregarestudiante.nombre}")
        
    def Mostrar_estudiantes(self):
        for i in(self.estudiantes):
            print(i.nombre)
            
    def Mostrar_grupo(self):
        print(f"Numero de grupo: {self.numero_grupo}")
        print(f"Asignatura: {self.asignatura.nombre}")
        print(f"Profesor: {self.profesor.nombre}")
        print("estudiantes:")
        self.Mostrar_estudiantes()
        
        
grupo1 = Grupo("1",informatica,julian)
grupo1.Agregar_estudiante(jorge)
print(grupo1.Mostrar_grupo())


Running = True
def Funcion_crear_Estudiantes():
    
    cantidadEstudiantes = int(input("Ingresa los estudiantes a crear: "))
    for i in range(1, cantidadEstudiantes + 1):
        print("ingrese los datos del estudiante ", i)
        nombre_estudiante = input("Nombre: ")
        apellido_estudiante = input("Apellido: ")
        fecha_nacimiento_estudiante = input("fecha de nacimiento: ")
        fecha_matricula = input("fecha de matricula: ")
        carrera_estudiante = input("carrera: ")
        semestre_estudiante = input("semestre: ")
        
        nuevo_estudiante = Estudiante(nombre_estudiante, apellido_estudiante, fecha_nacimiento_estudiante, fecha_matricula, carrera_estudiante, semestre_estudiante)
        estudiantesas.append(nuevo_estudiante)

while Running:
    estudiantesas = []
    quieres = input("quieres agregar estudiantes) (S/N): ")
    if quieres == "S":
        Funcion_crear_Estudiantes()
    for i in(estudiantesas):
        i.nombre
