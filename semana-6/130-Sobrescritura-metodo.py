class Animal:
    vivo = True

    def hablar(self):
        print('Sonido por defecto')

class Gato(Animal):

    def hablar(self):
        print('miau!')

animal_1 = Animal()
gato_1 = Gato()
animal_1.hablar()
gato_1.hablar()