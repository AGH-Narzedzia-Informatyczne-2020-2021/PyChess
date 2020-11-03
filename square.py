import pygame, sys

screen = pygame.display.set_mode((1280, 720))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 100, 100))
    pygame.display.flip()
