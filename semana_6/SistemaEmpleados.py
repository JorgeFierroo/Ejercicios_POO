class Empleado:
    def __init__(self,nombre,edad,salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, aptitudes, grupoAcargo):
        super().__init__(nombre, edad, salario)
        self.rol = aptitudes
        self.grupoAcargo = grupoAcargo
        
    def describir_rol(self):
        print(f"")
    
class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, habilidad, especialidad):
        super().__init__(nombre, edad, salario)
        self.habilidad = habilidad
        self.especialidad = especialidad
        
class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, horario):
        super().__init__(nombre, edad, salario)
        self.horario = horario
        
john = Gerente("john Alvarez", "52", "1,000,000", "Optimista", "B18")
Benjamin = Ingeniero("Benjamin Aburto", "27", "789,000", "Trabajo en equipo", "Informatica")
Nicolas = Asistente("Nicolas Peña", "29", "500,000", "2:00 PM - 7:30 PM")


