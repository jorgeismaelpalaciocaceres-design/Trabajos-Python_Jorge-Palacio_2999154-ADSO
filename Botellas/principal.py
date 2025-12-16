from modelo_botella import Botella
from modelo_botella_plastico import Botella_Plastico 
from base_de_datos import Base_Datos

# ==========================================
# ?          Código principal          
# ==========================================

"""
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
"""

# ==========================================
# !          Codigo principal CRUD
# ==========================================

bd = Base_Datos()

# --- 1. CREATE (Crear) ---
b1 = Botella("Vidrio", "1L", "Cilíndrica", "Transparente", 101)
b2 = Botella("Plástico", "500ml", "Cuadrada", "Azul", 102)
b3 = Botella("Metal", "750ml", "Cilíndrica", "Gris", 103)

bd.guardar_botella(b1)
bd.guardar_botella(b2)
bd.guardar_botella(b3)

# --- 2. READ (Mostrar) ---
bd.listar_botellas()

# --- 3. UPDATE (Actualizar) ---
print("Actualizando botella 102")
bd.actualizar_botella(102, "Plástico Reciclado", "600ml")
bd.listar_botellas()

# --- 4. DELETE (Eliminar) ---
print("Eliminando botella 101")
bd.eliminar_botella(101)
bd.listar_botellas()

