from modelo_botella import Botella
from modelo_botella_plastico import Botella_Plastico 

# ==========================================
# ?          Código principal          
# ==========================================

print("--- PRUEBA DE LA BOTELLA GENÉRICA ---")
# 1. Creamos una botella normal
object_botella = Botella("Vidrio", "1 Litro", "Cilíndrica")

# 2. Usamos sus métodos
print(f"Material de la botella: {object_botella.get_material()}")
object_botella.contener_liquido("Agua")


print("\n--- PRUEBA DE LA BOTELLA DE PLÁSTICO ---")
# 3. Creamos una botella de plástico (Hija)
# Necesita 5 datos: Material, Capacidad, Forma, Color, Tamaño
objeto_plastico = Botella_Plastico("Plástico", "600ml", "Ergonómica", "Azul", "Mediana")

# 4. Imprimimos todos sus datos
objeto_plastico.imprimir_datos()