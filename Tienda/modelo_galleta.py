class Galletas:

    def __init__(self):
        self.color=""
        self.forma=""
        self.tamano=""

    def _asignacion_material(self, dato_color, dato_forma, dato_tamano):
        self.color=dato_color
        self.forma=dato_forma
        self.tamano=dato_tamano
        print(f"Las galletas son de color {self.color}, de forma {self.forma} y de tamaño {self.tamano}.")
    
    def asignacion_material2(self, dato_color, dato_forma, dato_tamano):
        self.color=dato_color
        self.forma=dato_forma
        self.tamano=dato_tamano
        print(f"Las galletas son: {self.color}, {self.forma} y {self.tamano}.")

# ==========================================
# ?          CLASES HIJAS                  
# ==========================================

class Galletas(Galletas):
    def __init__(self):
        super().__init__()
        self.decoracion=""
        self.chispas=""

    def asignacion_decoracion(self):
        super().asignacion_material2("Rojo", "Circular", "Pequeña")
        self.decoracion="Activar"
        self.chispas="Aplicar"
        print(f"Estado Decoracion: {self.decoracion}")
        print(f"Estado Chispas: {self.chispas}")



# ==========================================
# !          CODIGO PRINCIPAL       !
# ==========================================
galleta_chocolate = Galletas() # Instancia de la clase Galletas
galleta_frutosRojos = Galletas()
galleta_vainilla = Galletas()

galleta_frutosRojos.asignacion_material2("Rojo","Circular", "Pequeña")
galleta_vainilla.asignacion_material2("Amarilla", "circular", "Mediana")
