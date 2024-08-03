import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Detectar Barra Espaciadora")

mirada_de_perrito = 0

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mirada_de_perrito = 0
                print(mirada_de_perrito)
            elif event.key == pygame.K_RIGHT:
                mirada_de_perrito = 1
                print(mirada_de_perrito)
            elif event.key == pygame.K_SPACE:
                if mirada_de_perrito == 0:
                    print("el perrito ladra a la izquierda")
                else:
                    print("el perrito ladra a la derecha")

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de pygame
pygame.quit()
sys.exit()

