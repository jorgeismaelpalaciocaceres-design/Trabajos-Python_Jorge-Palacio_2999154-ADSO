class BaseDatosAnimales:
    def __init__(self):
        self.lista_animales = [] # Nuestra "tabla" de animales

    # ==========================================
    # C - CREATE
    # ==========================================
    def guardar_animal(self, animal):
        if self.buscar_animal(animal.id):
            print(f"Ya existe un animal con el ID {animal.id}")
        else:
            self.lista_animales.append(animal)
            print(f"{animal.nombre} registrado exitosamente.")

    # ==========================================
    # R - READ
    # ==========================================
    def listar_todos(self):
        print("\n--- LISTA DE ANIMALES ---")
        if not self.lista_animales:
            print("(No hay animales registrados)")
        else:
            for animal in self.lista_animales:
                print(animal.obtener_info_basica()) 
        print("-------------------------------------\n")


    def buscar_animal(self, id_buscar):
        for animal in self.lista_animales:
            if animal.id == id_buscar:
                return animal
        return None

    # ==========================================
    # U - UPDATE
    # ==========================================
    def actualizar_animal(self, id_buscar, nuevo_habitat, nueva_edad):
        animal_encontrado = self.buscar_animal(id_buscar)

        if animal_encontrado:
            animal_encontrado.habitat = nuevo_habitat
            animal_encontrado.set_edad(nueva_edad)
            print(f"Datos de {animal_encontrado.nombre} actualizados.")
        else:
            print(f"No se encontró el animal con ID {id_buscar}")

    # ==========================================
    # D - DELETE
    # ==========================================
    def eliminar_animal(self, id_buscar):
        animal_encontrado = self.buscar_animal(id_buscar)

        if animal_encontrado:
            self.lista_animales.remove(animal_encontrado)
            print(f"{animal_encontrado.nombre} ha sido eliminado del registro.")
        else:
            print(f"No se puede eliminar. ID {id_buscar} no existe.")