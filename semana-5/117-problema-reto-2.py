def letras_unicas(palabra):

    lista = list(set(palabra))
    return sorted(lista)

print(letras_unicas("entretenido"))