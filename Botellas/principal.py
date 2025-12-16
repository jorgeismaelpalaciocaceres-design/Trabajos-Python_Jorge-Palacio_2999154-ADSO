from modelo_botella import Botella
from modelo_botella_plastico import Botella_Plastico 
from base_de_datos import Base_Datos

# ==========================================
# ?          Código principal          
# ==========================================

print("--- PRUEBA DE LA BOTELLA GENÉRICA ---")
# 1. Creamos una botella normal
object_botella = Botella("Vidrio", "1 Litro", "Cilíndrica")
# 2. Usamos sus métodos
print(f"Material de la botella: {object_botella.get_material()}")
mensaje = object_botella.contener_liquido("Agua")
print(mensaje)


print("\n--- PRUEBA DE LA BOTELLA DE PLÁSTICO ---")
# 3. Creamos una botella de plástico (Hija)
# Necesita 5 datos: Material, Capacidad, Forma, Color, Tamaño
objeto_plastico = Botella_Plastico("Plástico", "600ml", "Ergonómica", "Azul", "Mediana")
# 4. Imprimimos todos sus datos
mensjae2 = objeto_plastico.imprimir_datos()
print(mensjae2)


#! Codigo principal CRUD
#? 1.Crear el objeto

obj_base_datos = Base_Datos()
material = input("ingrese el material: ")
material = input("ingrese el material: ")
obj_botella = Botella(material)

obj_base_datos.guardar_objeto(obj_botella)

