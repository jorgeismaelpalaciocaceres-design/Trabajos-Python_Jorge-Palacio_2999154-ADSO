from modelo_animal import Animal
from modelo_carnivoros import Carnivoros


# ==========================================
# ?          Código principal          
# ==========================================

#* 1. Creación de un animal
objeto_animal1 = Animal("Gato", "6", "Terrestre", "Omnívoro", "Pequeño-Mediano", "Naranja")
#! El animal se está moviendo
print(objeto_animal1.moverse())
#! El animal se está alimentando
print(objeto_animal1.alimentarse())
#! El animal se está comunicando
print(objeto_animal1.comunicarse())
#! El animal se está reproduciendo
print(objeto_animal1.reproducirse())
#! El animal se está adaptando a su entorno
print(objeto_animal1.adaptarse())
#! El animal está descansando
print(objeto_animal1.descansar())
#! El animal está durmiendo
print(objeto_animal1.dormir())

#* 2. Creación de un animal carnivoro
objeto_carnivoro1 = Carnivoros("León", "15", "Terrestre", "Carnivoro", "Medioano-Grande", "Amarillo")
#! Instinto al tener habre de los carnivoros a cazar
print(objeto_carnivoro1.cazar())
#? Get de su atributo privado
print(objeto_carnivoro1.get())
#? Set (Modificación) de su atrubuto privado
print(objeto_carnivoro1.set(8))
#? Verificación de modificación de edad (Atributo privado)
print(objeto_carnivoro1.get())