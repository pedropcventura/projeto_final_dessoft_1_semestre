import pygame
from maciel_foods_versãomedio import *
from jogo_zumbi import *

pygame.init()
 
WIDTH = 500
HIGHT = 600

#Define as imagens
pygame.display.set_caption("Tela Inicial")
window = pygame.display.set_mode((WIDTH, HIGHT))

pixel = pygame.image.load('imagens/Png/Tela inicial.png')
pixel = pygame.transform.scale(pixel, (WIDTH, HIGHT))

z_or_b = pygame.image.load('imagens/Png/press z or b.png')


#Define classe para o efeito do zoom 
class Zoom(pygame.sprite.Sprite):
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



#Define classe para o efeito do loop da animação
class Animacao(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        rei0 = pygame.image.load('imagens/Png/rei0.png')
        rei0 = pygame.transform.scale(rei0, (WIDTH, 500))
        rei1 = pygame.image.load('imagens/Png/rei1.png')
        rei1 = pygame.transform.scale(rei1, (WIDTH, 500))
        rei2 = pygame.image.load('imagens/Png/rei2.png')
        rei2 = pygame.transform.scale(rei2, (WIDTH, 500))
        rei3 = pygame.image.load('imagens/Png/rei3.png')
        rei3 = pygame.transform.scale(rei3, (WIDTH, 500))
        rei4 = pygame.image.load('imagens/Png/rei4.png')
        rei4 = pygame.transform.scale(rei4, (WIDTH, 500))
        rei5 = pygame.image.load('imagens/Png/rei5.png')
        rei5 = pygame.transform.scale(rei5, (WIDTH, 500))
        rei6 = pygame.image.load('imagens/Png/rei6.png')
        rei6 = pygame.transform.scale(rei6, (WIDTH, 500))
        rei7 = pygame.image.load('imagens/Png/rei7.png')
        rei7 = pygame.transform.scale(rei7, (WIDTH, 500))
        self.sprites.append(rei0)
        self.sprites.append(rei1)
        self.sprites.append(rei2)
        self.sprites.append(rei3)
        self.sprites.append(rei4)
        self.sprites.append(rei5)
        self.sprites.append(rei6)
        self.sprites.append(rei7)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 0.2

        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


#Coloca o zoom e animação dentro do grupo
z_or_b = Zoom(200, 130)
sprites_zoom = pygame.sprite.Group()
sprites_zoom.add(z_or_b)

hehehehaw = Animacao(0, 0)
sprites_animacao = pygame.sprite.Group()
sprites_animacao.add(hehehehaw)

clock = pygame.time.Clock()
FPS = 60


t=0
espera_final=0
final = True
game = True
tudo = True 
#Loop do jogo inteiro
def inicializa_musica(arquivo, volume):
     pygame.mixer.init()
     pygame.mixer.music.load(arquivo)
     pygame.mixer.music.set_volume(volume)
     pygame.mixer.music.play()


while tudo:
    window = pygame.display.set_mode((WIDTH, HIGHT))

    #Começa música dudu
    
    inicializa_musica("sou_foda_mp3.ogg.mp3", 80)
    
    

    #Loop da tela inicial + jogos 
    while game:

        pygame.display.set_caption("Tela Inicial")
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tudo = False
                pygame.quit()

            #Roda jogo zumbi
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    pygame.mixer.music.stop()
                    roda_jogo_zumbi()
                    game = False

                #Roda jogo zumbi
                if event.key == pygame.K_b:
                    pygame.mixer.music.stop()
                    roda_jogo_maciel()
                    game = False

                       
        window.fill((255, 255, 255))  
        window.blit(pixel, (0,0))
        
        if t >= 50:
            sprites_zoom.draw(window)
            sprites_zoom.update()

        t+=1
        pygame.display.update()

    #Loop tela final
    pygame.display.set_caption("Tela final")
    final = True
    window = pygame.display.set_mode((WIDTH, 500))
    while final:
        
        pygame.time.wait(25)
        sprites_animacao.draw(window)
        sprites_animacao.update()

        if t>46:
            pygame.mixer.init()
            pygame.mixer.music.load("audios/hehehehaw.mp3")
            pygame.mixer.music.set_volume(1000)
            pygame.mixer.music.play()
            t=0
        t+=1


        if espera_final > 60:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    tudo = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    final = False
                    game = True
                    espera_final = 0

        espera_final+=1

        pygame.display.update()
        
pygame.quit()
    
