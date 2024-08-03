import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mi Primer Juego")

# Configuración del reloj
clock = pygame.time.Clock()

# Cargar la imagen del personaje
player_image = pygame.image.load('canio.png')
player_rect = player_image.get_rect()
player_rect.topleft = (300, 220)

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
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    # Rellenar la pantalla con un color (negro)
    screen.fill((0, 0, 0))

    # Dibujar el personaje
    screen.blit(player_image, player_rect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar a 60 fotogramas por segundo
    clock.tick(60)

# Salir de pygame
pygame.quit()
sys.exit()
