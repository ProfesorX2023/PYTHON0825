class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color

    def area(self):
        return self.caras * self.caras * self.caras

class Esfera:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3/4 * 3.1416 * self.radio**3

cubo_1 = Cubo("Azul")
cubo_2 = Cubo("Verde")
cubo_3 = Cubo("Rojo")

esfera_1 = Esfera(5)

print(cubo_1.caras, cubo_1.color)
print(cubo_2.caras, cubo_2.color)
print(cubo_3.caras, cubo_3.color)
print(print(esfera_1.area()))