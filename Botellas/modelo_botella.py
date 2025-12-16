class Botella:
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_color, dato_codigo):
        # Atributos (Características)
        self.codigo = dato_codigo
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.color = dato_color

    # Gets y Sets
    def get_material(self):
        return self.material
    
    def set_material(self, dato_material):
        self.material = dato_material

    # ==========================================
    #           Metodos         
    # ==========================================

    def contener_liquido(self, dato_liquido):
        return f"Se almacenó solo: {dato_liquido} - Con una capacidad de: {self.capacidad}"

    def imprimir_datos(self):
        # Usamos este método para mostrar la info en el CRUD
        return f"ID: {self.codigo} | Material: {self.material} | Capacidad: {self.capacidad} | Forma: {self.forma} | Color: {self.color}"
    
    def transportar(self):
        return f"La botella de {self.material} esta siendo transportada"
    
    def reutilizar(self):
        return f"La botella {self.material} esta siendo reciclada y reutilizada"
    
    def verificar_compatibilidad(self):
        mensaje = ""
        if self.material == "Vidrio":
            mensaje = f"La botella de {self.material} es resistente al calor y al frio"
        elif self.material == "Plastico": # <--- Corregido: faltaban los dos puntos
            mensaje = f"La botellas de {self.material} es resistente al frio pero no al calor"
        return mensaje