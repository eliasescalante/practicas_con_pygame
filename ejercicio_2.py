import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mi Primer Juego")

# Configuración del reloj
clock = pygame.time.Clock()

# Configuración del personaje
player = pygame.Rect(300, 220, 40, 40)  # Un rectángulo representando al personaje
player_color = (0, 128, 255)  # Color azul

# Velocidad del personaje
speed = 5

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el personaje
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Rellenar la pantalla con un color (negro)
    screen.fill((0, 0, 0))

    # Dibujar el personaje
    pygame.draw.rect(screen, player_color, player)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar a 60 fotogramas por segundo
    clock.tick(60)

# Salir de pygame
pygame.quit()
sys.exit()
