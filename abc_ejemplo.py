from abc import ABC, abstractmethod # 1. Importamos

class MoldePadre(ABC): # 2. Heredamos de ABC
    
    @abstractmethod # 3. Decoramos el método obligatorio
    def metodo_obligatorio(self):
        pass # 4. No ponemos código, solo 'pass'