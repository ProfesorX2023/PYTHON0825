#Unión, Intersección, Diferencia, Diferencia simétrica
conjunto_1 = {1,2,3,6,7,8,9}
conjunto_2 = {2,4,6,8,10,12,14}
print(f"Union de Conjuntos {conjunto_1.union(conjunto_2)}")
print(f"Insersección de Conjuntos {conjunto_1.intersection(conjunto_2)}")
print(f"Diferencia de conjuntos {conjunto_1.difference(conjunto_2)}")
print(f"Diferencia Simétrica de conjuntos {conjunto_1.symmetric_difference(conjunto_2)}")
print(f"Insersección de Conjuntos {conjunto_2.difference(conjunto_1)}")