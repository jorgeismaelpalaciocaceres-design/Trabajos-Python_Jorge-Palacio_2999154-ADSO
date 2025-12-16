from modelo_animal import Animal

class Reptiles(Animal):
    #? Constructor
    def __init__(self, dato_id, data_nombre, data_edad, data_habitad, data_dieta, data_tamano, data_color, dato_raza_cocodrilo):
        super().__init__(dato_id, data_nombre, data_edad, data_habitad, data_dieta, data_tamano, data_color)
        self.raza = dato_raza_cocodrilo

# ==========================================
# ?          Metodos         
# ==========================================

    #? Metodo obligatorio
    def comunicarse(self):
        mensaje = f"El {self.nombre} se esta comunicando químicamente atravéz de las feromonas"
        return mensaje

    #! Instinto
    def cazar(self):
        mensaje = f"El {self.nombre} de raza {self.raza} Empieza a cazar al tener hambre"
        return mensaje
    
