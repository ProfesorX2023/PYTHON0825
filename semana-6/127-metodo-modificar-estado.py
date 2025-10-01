class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1

contador_1 = Contador()
contador_1.incrementar()
print(contador_1.valor)
contador_1.incrementar()
print(contador_1.valor)
contador_1.incrementar()
print(contador_1.valor)
print(contador_1.valor)
print(contador_1.valor)
contador_1.incrementar()

print(contador_1.valor)