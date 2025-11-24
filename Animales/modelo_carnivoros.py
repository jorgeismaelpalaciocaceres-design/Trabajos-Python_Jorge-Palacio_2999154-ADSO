from modelo_animal import Animal

class Carnivoros(Animal):
    #? Constructor
    def __init__(self, data_nombre, data_edad, data_habitad, data_dieta, data_tamano, data_color):
        super().__init__(data_nombre, data_edad, data_habitad, data_dieta, data_tamano, data_color)

# ==========================================
# ?          Metodos         
# ==========================================

    #! Instinto
    def cazar(self):
        mensaje = f"El {self.nombre} Empieza a cazar al tener hambre"
        return mensaje