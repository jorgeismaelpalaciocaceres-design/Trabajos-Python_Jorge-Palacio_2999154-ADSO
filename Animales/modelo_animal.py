from abc import ABC, abstractmethod

#!Abstracción Formal ABC (Abstract Base Classes) Clase Base o Padre
class Animal(ABC):
    #? Constructor
    def __init__(self, data_nombre, data_edad, data_habitat, data_dieta, data_tamano, data_color):
        self.nombre = data_nombre
        #! Atributo privado
        self.__edad = data_edad
        self.habitat = data_habitat
        self.dieta = data_dieta
        self.tamano = data_tamano
        self.color = data_color

# ==========================================
# ?          Gets y Sets      
# ==========================================

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, nueva_edad):
        if(nueva_edad > 5):
            self.__edad = nueva_edad
            mensaje = f"Edad de {self.nombre} actualizada con exito!" 
        else:
            mensaje = "La edad no puede ser menor a 5"
        return mensaje
    
# ==========================================
# ?          Metodos         
# ==========================================

    #! Metodo Contrato
    @abstractmethod 
    def comunicarse(self):
        pass

    def moverse(self):
        mensaje = f"El {self.nombre} se esta desplazando por su habitad"
        return mensaje

    def alimentarse(self):
        mensaje = f"EL {self.nombre} se esta alimentando"
        return mensaje
    
    def reproducirse(self):
        mensaje = f"El {self.nombre} se esta reproduciendo con otro ejemplar de su misma especie"
        return mensaje
    
    def adaptarse(self):
        mensaje = f"El {self.nombre} se esta adaptando a su entorno cambiante"
        return mensaje
    
    def descansar(self):
        mensaje = f"El {self.nombre} esta descansando"
        return mensaje
    
    def dormir(self):
        mensaje = f"El {self.nombre} esta durmiendo"
        return mensaje
