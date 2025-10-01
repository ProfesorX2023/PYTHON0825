class Animal:
    vivo = True

    def hablar(self):
        print("sonido por defecto")

class Perro(Animal):
    pass

perro_1 = Perro()
perro_1.hablar()
animal_1 = Animal()
animal_1.hablar()
print(perro_1.vivo)