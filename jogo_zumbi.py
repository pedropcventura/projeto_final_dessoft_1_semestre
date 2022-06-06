import pygame
import random
pygame.init()
janela = pygame.display.set_mode((550, 500))
pygame.display.set_caption("Jogo de Zumbis")

fundo = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/fundo.jpg")
#fundo = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/fundo.jpg")
chao = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/chao_cortado.jpg")
chao2 = chao = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/chao_cortado.jpg")
zumbi_img = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/zumbi.png")
zumbi_img = pygame.transform.scale(zumbi_img, (80,120))
protagonista = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/protagonista.png")
zumbi_img = pygame.transform.scale(zumbi_img, (80,120)).convert_alpha()
protagonista = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/protagonista.png").convert_alpha()
protagonista = pygame.transform.scale(protagonista, (140,140))
helicoptero = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/helicoptero/helicoptero1.png")
missil = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/missiljogo.png")
missil = pygame.transform.scale(missil, (55,20))
missil = pygame.transform.rotate(missil, 180)
explosao = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/explosao/frame_00_delay-0.03s.jpg")
explosao = pygame.transform.scale(explosao, (157.4,106))


all_exp = pygame.sprite.Group()





anim_helic = []
for x in range(3):
    x +=1
    narq = "Pasta_das_imagens_do_jogo_zombie/helicoptero/helicoptero{}.png".format(x)
    imge = pygame.image.load(narq).convert()
    anim_helic.append(imge)


anim_pro = []
for x in range(35):
    x+=1
    narq = "Pasta_das_imagens_do_jogo_zombie/stickman_correndo/frame_{:02d}_delay-0.03s.jpg".format(x)
    imge = pygame.image.load(narq).convert_alpha()
    imge = pygame.transform.scale(imge, (160,160))
    anim_pro.append(imge)
print(len(anim_pro))
class Helicoptero(pygame.sprite.Sprite):
    def __init__(self, img, all_sprites, all_missils, missil):
    def __init__(self, img, all_sprites, all_missils, missil, explosao):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 550/2
        self.rect.y = 30
        self.speedx = 0
        self.speedy = 0
        self.all_sprites = all_sprites
        self.all_missils = all_missils
        self.missil = missil
        self.explosao = explosao
        self.frameh = 1

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy


        # Mantem dentro da tela
        if self.rect.right > 630:
            self.rect.right = 630
        if self.rect.left < -50:
            self.rect.left = -50
        if self.rect.top < -70:
            self.rect.top = -70
        if self.rect.bottom > 270:
            self.rect.bottom = 270

    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_bullet = Missil(self.missil, self.rect.bottom, self.rect.centerx)
        self.all_sprites.add(new_bullet)
        self.all_missils.add(new_bullet)

        if len(self.all_missils) < 3:
            new_bullet = Missil(self.missil, self.rect.bottom, self.rect.centerx, self.all_sprites,self.explosao)
            self.all_sprites.add(new_bullet)
            self.all_missils.add(new_bullet)


class zombie(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(550, 600)
        self.rect.y = 290
        self.speedx = random.randint(-4,-1)
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        if self.rect.x < 125:
            self.rect.x = random.randint(550, 600)
            self.rect.y = 290
            self.speedx = random.randint(-4,-1)
        
class Protagonista(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 274
        self.framep = 1
    def update(self):
        self.image = anim_pro[self.framep]


        if self.framep < 34:
            self.framep +=1
        else:
            self.framep = 0




class Missil(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, bottom, centerx):
    def __init__(self, img, bottom, centerx, all_sprites, explosao):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        self.explosao = explosao
        self.all_sprites = all_sprites
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 5  # Velocidade fixa para cima
    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom >410:
            new_exp = Explosao(self.explosao, self.rect.centerx, self.rect.y)
            all_exp.add(new_exp)
            self.all_sprites.add(new_exp)
            self.kill()


class Explosao(pygame.sprite.Sprite):
    def __init__(self, img, centerx, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx;
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.y = y - 90
        self.timer = 0
    def update(self):
        self.timer += pygame.time.get_ticks()
        if self.timer > 50000:
           self.kill()

chao_x = 0
chao2_x = 550
chao_velocidade = -1.7

# Criando um grupo de meteoros
        
all_missils = pygame.sprite.Group()
all_zombies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
protag = Protagonista(protagonista)
player = Helicoptero(helicoptero, all_sprites, all_missils, missil)
player = Helicoptero(helicoptero, all_sprites, all_missils, missil,explosao)
all_sprites.add(player)
all_sprites.add(protag)
# Criando os meteoros
@@ -135,6 +182,13 @@ def update(self):
    all_sprites.add(zumbi)
    all_zombies.add(zumbi)

chao_x = 0
chao2_x = 550
chao_velocidade = -1.7

# Criando um grupo de meteoros




clock = pygame.time.Clock()
@@ -184,27 +238,20 @@ def update(self):

    janela.fill((255, 255, 255))

    janela.blit(fundo, (0, 0))
    #janela.blit(fundo, (0, 0))

    chao_posicao = janela.blit(chao, (chao_x, 410))
    chao_2posicao = janela.blit(chao2, (chao2_x, 410))
    chao_x += chao_velocidade
    chao2_x += chao_velocidade
    if chao_x < -550:
        chao_x = 550
    if chao2_x < -550:
        chao2_x = 550


    all_sprites.update()

    hits = pygame.sprite.groupcollide(all_zombies, all_missils, True, True)
    hits = pygame.sprite.groupcollide(all_zombies, all_exp, True, False)
    for z in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
        # O meteoro e destruido e precisa ser recriado
        m = zombie(zumbi_img)
        all_sprites.add(m)
        all_zombies.add(m)

    hits = pygame.sprite.spritecollide(player, all_zombies, True)
    
    #hits = pygame.sprite.spritecollide(player, all_zombies, True)
    all_sprites.draw(janela)

    #janela.blit(protagonista, (15, 274))
    #janela.blit(helicoptero, (130, 30))
    #janela.blit(missil, (285, 125))

    #janela.blit(explosao, (260,320))
    chao_posicao = janela.blit(chao, (chao_x, 410))
    chao_2posicao = janela.blit(chao2, (chao2_x, 410))
    chao_x += chao_velocidade
    chao2_x += chao_velocidade
    if chao_x < -550:
        chao_x = 550
    if chao2_x < -550:
        chao2_x = 550

    pygame.display.update()