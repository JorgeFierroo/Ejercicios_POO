class Persona:
    def __init__(self,nombre,apellido,fecha_de_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento

    #Metodo para presentarse
    def Presentarse(self):
        print(f"hola mi nombre es {self.nombre} {self.apellido} y naci {self.fecha_de_nacimiento}")


class Estudiante(Persona): #Clase estudiante hereda atributos de persona
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
    
    
#Comprobando si funciona la clase asignatura
informatica = Asignatura("programacion","300","5") #Creando una instancia de asignatura
print(informatica.Mostrar_informacion()) #Mostrando la informacion de la asignatura creada

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
        estudiantesExe.append(nuevo_estudiante)
        
def Funcion_crear_Asignaturas():
    cantidadAsignaturas = int(input("Ingresa la cantidad de asignaturas a crear: "))
    for i in range(1, cantidadAsignaturas + 1):
        print("ingrese los siguientes datos para su asignatura ", i)
        nombreAsignatura = input("Nombre: ")
        codigoAsignatura = input("Codigo: ")
        creditosAsignatura = input("Creditos: ")
    
        nueva_Asignatura = Asignatura(nombreAsignatura,codigoAsignatura,creditosAsignatura)
        asignaturasExe.append(nueva_Asignatura)
    
def Funcion_crear_Grupo():
    cantidadGrupos = int(input("Ingresa la cantidad de grupos a crear: "))
    for i in range(1, cantidadGrupos +1):
        print("ingrese los siguientes datos para el grupo ", i)
        numeroGrupo = input("numero del grupo: ")
        Asignatura_grupo = input("Asignatura: ")
        Profesor_grupo = input("Profesor: ")
        
        nuevo_grupo = Grupo(numeroGrupo,Asignatura_grupo,Profesor_grupo)
        gruposExe.append(nuevo_grupo)
        
def Funcion_crear_Profesor():
    cantidadProfesores = int(input("Ingresa la cantidad de profesores a crear: "))
    for i in range(1, cantidadProfesores +1):
        print("ingrese los siguientes datos para el El profesor ", i)
        nombreProfesor = input("Nombre: ")
        ApellidoProfesor = input("Apellido: ")
        FechaNacimiento_Profesor = input("Fecha de nacimiento: ")
        numeroEmpleado_Profesor = input("Numero de empleado: ")
        DepartamentoProfesor = input("Departamento: ")
        
        nuevo_profesor = Profesor(nombreProfesor,ApellidoProfesor,FechaNacimiento_Profesor,numeroEmpleado_Profesor,DepartamentoProfesor)
        profesoresExe.append(nuevo_profesor)
    
Running = True # Hace funcionar el bucle

#Bucle para interactuar de forma textual 
while Running:
    asignaturasExe = []
    gruposExe = []
    profesoresExe = []
    estudiantesExe = []
    quieres = input("quieres agregar crear Asignaturas? (S/N): ").upper()
    if quieres == "S":
        Funcion_crear_Asignaturas()
    elif quieres == "N":
        print("Que tenga buen dia")
        Running = False
    else:
        print("Incorrecto")