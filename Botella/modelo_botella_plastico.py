from modelo_botella import Botella

class Botella_Plastico(Botella):
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_color, dato_tamano):
        super().__init__(dato_material, dato_capacidad, dato_forma)
        self.color = dato_color
        self.tamano = dato_tamano

    def imprimir_datos(self):
        dato_mensaje = super().imprimir.datos()
        mensaje = dato_mensaje + f"Color es : {self.color} - Tamaño : {self.tamano}"
        print(mensaje)


