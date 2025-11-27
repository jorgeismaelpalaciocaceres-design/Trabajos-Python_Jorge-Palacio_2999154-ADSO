from modelo_carro import Carro

class Camion(Carro):
    #?Constructor
    def __init__(self, dato_modelo, dato_color, dato_motor, dato_placa, capacidad_carga):
        super().__init__(dato_modelo, dato_color, dato_motor, dato_placa) 
        self.capacidad_carga = capacidad_carga

      

# ==========================================
# ?          Metodos         
# ==========================================

    def cargar(self, material):
        mensaje = f"El {self.modelo} esta cargando {material} y tiene una capacdad de {self.capacidad_carga}"
        return mensaje 
