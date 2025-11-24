from modelo_carro import Carro

class Bus(Carro):
    def __init__(self, dato_modelo, dato_color, dato_motor, dato_capacidad):
        super().__init__(dato_modelo, dato_color, dato_motor)
        self.capacidad = dato_capacidad

    def recoger_pasajeros(self, dato_cantidad_pasajeros):
        if (dato_cantidad_pasajeros < self.capacidad):
            mensaje = f"El bus tipo ({self.modelo}) regio {dato_cantidad_pasajeros} pasajeros!"
        else:
            mensaje = f"Excede la capacidad del Bus:{self.modelo} que es de {self.capacidad}"
        return mensaje