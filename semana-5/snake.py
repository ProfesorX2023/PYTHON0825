# 🐍 JUEGO DE LA SERPIENTE 🐍
import turtle
import time
import random

# Crear la ventana del juego
ventana = turtle.Screen()
ventana.title("Juego de la Serpiente")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)

# Crear la cabeza de la serpiente
serpiente = turtle.Turtle()
serpiente.shape("square")
serpiente.color("green")
serpiente.penup()
serpiente.speed(0)

# Crear la comida
comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.speed(0)
comida.goto(0, 100)

# Variables del juego
direccion = "stop"
cuerpo = []
puntos = 0

# Mostrar puntos
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Puntos: 0", align="center", font=("Arial", 20, "bold"))


# Funciones para mover la serpiente
def ir_arriba():
    global direccion
    if direccion != "abajo":
        direccion = "arriba"


def ir_abajo():
    global direccion
    if direccion != "arriba":
        direccion = "abajo"


def ir_izquierda():
    global direccion
    if direccion != "derecha":
        direccion = "izquierda"


def ir_derecha():
    global direccion
    if direccion != "izquierda":
        direccion = "derecha"


# Controles con las flechas del teclado
ventana.listen()
ventana.onkey(ir_arriba, "Up")
ventana.onkey(ir_abajo, "Down")
ventana.onkey(ir_izquierda, "Left")
ventana.onkey(ir_derecha, "Right")

# Bucle principal del juego
while True:
    ventana.update()

    # Mover el cuerpo de la serpiente
    for i in range(len(cuerpo) - 1, 0, -1):
        x = cuerpo[i - 1].xcor()
        y = cuerpo[i - 1].ycor()
        cuerpo[i].goto(x, y)

    if len(cuerpo) > 0:
        cuerpo[0].goto(serpiente.xcor(), serpiente.ycor())

    # Mover la cabeza según la dirección
    if direccion == "arriba":
        serpiente.sety(serpiente.ycor() + 20)
    if direccion == "abajo":
        serpiente.sety(serpiente.ycor() - 20)
    if direccion == "izquierda":
        serpiente.setx(serpiente.xcor() - 20)
    if direccion == "derecha":
        serpiente.setx(serpiente.xcor() + 20)

    # Si choca con la pared, reiniciar
    if serpiente.xcor() > 290 or serpiente.xcor() < -290 or serpiente.ycor() > 290 or serpiente.ycor() < -290:
        serpiente.goto(0, 0)
        direccion = "stop"
        for parte in cuerpo:
            parte.hideturtle()
        cuerpo.clear()
        puntos = 0
        marcador.clear()
        marcador.write("Puntos: 0", align="center", font=("Arial", 20, "bold"))

    # Si come la comida
    if serpiente.distance(comida) < 20:
        # Mover la comida a un lugar aleatorio
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        # Agregar una parte al cuerpo
        nueva_parte = turtle.Turtle()
        nueva_parte.shape("square")
        nueva_parte.color("lime")
        nueva_parte.penup()
        nueva_parte.speed(0)
        cuerpo.append(nueva_parte)

        # Sumar puntos
        puntos += 10
        marcador.clear()
        marcador.write(f"Puntos: {puntos}", align="center", font=("Arial", 20, "bold"))

    # Velocidad del juego
    time.sleep(0.1)