class Botella:
    def __init__(self, dato_material, dato_capacidad, dato_forma):
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        
    def contener_liquido(self, dato_liquido):
        mensaje = f"Se almaceno solo : {dato_liquido} -  Con una capacidad de : {self.capacidad}"
        return mensaje
    
# ==========================================
# ?          Gets y Sets         
# ==========================================

    def get_material(self):
        return self.material
    
    def set_material(self, dato_material):
        self.material = dato_material

    def imprimir_datos(self):
        mensaje = f"Nombre del material : {self.material} - Capacidad : {self.capacidad}"
        return mensaje