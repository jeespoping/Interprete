import comander
from comander import *
from pygame.locals import *
import pygame, sys

import time

color = (255,255,255)


def colenguaje():
    palabra = ""
    puntero = item(70 + (45 * len(palabra)), 220, "puntero.png", "puntero2.png")
    nodos=list()
    nodos.append(stack)
    contador=0
    pygame.init()

    mifuente = []
    mitexto = []

    for index in range(len(palabra)):
        mifuente.append(pygame.font.Font(None, 30))
        mitexto.append(mifuente[index].render(palabra[index], 2, (200, 60, 80)))

    ventana = pygame.display.set_mode((800,600))
    salir = False
    reloj1 = pygame.time.Clock()

    pygame.display.set_caption("IDE COLENGUAJE")

    gol = Cambiar(palabra)

    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_8:

                if event.key ==pygame.K_9:

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:

                if event.key == pygame.K_RIGHT:




        reloj1.tick(15)
        ventana.fill((255,255,255))

        x = 120
        y = 300
        for index in range(len(palabra)):
            ventana.blit(mitexto[index], (x, y))
            x+=45
        pygame.display.update()

    pygame.quit()


colenguaje()