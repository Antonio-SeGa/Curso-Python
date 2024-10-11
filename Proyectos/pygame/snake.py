import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tamaño de la pantalla
ancho = 600
alto = 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de Snake')

# Configuración de la serpiente
tamaño_segmento = 10
velocidad = 15

# Fuente
fuente = pygame.font.SysFont("bahnschrift", 25)

def mensaje(msg, color):
    mesg = fuente.render(msg, True, color)
    pantalla.blit(mesg, [ancho / 6, alto / 3])

def juego():
    game_over = False
    game_close = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho - tamaño_segmento) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamaño_segmento) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            pantalla.fill(azul)
            mensaje("Perdiste! Presiona C para volver a jugar o Q para salir", rojo)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_segmento
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_segmento
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_segmento
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_segmento
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_close = True

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamaño_segmento, tamaño_segmento])
        serpiente_segmento = []
        serpiente_segmento.append(x1)
        serpiente_segmento.append(y1)
        serpiente.append(serpiente_segmento)
        if len(serpiente) > longitud_serpiente:
            del serpiente[0]

        for s in serpiente[:-1]:
            if s == serpiente_segmento:
                game_close = True

        for s in serpiente:
            pygame.draw.rect(pantalla, negro, [s[0], s[1], tamaño_segmento, tamaño_segmento])

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_segmento) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tamaño_segmento) / 10.0) * 10.0
            longitud_serpiente += 1

        pygame.time.Clock().tick(velocidad)

    pygame.quit()
    quit()

juego()
