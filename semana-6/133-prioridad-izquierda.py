class Padre:
    def trabajo(self):
        print("Trabajo en la construccion")

class Madre:
    def trabajo(self):
        print("Trabajo en el hospital")

class Hija(Padre, Madre):
    pass

amanda = Hija()
amanda.trabajo()