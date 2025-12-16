class Carro:
    #? CONSTRUCTOR (Agregamos dato_id al principio)
    def __init__(self, dato_id, dato_modelo, dato_color, dato_motor, dato_placa):
        self.id = dato_id
        self.modelo = dato_modelo
        self.color = dato_color
        self.motor = dato_motor
        #! ATRIBUTO PRIVADO
        self.__placa = dato_placa

    # ==========================================
    # ?          Metodos Nuevos para CRUD
    # ==========================================
    
    def info_basica(self):
        return f"ID: {self.id} | Modelo: {self.modelo} | Placa: {self.__placa} | Color: {self.color}"
    
    #!Getter
    def get_placa(self):
        return self.__placa

    #!Setters
    def set_placa(self, nueva_placa): 
        if(len(nueva_placa) == 3):
            self.__placa = nueva_placa
            mensaje = "Se cambio la placa con exito"
        else:
            mensaje = "La placa debe tener 3 Caracteres"
        return mensaje
    

# ==========================================
# ?          Metodos         
# ==========================================

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

