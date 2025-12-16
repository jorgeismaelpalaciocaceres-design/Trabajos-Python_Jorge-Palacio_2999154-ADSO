from modelo_carro import Carro

class Deportivo(Carro):
    def __init__(self, dato_id, dato_modelo, dato_color, dato_motor, dato_placa, dato_puertas, dato_combustible):
        super().__init__(dato_id, dato_modelo, dato_color, dato_motor, dato_placa)
        self.puertas = dato_puertas
        self.combustible = dato_combustible

# ==========================================
# ?          Metodos         
# ==========================================

    def encender_aire(self, dato_aire):
        if (dato_aire == "Encender"):
            mensaje = f"El aire del carro {self.modelo} esta encendido"
        elif (dato_aire == "Apagado"):
            mensaje =f"El aire del carro {self.modelo} esta apagado"
        else:
            mensaje = "Porfavor ingrese un valor valido -> Encendido o Apagado"
        return mensaje
    
    def chequear_seguridad(self, dato_seguridad):
        if (dato_seguridad):
            mensaje = f"El carro {self.modelo} tiene los Sistemas de seguridad (Airbags, Frenos ABS) activados y listos"
        else:
            mensaje = "Los Sistemas de seguridad (Airbags, Frenos ABS) estan desacitivados"
        return mensaje
    
    def ajustar_espejos(self):
        mensaje =f"Los espejos del carro {self.modelo} estan ajustados"
        return mensaje