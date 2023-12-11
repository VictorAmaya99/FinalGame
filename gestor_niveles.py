import json

import json

# Clase para representar un nivel
class Nivel:
    def __init__(self, world_data, tile_size):
        self.world_data = world_data
        self.tile_size = tile_size

# Gestor de niveles que maneja la información de los niveles y los guarda/carga desde un archivo JSON
class GestorNiveles:
    def __init__(self):
        self.niveles = {}  # Diccionario para almacenar la información de los niveles

    def agregar_nivel(self, nombre_nivel, nivel):
        # Guardar la información del nivel en el diccionario
        self.niveles[nombre_nivel] = {
            'world_data': nivel.world_data,
            'tile_size': nivel.tile_size,
            # Puedes agregar más datos relevantes del nivel aquí
        }

    def guardar_partida(self, nombre_archivo):
        # Guardar la información de los niveles en un archivo JSON
        with open(nombre_archivo, 'w') as archivo:
            json.dump(self.niveles, archivo)

    def cargar_partida(self, nombre_archivo):
        # Cargar la información de los niveles desde un archivo JSON
        with open(nombre_archivo, 'r') as archivo:
            self.niveles = json.load(archivo)

