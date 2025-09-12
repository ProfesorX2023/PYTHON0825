def devolver_distintos(a, b, c):
    suma = a + b + c
    lista = [a, b, c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        return sorted(lista)[1]

print(devolver_distintos(4,1,8))