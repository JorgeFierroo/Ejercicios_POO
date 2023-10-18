class Listas:
    def __init__(self):
        self.Milista = []
        
    def Agregar(self,elemento):
        self.Milista.append(elemento)
        
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
    
    def Ordenar(self):
        n = len(self.Milista)
        if n<1:
            print("//// la lista ya esta ordenada y/o esta vacia ////")
            print(Mi_lista.Milista)
        else:
            for i in range(n):
                for j in range(0, n-i-1):
                    if self.Milista[j]>self.Milista[j+1]:
                        cum = self.Milista[j]
                        self.Milista[j], self.Milista[j+1] = self.Milista[j+1], cum 
                        print(self.Milista)
        return self.Milista
        
        
        
Mi_lista = Listas()
    
    
    
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
    
def Agreg_Numeros():
    print("ingrese el largo para su lista")
    largo = obtener_numero()
    print("Ingrese elementos de su lista")
    for i in range(largo):
        elemento = obtener_numero()
        Mi_lista.Agregar(elemento)
        print(Mi_lista.Milista)
        
Running = True
        
while Running:
    iniciar_interfaz()
    opcion = Opciones()
    if opcion == 1:
        Agreg_Numeros()
        print(Mi_lista.Milista)
    if opcion == 2:
        BuscarN = int(input("Ingrese el numero a buscar: "))
        print(Mi_lista.Buscar(BuscarN))
    if opcion == 3:
        Mi_lista.Ordenar()
    if opcion == 4:
        Running = False