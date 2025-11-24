from modelo_botella import Botella

class Botella_Plastico(Botella):
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_color, dato_tamano):
        # Aquí llamamos al constructor del Padre (Botella)
        super().__init__(dato_material, dato_capacidad, dato_forma)
        # Y aquí agregamos lo nuevo exclusivo de la botella de plástico
        self.color = dato_color
        self.tamano = dato_tamano

    def imprimir_datos(self):
        # Traemos los datos del padre
        dato_mensaje = super().imprimir_datos() 
        # Le sumamos los datos nuevos
        mensaje = f"{dato_mensaje} - Color: {self.color} - Tamaño: {self.tamano}"
        return mensaje

