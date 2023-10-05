class Libros:
    def __init__(self,nombre,autor,paginas):
        self.nombre = nombre
        self.autor = autor
        self.paginas = paginas
        
    def __str__(self):
        return f"nombre: {self.nombre} // autor: {self.autor} // paginas: {self.paginas}"
        
class Biblioteca:
    def __init__(self):
        self.catalogo = []
        
    def Agregar_libro(self,libro):
        self.catalogo.append(libro)
        
    def Buscar_libro(self, libro):
        for i in(self.catalogo):
            if libro == i.nombre:
                print(i.nombre)
            else: 
                print("el libro no se ha encontrado")
        
    def Mostrar_catalogo(self):
        for i in(self.catalogo):
            return i

libro1 = Libros("Marepoto", "piñera", "464")
Mi_biblioteca = Biblioteca()
Mi_biblioteca.Agregar_libro(libro1)
print(Mi_biblioteca.Mostrar_catalogo())
Mi_biblioteca.Buscar_libro("picoyo")
