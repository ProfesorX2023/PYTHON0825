def mostrar_atributos(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_atributos(nombre="Ana", edad=25,ciudad="Antigua Guatemala",carrera="Ingeniería")