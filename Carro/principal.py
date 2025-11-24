from modelo_carro import Carro
from modelo_bus import Bus
from modelo_deportivo import Deportivo

# ==========================================
# ?          Código principal          
# ==========================================

#* 1. Creamos un carro
objeto_carro1 = Carro("Toyota", "Rojo", "V8")
arrancar_carro1 = objeto_carro1.arrancar()
#! Arrancamos
print(objeto_carro1.arrancar())
#! Aceleramos 
print(objeto_carro1.aceleraracion("Acelerar"))
#! Manejamos la dirección 
print(objeto_carro1.direccion("Derecha"))
#! Encendemos las luces 
print(objeto_carro1.luces("Encender"))

#* 2. Creamos un Bus 
objeto_bus1 = Bus("Escolar", "Amarillo", "Cummins L9 e ISB6.7 G", 72)
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
objeto_deportivo1 = Deportivo("Porsche 911 Carrera S (992)", "Rojo Guardia", "Motor bóxer de 6 cilindros", "2 puertas", "Gasolina")
#! Encender el aire
print(objeto_deportivo1.encender_aire("Encender"))
#! Chequear seguridad
print(objeto_deportivo1.chequear_seguridad("Si"))
#! Ajustar espejos
print(objeto_deportivo1.ajustar_espejos())

