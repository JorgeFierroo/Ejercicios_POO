class Playlist:
    def __init__(self):
        self.canciones = []
        self.nombre = None
        self.estado = "pausada"
        self.indice = None

    def anadir_canciones(self,nombre):
        self.canciones.append(nombre)

    def display_songs(self):
        """Mostrar todas las canciones en la lista de reproducción."""
        if not self.canciones:
            print("La lista de reproducción está vacía.")
        else:
            print("Lista de Canciones:")
            for index, song in enumerate(self.canciones, start=1):
                print(f"{index}. {song}")


mi_playlist = Playlist()
mi_playlist.anadir_canciones("duality")
mi_playlist.display_songs()
