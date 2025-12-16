from abc import ABC, abstractmethod

#! Clase Base o Padre
class Animal(ABC):
    #? Agregamos 'dato_id' al inicio del constructor
    def __init__(self, dato_id, data_nombre, data_edad, data_habitat, data_dieta, data_tamano, data_color):
        self.id = dato_id   
        self.nombre = data_nombre
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
        if int(nueva_edad) > 0: # Validación simple
            self.__edad = nueva_edad
            return "Edad actualizada"
        return "Edad no válida"

    # ==========================================
    # ?          Metodos Generales
    # ==========================================
    # Método para listar en el CRUD
    def obtener_info_basica(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Edad: {self.__edad} | Hábitat: {self.habitat}"

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
