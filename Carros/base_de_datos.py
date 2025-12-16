class BaseDatosCarros:
    def __init__(self):
        self.lista_vehiculos = [] # Aquí guardaremos todos los carros

    # ==========================================
    # C - CREATE
    # ==========================================
    def guardar_vehiculo(self, vehiculo):
        if self.buscar_vehiculo(vehiculo.id):
            print(f"Ya existe un vehículo con el ID {vehiculo.id}")
        else:
            self.lista_vehiculos.append(vehiculo)
            print(f"Vehículo {vehiculo.modelo} guardado exitosamente.")

    # ==========================================
    # R - READ
    # ==========================================
    def listar_todos(self):
        print("\n--- CONCESIONARIO (LISTA DE VEHÍCULOS) ---")
        if not self.lista_vehiculos:
            print("(El garaje está vacío)")
        else:
            for carro in self.lista_vehiculos:
                print(carro.info_basica())
        print("------------------------------------------\n")

    def buscar_vehiculo(self, id_buscar):
        for carro in self.lista_vehiculos:
            if carro.id == id_buscar:
                return carro
        return None

    # ==========================================
    # U - UPDATE
    # ==========================================
    def actualizar_vehiculo(self, id_buscar, nuevo_color, nueva_placa):
        vehiculo_encontrado = self.buscar_vehiculo(id_buscar)

        if vehiculo_encontrado:
            vehiculo_encontrado.color = nuevo_color
            mensaje_placa = vehiculo_encontrado.set_placa(nueva_placa)
            
            print(f"Actualización del ID {id_buscar}: Color cambiado a {nuevo_color}. {mensaje_placa}")
        else:
            print(f"Vehículo con ID {id_buscar} no encontrado.")

    # ==========================================
    # D - DELETE
    # ==========================================
    def eliminar_vehiculo(self, id_buscar):
        vehiculo_encontrado = self.buscar_vehiculo(id_buscar)

        if vehiculo_encontrado:
            self.lista_vehiculos.remove(vehiculo_encontrado)
            print(f"El vehículo {vehiculo_encontrado.modelo} ha sido eliminado.")
        else:
            print(f"No se puede eliminar. ID {id_buscar} no existe.")