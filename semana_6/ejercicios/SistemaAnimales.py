class Animal:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.patas = 4

    def ladrar(self,sonido):
        return f"El perro hace {sonido}"

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.patas = 4

    def maullar(self,sonido):
        return f"El gato hace {sonido}"
    
class Pajaro(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        
    def piar(self,sonido):
        return(f"el pajaro haces {sonido}")
    
suki = Gato("suki","6 meses")
kira = Perro("Kira","4 años")
koko = Pajaro("Koko","4 meses")
pajarosonido = input("que sonido hace el pajaro?: ")
print(kira.ladrar("guauu"))
print(suki.maullar("miauuu"))
print(koko.piar(pajarosonido))