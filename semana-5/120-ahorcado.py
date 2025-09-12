from random import choice

# Función para elegir la palabra al azar
def palabra_al_azar():
    return choice(["chile","calabaza","vestido","sandalias","responsabilidad","guatemala"])

# Función para convertir la palabra a guiones
def convertir_guiones(palabra_secreta):
    guiones = []
    for n in palabra_secreta: #chile
        guiones.append("_")
    return guiones

# Función para verificar si se ingresa una letra
def verificar():
    letra = "%"
    while letra not in"abcdefghijklmnñopqrstuvwxyz":
        letra = input("Ingresa una letra: ")

    return letra

# Comienzo del juego

palabra_secreta = list(palabra_al_azar())
guiones = convertir_guiones(palabra_secreta)
lista_incorrectas = []
vidas = 7

print("""
BIENVENIDO AL JUEGO DEL AHORCADO
EL JUEGO TRATA DE QUE ADIVINES LAS PALABRAS
PUEDES ESCRIBIR UNA LETRA PARA DARTE UNA PISTA
EL JUEGO TE DIRÁ EN DONDE APARECE LA LETRA PARA REDUCIR LA PALABRA
TIENES 7 VIDAS
""")

while True:
    intento = verificar()
    if intento in palabra_secreta:
        for n in range(len(palabra_secreta)):
            if intento == palabra_secreta[n]:
                guiones[n] = intento
                print(guiones)

        if guiones == palabra_secreta:
            print("Felicidades Adivinaste!")
            palabra = "".join(palabra_secreta)
            print(f"La palabra es {palabra}")
    else:
        lista_incorrectas.append(intento)
        print("Lista de intentos incorrectos")
        print(lista_incorrectas)
        vidas -= 1

        if vidas == 0:
            print("GAME OVER")
            palabra = "".join(palabra_secreta)
            print(f"La palabra era {palabra}")
            break