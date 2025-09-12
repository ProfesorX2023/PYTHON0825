def precio_sin_iva(precio):
    return precio *0.88

def calcular_total(precio, cantidad):
    return precio_sin_iva(precio) * cantidad

print(calcular_total(100, 3))