class Garaje:
    def __init__(self):
        self.disponible = True
        self.almacenar_Vehiculo = []
        
    def Estacionar_vehiculo(self, vehiculo):
        self.almacenar_Vehiculo.append(vehiculo)
        self.disponible = False
        
class Vehiculo:
    def __init__(self, matricula, propietario):
        self.matricula = matricula
        self.propietario = propietario
        
class Propietario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculo = []
        
    def Estacionar_vehiculo(self, vehiculo):
        if Mi_Garaje.disponible == True:
            Mi_Garaje.Estacionar_vehiculo(vehiculo)
            print("El vehiculo se estaciono correctamente")
            print(Mi_Garaje.disponible)
        else:
            print("no hay espacio en el garaje")   
Mi_Garaje = Garaje()         
Jorge = Propietario("Jorge")
Brandon = Propietario("Brandon")
vehiculo_de_jorge = Vehiculo("A40-21J", Jorge)
vehiculo_de_Brandon = Vehiculo("H74-1HO", Brandon)
print(Jorge.Estacionar_vehiculo(vehiculo_de_jorge))
print(Brandon.Estacionar_vehiculo(vehiculo_de_Brandon))
