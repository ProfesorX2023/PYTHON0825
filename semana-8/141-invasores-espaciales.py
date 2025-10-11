import pygame
import random
import math
from pygame import mixer


# Inicializar pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e ícono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')

# variables del jugador
img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# función jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#funcion del enemigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene],(x,y))

# función para detectar colisiones
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    if distancia <= 27:
        return True
    else:
        return False

#variables de la bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x + 16,y + 10))

# loop del juego
se_ejecuta = True
while se_ejecuta:

    # imagen de fondo
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    #evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        #evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #mantener jugador dentro de los bordes

    if jugador_x <=0:
        jugador_x =0
    elif jugador_x >=736:
        jugador_x =736

    jugador_x += jugador_x_cambio

    #modificar ubicacion del enemigo

    for e in range(cantidad_enemigos): # e = 0, 1,2,3,4,5,6,7

        # FIN DEL JUEGO
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # mantener dentro de bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]


        enemigo(enemigo_x[e],enemigo_y[e], e)

        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x,  bala_y)
        if colision:
            bala_y = 500
            bala_visible = False
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)
    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)

    pygame.display.update()