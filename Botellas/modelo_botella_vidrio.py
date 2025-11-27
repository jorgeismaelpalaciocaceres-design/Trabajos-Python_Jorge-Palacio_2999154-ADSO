from modelo_botella import Botella

class Botella_Vidrio(Botella):
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_siseño, dato_grabado):
        super().__init__(dato_material, dato_capacidad, dato_forma)
        self.diseño = dato_siseño
        self.grabado = dato_grabado


# ==========================================
# ?          Metodos         
# ==========================================

    def reutilizar(self):
        mensaje = f"La botella de {self.material} esta siendo llevada a un punto de recolección de notella de plastico para ser recicladas"    
        return mensaje
    