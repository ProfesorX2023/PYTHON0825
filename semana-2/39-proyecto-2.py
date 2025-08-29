nombre = input("¿Cuál es tu nombre?")
ventas = float(input("¿A cuanto asicende el monto de tus ventas?"))
comision = ventas*13/100
total = comision + ventas
print(f"El total de comisiones de tus ventas es Q. {round(comision,2)}\nEl total devengado es Q. {round(total,2)}")