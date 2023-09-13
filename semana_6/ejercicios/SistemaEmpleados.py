class Empleado:
    def __init__(self,nombre,edad,salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, aptitudes, grupoAcargo):
        super().__init__(nombre, edad, salario)
        self.aptitudes = aptitudes
        self.grupoAcargo = grupoAcargo
        self.rol = "analiza, planifica, dirige y gestiona que todas las\n funciones se realicen de manera óptima dentro de una empresa"
        
    def describir_rol(self):
        print(f"El gerente  {self.rol}")
        print()
    
class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, habilidad, especialidad):
        super().__init__(nombre, edad, salario)
        self.habilidad = habilidad
        self.especialidad = especialidad
        self.rol = "Planificar, organizar, programar, dirigir y controlar la\n construcción y montaje industrial de todo tipo de obras de ingeniería"

    def describir_rol(self):
        print(f"El ingeniero se encarga de {self.rol}")
        print()
        
class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, horario):
        super().__init__(nombre, edad, salario)
        self.horario = horario
        self.rol = "ayuda a los directivos hacer un mejor uso de su tiempo"

    def describir_rol(self):
        print(f"un Asistente {self.rol}")
        print()
        
john = Gerente("john Alvarez", "52", "1,000,000", "Optimista", "B18")
Benjamin = Ingeniero("Benjamin Aburto", "27", "789,000", "Trabajo en equipo", "Informatica")
Nicolas = Asistente("Nicolas Peña", "29", "500,000", "2:00 PM - 7:30 PM")

empleados = [john,Benjamin,Nicolas]
for i in (empleados):
    i.describir_rol()