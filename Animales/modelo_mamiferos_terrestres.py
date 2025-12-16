from modelo_animal import Animal

class Mamiferos_Terrestrs(Animal):
    def __init__(self, dato_id, data_nombre, data_edad, data_habitat, data_dieta, data_tamano, data_color, dato_tipo_mamifero, dato_genero):
        super().__init__(dato_id, data_nombre, data_edad, data_habitat, data_dieta, data_tamano, data_color)
        self.tipo = dato_tipo_mamifero
        self.genero = dato_genero

# ==========================================
# ?          Metodos         
# ==========================================

    #? Metodo obligatorio
    def comunicarse(self):
        mensaje = f"El {self.nombre} se esta por medio de señales visuales por medio de su cuerpo y haciendo sonidos"
        return mensaje

    def tener_un_hijo_por_parto(self):
        mensaje = f"El {self.tipo} {self.genero} esta teniendo un parto" 
        return mensaje