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
    
    def apagar(self):
        mensaje = f"El carro: {self.modelo} se apagó"
        return mensaje
    
    def aceleraracion(self, dato_aceleracion):
        if (dato_aceleracion == "Acelerar"):
            mensaje = f"El carro {self.modelo} esta acelerando"
        elif (dato_aceleracion == "Frenar"):
            mensaje = f"El carro {self.modelo} frenó"
        return mensaje
    
    def direccion(self, dato_direccion):
        if (dato_direccion == "Derecha"):
            mensaje = f"EL auto {self.modelo} esta girando a la derecha"
        elif (dato_direccion =="Izquierda"):
            mensaje = f"EL auto {self.modelo} esta girando a la izquierda"
        else:
            mensaje = "Por favor seleccione una dirección valida"
        return mensaje
    
    def luces(self, dato_luces):
        if(dato_luces == "Encender"):
            mensaje = f"Las luces del carro {self.modelo} estan encendidas"
        elif(dato_luces == "Apagar"):
            mensaje = f"Las luces del carro {self.modelo} estan apagadas"
        else:
            mensaje = "Por favor ingrese un dato valido"
        return mensaje
    
    def ventanas(self, dato_ventanas):
        if(dato_ventanas == "Subir"):
            mensaje = f"Las Ventanas del carro {self.modelo} estan subiendo"
        elif(dato_ventanas == "Bajar"):
            mensaje = f"Las Ventanas del carro {self.modelo} estan bajando"
        else:
            mensaje = "Por favor ingrese un dato valido"
        return mensaje

