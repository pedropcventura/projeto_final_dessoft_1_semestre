from itertools import chain
import pygame

pygame.init()

window = pygame.display.set_mode((600, 380))
fundo = pygame.image.load('imagens/Do google/fundo restaurante.jpg').convert_alpha()
fundo_menor = pygame.transform.scale(fundo, (600, 380))

game = True

clock = pygame.time.Clock()
FPS = 30
while game:
    clock.tick(FPS)

    window.fill((255, 255, 255))  
    window.blit(fundo_menor, (0,0))

pygame.quit()