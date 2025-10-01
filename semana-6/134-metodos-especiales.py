class Libro:
    def __init__(self, autor, titulo, paginas):
        self.autor = autor
        self.titulo = titulo
        self.paginas = paginas

    def __str__(self):

        return f"Titulo '{self.titulo}'\nEscrito por: {self.autor}'"

    def __len__(self):
        return self.paginas

libro_1 = Libro("Stephen King","Cujo",1074)
print(str(libro_1))
print(len(libro_1))