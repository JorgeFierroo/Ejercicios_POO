import tkinter as tk
from tkinter import Canvas

class Listas:
    def __init__(self, root=None):
        self.Milista = []
        self.root = root
        
    def Agregar(self,elemento, gui=None):
        self.Milista.append(elemento)
        if gui:
            gui.update_grafico()
            
    def Buscar(self, elemento):
        if len(self.Milista)>=1:
            izquierda, derecha = 0, len(self.Milista) - 1
            while izquierda <= derecha:
                mid = (izquierda + derecha) // 2
                if self.Milista[mid] == elemento:
                    return True
                elif self.Milista[mid] < elemento:
                    izquierda = mid + 1
                else:
                    derecha = mid - 1
        else:
            print("Su lista esta vacia")
    
    def Ordenar(self, gui=None):
        n = len(self.Milista)
        if n < 1:
            print("//// la lista ya está ordenada y/o está vacía ////")
            print(Mi_lista.Milista)
        else:
            for i in range(n):
                for j in range(0, n-i-1):
                    if self.Milista[j] > self.Milista[j+1]:
                        self.Milista[j], self.Milista[j+1] = self.Milista[j+1], self.Milista[j]
                        print(self.Milista)
                        if gui:  # Actualiza el gráfico después de cada intercambio
                            gui.update_grafico()
                            self.root.after(200)  # Añade un pequeño retraso para que la animación sea visible
        return self.Milista
        
class ListasGUI:
    def __init__(self, root, lista):
        self.root = root
        self.lista = lista
        self.canvas = Canvas(self.root, width=400, height=300)
        self.canvas.pack()
        self.update_grafico()

    def update_grafico(self):
        self.canvas.delete("all")  # Borra cualquier gráfico anterior
        if len(self.lista.Milista) == 0:  # Si la lista está vacía, no hace nada
            return
        max_value = max(self.lista.Milista)
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        bar_width = canvas_width / len(self.lista.Milista)
        for index, value in enumerate(self.lista.Milista):
            bar_height = (value / max_value) * (canvas_height - 20)
            self.canvas.create_rectangle(index * bar_width, canvas_height - bar_height, (index + 1) * bar_width, canvas_height, fill="blue")
        self.root.update()
        
    
def iniciar_interfaz():
    valido = ["S","N"]
    while True:
        entrada = input("Quieres comenzar? (S/N): ").upper()

        try:
            letra = str(entrada)
            if letra in valido:
                return letra
            else:
                print("¡Letra no válida! Solo se permite (S/N). Intenta de nuevo.")
        except ValueError:
            print("¡Esa no es una letra válida! Intenta de nuevo.")
    
def obtener_numero():
    while True:
        entrada = input("Ingresa un número: ")

        # Intentamos convertir la entrada a un número
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("¡Eso no es un número válido! Intenta de nuevo.")

def obtener_opcion():
    numeros_validos = {1, 2, 3, 4}

    while True:
        entrada = input("ingrese su opcion AQUI: ")

        try:
            numero = int(entrada)
            if numero in numeros_validos:
                return numero
            else:
                print("¡Opcion no válida! Solo se aceptan los números 1, 2, 3 y 4. Intenta de nuevo.")
        except ValueError:
            print("¡Eso no es un número válido! Intenta de nuevo.")

    
def Opciones():
    print("Eliga lo que quieres hacer")
    print("1) Agregar numeros")
    print("2) Buscar elemento")
    print("3) Ordenar lista")
    print("4) Salir")
    opcion = obtener_opcion()
    return opcion
    
def Agreg_Numeros(gui):
    print("ingrese el largo para su lista")
    largo = obtener_numero()
    print("Ingrese elementos de su lista")
    for i in range(largo):
        elemento = obtener_numero()
        Mi_lista.Agregar(elemento, gui)
        print(Mi_lista.Milista)
        
root = tk.Tk()
root.title("Visualización de Lista")
Mi_lista = Listas(root)  # Primero instancia Mi_lista
gui = ListasGUI(root, Mi_lista)  # Luego instancia ListasGUI

Running = True
        
while Running:
    iniciar_interfaz()  # Si deseas iniciar la interfaz cada vez
    opcion = Opciones()
    if opcion == 1:
        Agreg_Numeros(gui)
        print(Mi_lista.Milista)
    elif opcion == 2:
        BuscarN = int(input("Ingrese el numero a buscar: "))
        print(Mi_lista.Buscar(BuscarN))
    elif opcion == 3:
        Mi_lista.Ordenar(gui)
    elif opcion == 4:
        Running = False

root.mainloop()