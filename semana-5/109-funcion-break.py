#lista = [3,5,7,9,12,15,17] divisor = 4

def primer_divisible(lista, divisor):
    for num in lista:
        if num % divisor == 0:
            return num

    return None

print(primer_divisible([3,5,7,9,12,15,17], 4))