class Botella:
    def __init__(self, dato_material, dato_capacidad, dato_forma):
        # Atributos (Características)
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        
    # Método (Acción)
    def contener_liquido(self, dato_liquido):
        mensaje = f"Se almacenó solo: {dato_liquido} - Con una capacidad de: {self.capacidad}"
        return mensaje
    
    # Getters y Setters (Para obtener o cambiar valores)
    def get_material(self):
        return self.material
    
    def set_material(self, dato_material):
        self.material = dato_material

    def imprimir_datos(self):
        mensaje = f"Material: {self.material} - Capacidad: {self.capacidad} - Forma: {self.forma}"
        return mensaje
    