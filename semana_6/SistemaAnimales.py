class Animal:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad


class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.patas = 4

    def grunir(self,sonido):
        return f"El perro hace {sonido}"

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.patas = 4

    def maullar(self,sonido):
        return f"El gato hace {sonido}"
    
suki = Gato("suki","6 meses")
kira = Perro("Kira","4 años")
print(kira.grunir("grrrr"))
print(suki.maullar("miauuu"))