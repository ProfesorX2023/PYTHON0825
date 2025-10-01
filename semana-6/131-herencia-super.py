class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Admin(Usuario):
    def __init__(self, nombre, nivel):
        super().__init__(nombre)
        self.nivel = nivel

root_1 = Admin("root 1",10)
root_2 = Admin("root 2",5)
usuario_1 = Usuario("Luis")
print(root_1.nombre, root_1.nivel)
print(root_2.nombre, root_2.nivel)

