class Base_Datos:
    def __init__(self):
        self.lsita_botellas = []
        self.lista_plastico = []

    def guardar_objeto(self, nuevo_obj):
        self.lsita_botellas.append(nuevo_obj)

    def guerdar_varios_objetos(self, lista_nueva):
        self.lista_plastico.extend(lista_nueva)

    def imprimir_info(self):
        for obj in self.lsita_botellas:
            print(obj.get_material())
