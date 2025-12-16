class Base_Datos:
    def __init__(self):
        # Esta lista vacía será nuestro "almacén" de datos
        self.lista_botellas = []

    # ==========================================
    # C Crear (Guardar el objeo)
    # ==========================================
    def guardar_botella(self, nueva_botella):
        self.lista_botellas.append(nueva_botella)
        print("✅ Botella guardada exitosamente.")

    # ==========================================
    # R Read (Mostrar)
    # ==========================================
    def listar_botellas(self):
        print("\n--- BOTELLAS ---")
        if len(self.lista_botellas) == 0:
            print(" (La base de datos está vacía) ")
        else:
            for obj_botella in self.lista_botellas:
                print(obj_botella.imprimir_datos())

    # ==========================================
    # U - Ubdate (Modificar o actualizar objeto)
    # ==========================================
    def actualizar_botella(self, codigo_buscar, nuevo_material, nueva_capacidad):
        encontrado = False #Variable iniciadora para sabe si se encuentra
        
        for obj_botella in self.lista_botellas:
            if obj_botella.codigo == codigo_buscar:
                obj_botella.material = nuevo_material
                obj_botella.capacidad = nueva_capacidad
                print(f" Botella {codigo_buscar} actualizada correctamente.")
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró una botella con el código {codigo_buscar}")

    # ==========================================
    # D - Delete (Eliminar objeto)
    # ==========================================
    def eliminar_botella(self, codigo_buscar):
        botella_a_eliminar = None #Variable inicializadora

        for obj_botella in self.lista_botellas:
            if obj_botella.codigo == codigo_buscar:
                botella_a_eliminar = obj_botella
                break

        if botella_a_eliminar:
            self.lista_botellas.remove(botella_a_eliminar)
            print(f"🗑️ Botella {codigo_buscar} eliminada del sistema.")
        else:
            print(f"No se puede eliminar. El código {codigo_buscar} no existe.")