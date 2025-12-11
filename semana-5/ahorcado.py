import random
import os


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def obtener_ahorcado(errores):
    estados = [
        """
           ┌───────┐
           │       │
           │       
           │      
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │       │
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      /│
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      /│\\
           │      
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      /│\\
           │      / 
           │
        ═══╧═══════════
        """,
        """
           ┌───────┐
           │       │
           │      😵
           │      /│\\
           │      / \\
           │
        ═══╧═══════════
        """
    ]
    return estados[errores]


def mostrar_vidas(vidas_restantes, vidas_totales=6):
    corazones_llenos = "❤️ " * vidas_restantes
    corazones_vacios = "🖤 " * (vidas_totales - vidas_restantes)
    return corazones_llenos + corazones_vacios


def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado


def jugar():
    palabras = [
        "python", "javascript", "programacion", "computadora", "algoritmo",
        "variable", "funcion", "bucle", "condicional", "estructura",
        "biblioteca", "modulo", "clase", "objeto", "herencia",
        "polimorfismo", "encapsulamiento", "compilador", "interprete"
    ]

    palabra = random.choice(palabras).upper()
    letras_adivinadas = set()
    letras_incorrectas = set()
    vidas = 6
    errores = 0

    while True:
        limpiar_pantalla()

        print("\n" + "=" * 50)
        print("       🎮 JUEGO DEL AHORCADO 🎮")
        print("=" * 50)

        print(obtener_ahorcado(errores))

        print(f"\n   Vidas: {mostrar_vidas(vidas)}")
        print(f"\n   Palabra: {mostrar_palabra(palabra, letras_adivinadas)}")

        if letras_incorrectas:
            print(f"\n   ❌ Letras incorrectas: {', '.join(sorted(letras_incorrectas))}")

        # Verificar victoria
        if all(letra in letras_adivinadas for letra in palabra):
            print("\n" + "=" * 50)
            print("   🎉🏆 ¡FELICIDADES! ¡GANASTE! 🏆🎉")
            print(f"   La palabra era: {palabra}")
            print("=" * 50)
            break

        # Verificar derrota
        if vidas == 0:
            print("\n" + "=" * 50)
            print("   💀 ¡GAME OVER! 💀")
            print(f"   La palabra era: {palabra}")
            print("=" * 50)
            break

        # Pedir letra
        print("\n" + "-" * 50)
        letra = input("   👉 Ingresa una letra: ").upper().strip()

        if len(letra) != 1 or not letra.isalpha():
            input("   ⚠️  Por favor ingresa solo una letra. [Enter]")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas:
            input("   ⚠️  Ya ingresaste esa letra. [Enter]")
            continue

        if letra in palabra:
            letras_adivinadas.add(letra)
            print(f"   ✅ ¡Correcto! La letra '{letra}' esta en la palabra.")
        else:
            letras_incorrectas.add(letra)
            vidas -= 1
            errores += 1
            print(f"   ❌ ¡Incorrecto! La letra '{letra}' no esta en la palabra.")

        input("   Presiona [Enter] para continuar...")


jugar()