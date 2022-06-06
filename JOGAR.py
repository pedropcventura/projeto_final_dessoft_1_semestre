import pygame
from maciel_foods_versaofacil import *
from jogo_zumbi import *

pygame.init()

WIDTH = 500
HIGHT = 600

pygame.display.set_caption("Tela Inicial")
window = pygame.display.set_mode((WIDTH, HIGHT))

pixel = pygame.image.load('imagens/Png/Tela inicial.png')
pixel = pygame.transform.scale(pixel, (WIDTH, HIGHT))

z_or_b = pygame.image.load('imagens/Png/press z or b.png')

tela_fim = pygame.image.load('imagens/Png/hehehehaw.png')
tela_fim = pygame.transform.scale(tela_fim, (500, 500))

pygame.mixer.init()
pygame.mixer.music.load("audios/duduc.mp3")
pygame.mixer.music.set_volume(100)
pygame.mixer.music.play()



class Animacao(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        zb1 = pygame.transform.scale(z_or_b, (300/16, 180/16))
        zb2 = pygame.transform.scale(z_or_b, (300/8, 180/8))
        zb3 = pygame.transform.scale(z_or_b, (300/6, 180/6))
        zb4 = pygame.transform.scale(z_or_b, (300/4, 180/4))
        zb5 = pygame.transform.scale(z_or_b, (300/2, 180/2))
        zb6 = pygame.transform.scale(z_or_b, (300/1.5, 180/1.5))
        zb7 = pygame.transform.scale(z_or_b, (300, 180))
        self.sprites.append(zb1)
        self.sprites.append(zb2)
        self.sprites.append(zb3)
        self.sprites.append(zb4)
        self.sprites.append(zb5)
        self.sprites.append(zb6)
        self.sprites.append(zb7)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 0.2

        if self.current_sprite < len(self.sprites):
            self.image = self.sprites[int(self.current_sprite)]



z_or_b = Animacao(200, 130)
sprites_animacao = pygame.sprite.Group()
sprites_animacao.add(z_or_b)

clock = pygame.time.Clock()
FPS = 60


t=0
game = True
while game:

    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game == False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                pygame.mixer.music.stop()
                roda_jogo_zumbi()

                window.blit(tela_fim, (0,0))
                pygame.mixer.music.load("audios/hehehehaw.mp3")
                pygame.mixer.music.set_volume(100)
                pygame.mixer.music.play()
                check = True
                while check:
                    if event.type == pygame.KEYDOWN:
                        check = False

            if event.key == pygame.K_b:
                pygame.mixer.music.stop()
                roda_jogo_maciel()
            
                window.blit(tela_fim, (0,0))
                pygame.mixer.music.load("audios/hehehehaw.mp3")
                pygame.mixer.music.set_volume(100)
                pygame.mixer.music.play()
                check = True
                while check:
                    if event.type == pygame.KEYDOWN:
                        check = False

                    

    window.fill((255, 255, 255))  
    window.blit(pixel, (0,0))
    
    if t >= 150:
        sprites_animacao.draw(window)
        sprites_animacao.update()

    t+=1
    pygame.display.update()
    
pygame.quit()
    
