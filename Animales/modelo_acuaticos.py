from modelo_animal import Animal

class Acuaticos(Animal):
    def __init__(self, data_nombre, data_edad, data_habitat, data_dieta, data_tamano, data_color, tipo_respiracion):
        super().__init__(data_nombre, data_edad, data_habitat, data_dieta, data_tamano, data_color)
        self.respiracion = tipo_respiracion

# ==========================================
# ?          Metodos         
# ==========================================
    def comunicarse(self):
        mensaje = f"El {self.nombre} se esta comunicando por medio de ultra sonidos que viajan por el agua"
        return mensaje
    
    def moverse(self):
        mensaje = f"El {self.nombre} esta nadando por el agua"
        return mensaje
    
    def respirar(self):
        mensaje = f"El {self.nombre} salio a la superficie a respirar"
        return mensaje