class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

persona_1 = Persona("Luis")
persona_2 = Persona("Jose")
persona_1.saludar()
persona_2.saludar()