from modelo_carro import Carro

class Bus(Carro):
    def __init__(self, dato_modelo, dato_color, dato_motor, dato_capacidad):
        super().__init__(dato_modelo, dato_color, dato_motor)
        self.capacidad = dato_capacidad

    def recoger_pasajeros(self, dato_cantidad_pasajeros):
        mensaje = f"La camioneta: {self.modelo} regio {dato_cantidad_pasajeros}!"
        return mensaje