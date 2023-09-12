class Producto:
    def __init__(self, nombre,precio,categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        
    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Categoria: {self.categoria}")
        
class Electronico(Producto):
    def __init__(self, nombre, precio, categoria,consumo):
        super().__init__(nombre, precio, categoria)
        self.consumo = consumo
        
    def mostrar_detalle(self):
        return super().mostrar_detalle()
        
class Alimenticio(Producto):
    def __init__(self, nombre, precio, categoria, proteinas):
        super().__init__(nombre, precio, categoria)
        self.proteinas = proteinas
        
    def mostrar_detalle(self):
        return super().mostrar_detalle()
        
class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria,color):
        super().__init__(nombre, precio, categoria)
        self.color = color
        
    def mostrar_detalle(self):
        return super().mostrar_detalle()
    
microondas = Electronico("Microondas", "35,000", "Electrodomestico", "120 watts")
tostador = Electronico("Tostador", "22,990", "Electrodomestico", "80 watts")

pizza = Alimenticio("Pizza", "9,000", "Alimenticio", "0")
lasagna = Alimenticio("Lasagna", "7,000", "Alimenticio", "90")

short = Vestimenta("Short", "10,990", "Vestimenta", "rojo")
cortavientos = Vestimenta("Cortavientos", "72,990", "Vestimenta", "beige")

Electronico = [microondas,tostador]
Alimenticio = [pizza,lasagna]
Vestimenta = [short,cortavientos]

for i in(Electronico):
    print(i.mostrar_detalle())

for x in(Alimenticio):
    print(x.mostrar_detalle())
    
for j in(Vestimenta):
    print(j.mostrar_detalle())
