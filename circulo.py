class Circulo:
    def __init__(self,radio):
        self.radio = radio
        
    def CalcularArea(radio):
        area = (radio**2)*3.14
        return f"El area del circulo es: {area}"
    
    def CalcularPerimetro(radio):
        perimetro = (2*radio)*3.14
        return f"El perimetro del circulo es: {perimetro}"
    
    def cambiar_radio(self, cambiar):
        self.radio = cambiar
        return f"el nuevo radio es: {self.radio}"
    
circulo0 = Circulo(4)
circulo1 = Circulo.CalcularArea(circulo0.radio)
circulo2 = Circulo.CalcularPerimetro(circulo0.radio)
print(circulo1)
print(circulo2)
circulo3 = circulo0.cambiar_radio(7)
print(circulo3)

