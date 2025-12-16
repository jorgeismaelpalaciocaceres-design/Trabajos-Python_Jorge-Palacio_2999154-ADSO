from modelo_carro import Carro
from modelo_transporte_publico import Transporte_Publico
from modelo_deportivo import Deportivo
from modelo_camion import Camion
from base_de_datos import BaseDatosCarros

# ==========================================
# ?          Código principal          
# ==========================================

"""
#* 1. Creamos un carro
objeto_carro1 = Carro("Toyota", "Rojo", "V8","ABC")
arrancar_carro1 = objeto_carro1.arrancar()
#! Arrancamos
print(objeto_carro1.arrancar())
#! Aceleramos 
print(objeto_carro1.aceleraracion("Acelerar"))
#! Manejamos la dirección 
print(objeto_carro1.direccion("Derecha"))
#! Encendemos las luces 
print(objeto_carro1.luces("Encender"))

#* 2. Creamos un Transporte publico
objeto_bus1 = Transporte_Publico("Escolar", "Amarillo", "Cummins L9 e ISB6.7 G", "FKS", 72)
#! Recogemos pasajeros
print(objeto_bus1.recoger_pasajeros(70))
#! Arrancamos el Bus
print(objeto_bus1.arrancar())
#! Aceleramos el Bus
print(objeto_bus1.aceleraracion("Acelerar"))
#! Manejamos la dirección del bus
print(objeto_bus1.direccion("Derecha"))
#! Encendemos las luces del Bus
print(objeto_bus1.luces("Encender"))

#* 3. Creamos un carro deportivo
objeto_deportivo1 = Deportivo("Porsche 911 Carrera S (992)", "Rojo Guardia", "Motor bóxer de 6 cilindros", "LSF", "2 puertas", "Gasolina")
#! Encender el aire
print(objeto_deportivo1.encender_aire("Encender"))
#! Chequear seguridad
print(objeto_deportivo1.chequear_seguridad("Si"))
#! Ajustar espejos
print(objeto_deportivo1.ajustar_espejos())
#? Mostrat atributo privado (Self.__) GET
print(objeto_deportivo1.get_placa())
#? Modificar atributo privado GET
print(objeto_deportivo1.set("DDD"))

#* 4. Creamos un camion
objeto_camion1 = Camion("Chevrolet", "Blanco", "Isuzu", "ADS", "4.510 kg")
#! Cargamos el material
print(objeto_camion1.cargar("Tierra"))
"""
#! Codigo principal CRUD
db = BaseDatosCarros()

print("--- CREANDO VEHÍCULOS ---")
carro1 = Carro(10, "Toyota", "Rojo", "V8", "ABC")
bus1 = Transporte_Publico(20, "Escolar", "Amarillo", "Diesel", "FKS", 72)
deportivo1 = Deportivo(30, "Porsche 911", "Rojo", "Boxer 6", "LSF", "2 puertas", "Gasolina")
camion1 = Camion(40, "Chevrolet", "Blanco", "Isuzu", "ADS", "4.510 kg")

db.guardar_vehiculo(carro1)
db.guardar_vehiculo(bus1)
db.guardar_vehiculo(deportivo1)
db.guardar_vehiculo(camion1)

print("--- LISTANDO (READ) ---")
db.listar_todos()


print("--- 3. ACTUALIZANDO (UPDATE) ---")
db.actualizar_vehiculo(10, "Negro", "XYZ")
db.actualizar_vehiculo(30, "Azul Mate", "PLACA_LARGA") 
db.listar_todos()


print("--- ELIMINANDO ---")
db.eliminar_vehiculo(40)

db.listar_todos()
