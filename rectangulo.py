
class Cectangulo:
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho
        
    #metodos
    def CalcularArea(longitud,ancho):
        area = longitud*ancho
        return f"El area del rectangulo es: {area}"
    
    def CalcularPerimetro(longitud,ancho):
        perimetro = (longitud*2)+(ancho*2)
        return f"El perimetro del rectangulo es: {perimetro}"
    