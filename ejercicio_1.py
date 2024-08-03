import pygame
import sys


# Inicializar pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mi Primer Juego")

# Configuración del reloj
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        print(keys)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar a 60 fotogramas por segundo
    clock.tick(60)

# Salir de pygame
pygame.quit()
sys.exit()
