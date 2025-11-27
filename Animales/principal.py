from modelo_animal import Animal
from modelo_reptiles import Reptiles
from modelo_mamiferos_terrestres import Mamiferos_Terrestrs
from modelo_insectos import Insectos
from modelo_acuaticos import Acuaticos


# ==========================================
# ?          Código principal          
# ==========================================

#* 1. Creación de un mamifero terrestre
objeto_gato1 = Mamiferos_Terrestrs("GatoFelix", "6", "Terrestre", "Omnívoro", "Pequeño-Mediano", "Naranja", "Placentario", "Femenino")
#! El animal se está moviendo
print(objeto_gato1.moverse())
#! El animal se está alimentando
print(objeto_gato1.alimentarse())
#! El animal se está comunicando
print(objeto_gato1.comunicarse())
#! El animal se está reproduciendo
print(objeto_gato1.reproducirse())
#! El animal se está adaptando a su entorno
print(objeto_gato1.adaptarse())
#! El animal está descansando
print(objeto_gato1.descansar())
#! El animal está durmiendo
print(objeto_gato1.dormir())
#! El animal esta tieniendo un parto
print(objeto_gato1.tener_un_hijo_por_parto())

#* 2. Creación de un reptil
objeto_cocodrilo = Reptiles("Crocodic", "15", "Terrestre", "Carnivoro", "Medioano-Grande", "Albino", "Alligatoridae")
#! Instinto al tener habre de los carnivoros a cazar
print(objeto_cocodrilo.cazar())
#? Get de su atributo privado
print(objeto_cocodrilo.get_edad())
#? Set (Modificación) de su atrubuto privado
print(objeto_cocodrilo.set_edad(8))
#? Verificación de modificación de edad (Atributo privado)
print(objeto_cocodrilo.get_edad())

#* Creación de un insecto
objeto_mari = Insectos("Mariquita", "1 año", "Campor y bosques", "Carnivora", "Pequeño", "Rojo y negro", "Escarabajo", "6 patas")
#! El animal se esta comunicando
print(objeto_mari.comunicarse())

#* creación de un acuatico
objeto_acuatico1 = Acuaticos("Delfin", "20", "Oceanos y mares", "Carnivoro", "Mediano", "Gris", "Respiración pulmonar")
#! El animal se esta comunicando
print(objeto_acuatico1.comunicarse())
#! El animal se esta moviendo
print(objeto_acuatico1.moverse())
#! El animal respirar
print(objeto_acuatico1.respirar())