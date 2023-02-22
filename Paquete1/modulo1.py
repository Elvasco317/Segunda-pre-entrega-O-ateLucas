from mclients1 import Cliente

from mclients1 import Compra

cliente1 = Cliente("Jose Mariotta", 36, "josemariotta@gmail.com", "3492325412")
compra1 = Compra(cliente1, "GoPro Hero 7 Black", 545, 1)


print(compra1.calcular_total())

compra1.agregar_cantidad(2)

print(cliente1)

print(compra1)