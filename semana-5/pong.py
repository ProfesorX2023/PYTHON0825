# 🏓 JUEGO DE PONG 🏓
import turtle

# Crear la ventana del juego
ventana = turtle.Screen()
ventana.title("Juego de Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)

# Marcador de puntos
puntos_a = 0
puntos_b = 0

# JUGADOR A (izquierda) - Teclas W y S
jugador_a = turtle.Turtle()
jugador_a.shape("square")
jugador_a.color("blue")
jugador_a.shapesize(stretch_wid=5, stretch_len=1)
jugador_a.penup()
jugador_a.goto(-350, 0)

# JUGADOR B (derecha) - Teclas Arriba y Abajo
jugador_b = turtle.Turtle()
jugador_b.shape("square")
jugador_b.color("red")
jugador_b.shapesize(stretch_wid=5, stretch_len=1)
jugador_b.penup()
jugador_b.goto(350, 0)

# PELOTA
pelota = turtle.Turtle()
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.speed(0)
pelota.dx = 4  # Velocidad horizontal
pelota.dy = 4  # Velocidad vertical

# MARCADOR
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Jugador A: 0    Jugador B: 0", align="center", font=("Arial", 20, "bold"))


# Funciones para mover los jugadores
def jugador_a_arriba():
    if jugador_a.ycor() < 250:
        jugador_a.sety(jugador_a.ycor() + 30)


def jugador_a_abajo():
    if jugador_a.ycor() > -250:
        jugador_a.sety(jugador_a.ycor() - 30)


def jugador_b_arriba():
    if jugador_b.ycor() < 250:
        jugador_b.sety(jugador_b.ycor() + 30)


def jugador_b_abajo():
    if jugador_b.ycor() > -250:
        jugador_b.sety(jugador_b.ycor() - 30)


# Controles del teclado
ventana.listen()
ventana.onkey(jugador_a_arriba, "w")
ventana.onkey(jugador_a_abajo, "s")
ventana.onkey(jugador_b_arriba, "Up")
ventana.onkey(jugador_b_abajo, "Down")

# Bucle principal del juego
while True:
    ventana.update()

    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Rebote en la pared de arriba
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1  # Cambiar direccion

    # Rebote en la pared de abajo
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # Punto para Jugador A (pelota sale por la derecha)
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntos_a += 1
        marcador.clear()
        marcador.write(f"Jugador A: {puntos_a}    Jugador B: {puntos_b}", align="center", font=("Arial", 20, "bold"))

    # Punto para Jugador B (pelota sale por la izquierda)
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntos_b += 1
        marcador.clear()
        marcador.write(f"Jugador A: {puntos_a}    Jugador B: {puntos_b}", align="center", font=("Arial", 20, "bold"))

    # Rebote en la paleta del Jugador B
    if pelota.xcor() > 340 and abs(pelota.ycor() - jugador_b.ycor()) < 50:
        pelota.setx(340)
        pelota.dx *= -1

    # Rebote en la paleta del Jugador A
    if pelota.xcor() < -340 and abs(pelota.ycor() - jugador_a.ycor()) < 50:
        pelota.setx(-340)
        pelota.dx *= -1