class Carro:
    #? CONSTRUCTOR
    def __init__(self, dato_modelo, dato_color, dato_motor):
        self.modelo = dato_modelo
        self.color = dato_color
        self.motor = dato_motor

    #? METODOS
    def arrancar(self):
        mensaje = f"El carro: {self.modelo} esta arrancando su motor: {self.motor}"
        return mensaje
    
    def acelerar(self, dato_velocidad):
        mensaje = f"El carro: {self.modelo} esta acelerando hsta llegar auna velocidad de >> {dato_velocidad} k/h"
        return mensaje