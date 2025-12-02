from modelo_animal import Animal

class Insectos(Animal):
    def __init__(self, data_nombre, data_edad, data_habitat, data_dieta, data_tamano, data_color, dato_tipo_insecto, dato_numero_patas):
        super().__init__(data_nombre, data_edad, data_habitat, data_dieta, data_tamano, data_color)
        self.tipo = dato_tipo_insecto
        self.numero = dato_numero_patas

# ==========================================
# ?          Metodos         
# ==========================================

    def comunicarse(self):
        mensaje = f"El {self.tipo} {self.nombre} se esta comunicando por medio de feromonas sonidos y danzas"
        return mensaje
