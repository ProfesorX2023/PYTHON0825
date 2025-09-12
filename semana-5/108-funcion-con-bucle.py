def contar_letras(palabra):
    contador = 0
    for letra in palabra:
        print(letra)
        contador += 1

    return contador

print(contar_letras("Python"))