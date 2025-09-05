productos = ["Teclado","Mouse","Pantalla"]
productos.append("Case")
precios = [150,99,1200,800]
for proudcto,precio in zip(productos,precios):
    print(f"{proudcto}: Q.{precio}")