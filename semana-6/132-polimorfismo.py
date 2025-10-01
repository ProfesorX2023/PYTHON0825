class Ave:

    def volar(self):
        print('ave volando')

class Avion:

    def volar(self):
        print('avion despegando')

ave_1 = Ave()
avion_1 = Avion()
lista = [ave_1, avion_1]

for obj in lista:
    obj.volar()