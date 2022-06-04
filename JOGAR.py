import pygame
from maciel_foods_versaofacil import *
from jogo_zumbi import *

pygame.init()

WIDTH = 500
HIGHT = 600

pygame.display.set_caption("Tela Inicial")
window = pygame.display.set_mode((WIDTH, HIGHT))

pixel = pygame.image.load('imagens/Png/Tela inicial.png')
pixel = pygame.transform.scale(pixel, (300, 300))
pixel = pygame.transform.scale(pixel, (WIDTH, HIGHT))

pygame.mixer.init()
pygame.mixer.music.load("audios/duduc.mp3")
pygame.mixer.music.set_volume(100)
pygame.mixer.music.play()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game == False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                pygame.mixer.music.stop()
                roda_jogo_zumbi()
            if event.key == pygame.K_b:
                pygame.mixer.music.stop()
                roda_jogo_maciel()

        window.fill((255, 255, 255))  
        window.blit(pixel, (0,0))

        pygame.display.update()
    
pygame.quit()
    
