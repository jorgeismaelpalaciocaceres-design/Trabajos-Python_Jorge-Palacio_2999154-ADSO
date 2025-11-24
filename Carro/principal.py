from modelo_carro import Carro
from modelo_bus import Bus

# ==========================================
# ?          Código principal          
# ==========================================

# 1. Creamos un carro
objeto_carro1 = Carro("Toyota", "Rojo", "V8")
arrancar_carro1 = objeto_carro1.arrancar()
print(arrancar_carro1)

acelerar_carro1 = objeto_carro1.acelerar(120)
print(acelerar_carro1)

#2. Creamos un Bus
objeto_bus1 = Bus("Escolar",