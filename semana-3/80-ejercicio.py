"""
Ejercicio
Los mayores de edad pueden beber
Los mayores pueden entrar
Los mayores de 30 no pueden entrar a discotecas
Los de 20 y 25 tienen entrada gratis
"""
diccionario = {True:"Sí",False:"No"}
edad = int(input("Ingrese su edad: "))
print(f"Puede beber {diccionario[edad>=18]}")
print(f"Puede entrar {diccionario[edad>=18 and edad<=30]}")
print(f"Tiene entrada grátis: {diccionario[edad==20 or edad==25]}")