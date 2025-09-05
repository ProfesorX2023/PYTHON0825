#input y nombre por default
#instrucciones
#variables maximo=100 y minimo=1
#intentos vidas=8
#Necesitamos Random para obtener un número entre 1 y 100
#Contador intentos
#while para hacer que el juego funcione mientras tenga vidas
#if para verificar si acerto o no

#bibliotecas con funcionaes especiales
from random import randint

#Saludo e inicio del juego
nombre = input("¿Cuál es tu nombre?: ")
print(f"Bueno, {nombre}, he pensado en un número entre 1 y 100.")
print("Tienes solo 8 intentos para adivinarlo")

#numero secreto aleatorio
numero_secreto = randint(1,100)
intentos = 0
vidas = 0
max_intentos = 8

#ciclo de intentos
while vidas < max_intentos:
    intento = int(input("Ingresa un valor entre 1 y 100: "))
    if intento <1 or intento>100:
        print("Numero no permitido")
    elif intento < numero_secreto:
        print("Incorreccto, el número secreto es mayor")
    elif intento > numero_secreto:
        print("Incorrecto, número secreto es menor")
    else:
        print(f"Haz, Ganado el número era {numero_secreto}")
        break

    vidas += 1