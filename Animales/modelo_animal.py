class Animal():
    #? Constructor
    def __init__(self, data_nombre, data_edad, data_habitad, data_dieta, data_tamano, data_color):
        self.nombre = data_nombre
        #! Atributo privado
        self.__edad = data_edad
        self.habitad = data_habitad
        self.dieta = data_dieta
        self.tamano = data_tamano
        self.color = data_color

# ==========================================
# ?          Gets y Sets      
# ==========================================

    def get(self):
        return self.__edad
    
    def set(self, nueva_edad):
        if(nueva_edad > 5):
            self.__edad = nueva_edad
            mensaje = f"Edad de {self.nombre} actualizada con exito!" 
        else:
            mensaje = "La edad no puede ser menor a 5"
        return mensaje
    
# ==========================================
# ?          Metodos         
# ==========================================

    def moverse(self):
        mensaje = f"El {self.nombre} se esta desplazando por su habitad"
        return mensaje

    def alimentarse(self):
        mensaje = f"EL {self.nombre} se esta alimentando"
        return mensaje
    
    def comunicarse(self):
        mensaje = f"El {self.nombre} se esta comunicando como lo hace habitualmente su especie"
        return mensaje
    
    def reproducirse(self):
        mensaje = f"El {self.nombre} se esta reproduciendo con otro ejemplar de su misma especie"
        return mensaje
    
    def adaptarse(self):
        mensaje = f"El {self.nombre} se esta adaptando a su entorno cambiante"
        return mensaje
    
    def descansar(self):
        meensaje = f"El {self.nombre} esta descansando"
        return meensaje
    
    def dormir(self):
        mensaje = f"El {self.nombre} esta durmiendo"
        return mensaje
