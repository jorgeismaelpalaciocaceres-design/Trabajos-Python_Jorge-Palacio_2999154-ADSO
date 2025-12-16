class Botella:
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_color, dato_codigo):
        # Atributos (Características)
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.color = dato_color

    #? Getters y Setters (Para obtener o cambiar valores)
    def get_material(self):
        return self.material
    
    def set_material(self, dato_material):
        self.material = dato_material

    def get
        
# ==========================================
# ?          Metodos         
# ==========================================

    def contener_liquido(self, dato_liquido):
        mensaje = f"Se almacenó solo: {dato_liquido} - Con una capacidad de: {self.capacidad}"
        return mensaje

    def imprimir_datos(self):
        mensaje = f"Material: {self.material} - Capacidad: {self.capacidad} - Forma: {self.forma}"
        return mensaje
    
    def transportar(self):
        mensaje = f"La botella de {self.material} esta siendo transportada"
        return mensaje
    
    def reutilizar(self):
        mensaje = f"La botella {self.material} esta ciendo reciclada y reutilizada"
        return mensaje
    
    def verificar_compatibilidad(self):
        if self.material == "Vidrio":
            mensaje = f"La botella de {self.material} es resistente al calor y al frio"
        elif self.material == "Plastico"
            mensaje = f"La botellas de {self.material} es resistente al frio pero no al calor"
        return mensaje
    
    def imprimit_info(self):
        print(f"EL material es: {self.material}")
        print(f"EL material es: {self.forma}")
        
            