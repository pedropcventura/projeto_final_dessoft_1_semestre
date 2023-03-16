import pygame
import random

from . import constants
from .sprites.zombie import zombie
from .sprites.pessoa_cagando import pessoa_cagando
from .sprites.Protagonista import Protagonista


def roda_jogo_zumbi():
    pygame.init()
    janela = pygame.display.set_mode((constants.WIDTHG, constants.HEIGHTG))
    pygame.display.set_caption("Jogo de Zumbis")

    #importa imagens e sons externos, alem de se necessario, muda o tamanho das imagens e fonte

    fundo = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/fundo.jpg")
    fundo = pygame.transform.scale(fundo, (constants.WIDTHG, constants.HEIGHTG-90))
    chao = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/chao_cortado.jpg")
    chao2 = chao = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/chao_cortado.jpg")
    zumbi_img = pygame.image.load('Pasta_das_imagens_do_jogo_zombie/3MfN-0/3MfN-0.png')  
    zumbi_img = pygame.transform.scale(zumbi_img, (120,180)).convert_alpha()
    protagonista = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/XOsX-0/XOsX-0.png").convert_alpha() 
    protagonista = pygame.transform.scale(protagonista, (140,140))
    helicoptero = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/helicoptero/helicoptero1.png")
    helicoptero = pygame.transform.scale(helicoptero, (140,70))
    missil = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/missiljogo.png")
    missil = pygame.transform.scale(missil, (55,20))
    missil = pygame.transform.rotate(missil, 180)
    explosao = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/3iCN-0/3iCN-0.png")
    explosao = pygame.transform.scale(explosao, (157.4,106))
    grito = pygame.mixer.Sound("sons_zombie/cabra_gritando_curto.mp3")
    exp_som = pygame.mixer.Sound("sons_zombie/exp_som_curto.mp3")
    pygame.mixer.music.load('sons_zombie/monstros_sa_estourado.mp3')
    vida1 = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/vida.png")
    vida2 = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/vida.png")
    vida3 = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/vida.png")
    vida1 = pygame.transform.scale(vida1, (80,80))
    vida2 = pygame.transform.scale(vida2, (80,80))
    vida3 = pygame.transform.scale(vida3, (80,80))
    vida4 = pygame.transform.scale(vida3, (80,80))
    hit_som = pygame.mixer.Sound("sons_zombie/grito.mp3")
    fonte_placar = pygame.font.Font('PressStart2P.ttf', 28)
    pessoa_caindo = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/pessoa_cagando_sem_fundo.png")
    pessoa_caindo = pygame.transform.scale(pessoa_caindo, (90,90))

    #serve para verificar se explosao e zumbi colidiram
    all_exp = pygame.sprite.Group()




    #lista com animacoes do helicoptero, protagonista, zumbi e explosao respectivamente
    anim_helic = []
    for x in range(5):
        narq = "Pasta_das_imagens_do_jogo_zombie/hcert/helicoptero-{}.png".format(x)
        imge = pygame.image.load(narq)
        imge = pygame.transform.scale(imge, (140,70)).convert_alpha()
        anim_helic.append(imge)


    anim_pro = []
    for x in range(15):
        narq = "Pasta_das_imagens_do_jogo_zombie/XOsX-0/XOsX-{}.png".format(x) 
        imge = pygame.image.load(narq).convert_alpha()
        imge = pygame.transform.scale(imge, (160,160)).convert_alpha()
        anim_pro.append(imge)

    anim_zom = []
    for x in range(24):
        narq = "Pasta_das_imagens_do_jogo_zombie/3MfN-0/3MfN-{}.png".format(x) 
        imge = pygame.image.load(narq).convert_alpha()
        imge = pygame.transform.scale(imge, (120, 180)).convert_alpha()
        imge = pygame.transform.flip(imge, True, False)
        anim_zom.append(imge)

    anim_exp = []
    for x in range(12):
        narq = "Pasta_das_imagens_do_jogo_zombie/3iCN-0/3iCN-{}.png".format(x) 
        imge = pygame.image.load(narq)
        imge = pygame.transform.scale(imge, (160,106))
        anim_exp.append(imge)

    #classe que vao interagir entre si ou com o jogador
    class Helicoptero(pygame.sprite.Sprite):
        def __init__(self, img, all_sprites, all_missils, missil, explosao):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = constants.WIDTHG/2
            self.rect.y = 30
            self.speedx = 0
            self.speedy = 0
            self.all_sprites = all_sprites
            self.all_missils = all_missils
            self.missil = missil
            self.explosao = explosao
            self.frameh = 1

        def update(self):
            #anima o helic
            self.image = anim_helic[self.frameh]
            if self.frameh < 4:
                self.frameh +=1
            else:
                self.frameh = 0

            # Atualização da posição do helicoptero
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            

            # Mantem dentro da tela
            if self.rect.right > 630:
                self.rect.right = 630
            if self.rect.left < -50:
                self.rect.left = -50
            if self.rect.top < -70:
                self.rect.top = -70
            if self.rect.bottom > 370:
                self.rect.bottom = 370
        
        def shoot(self):
            # A nova bala vai ser criada 
            if len(self.all_missils) < 1:
                new_bullet = Missil(self.missil, self.rect.bottom, self.rect.centerx, self.all_sprites,self.explosao)
                self.all_sprites.add(new_bullet)
                self.all_missils.add(new_bullet)

    class Missil(pygame.sprite.Sprite):
        # Construtor da classe.
        def __init__(self, img, bottom, centerx, all_sprites, explosao):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.explosao = explosao
            self.all_sprites = all_sprites
            self.rect.centerx = centerx
            self.rect.bottom = bottom
            self.speedy = 7  # Velocidade fixa 

        def update(self):
            # A bala só se move no eixo y
            self.rect.y += self.speedy

            # se o missil chegar no chao morre
            if self.rect.bottom >510:
                new_exp = Explosao(self.explosao, self.rect.centerx, self.rect.y)
                all_exp.add(new_exp)
                self.all_sprites.add(new_exp)
                self.kill()

    class Explosao(pygame.sprite.Sprite):
        def __init__(self, img, centerx, y):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = img.get_rect()
            self.rect.centerx = centerx
            self.rect.y = y - 90
            self.timer = 0
            self.framee = 0
        
            exp_som.play()
            

        def update(self):
            #anima a explosao
            self.image = anim_exp[self.framee]
            if self.framee < 11:
                self.framee +=1
            else:
                self.framee = 0
            self.timer += pygame.time.get_ticks()
            if self.timer > 10000:
                self.kill()

    #isso serve para verificar colisoes e interacoes e a forma foi organizada para melhor serem utilizadas       
    all_missils = pygame.sprite.Group()
    all_zombies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_cagantes = pygame.sprite.Group()
    grup_player = pygame.sprite.Group()
    protag = Protagonista(protagonista, anim_pro)
    player = Helicoptero(helicoptero, all_sprites, all_missils, missil,explosao)
    cagante = pessoa_cagando(pessoa_caindo, 0, random.randint(60, constants.HEIGHTG))
    cagante2 = pessoa_cagando(pessoa_caindo, 0, random.randint(60, constants.HEIGHTG))
    all_sprites.add(player)
    all_sprites.add(protag, cagante)
    grup_player.add(player)

    for i in range(5):
        zumbi = zombie(zumbi_img, anim_zom)
        all_sprites.add(zumbi)
        all_zombies.add(zumbi)

    chao_x = 0
    chao2_x = constants.WIDTHG
    chao_velocidade = -1.7




    #o loop confere o tempo e so vai rodar na quantidade de vezes que eu quero
    clock = pygame.time.Clock()
    FPS = 60


    vidas = 4

    placar = 0

    pygame.mixer.music.play(loops=-1)
    alive = True
    while alive:
        #falo pro looop so rodar essa quantidade de vezes
        clock.tick(FPS)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #toca a musica da bomba caindo e atira
                    #grito.play()
                    
                    player.shoot()
                #vai pra direçao que o jogador colocou na setinha
                if event.key == pygame.K_LEFT:
                    player.speedx -= 7
                if event.key == pygame.K_RIGHT:
                    player.speedx += 7
                if event.key == pygame.K_DOWN:
                    player.speedy += 7
                if event.key == pygame.K_UP:
                    player.speedy -= 7
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx += 7
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 7
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_DOWN:
                    player.speedy -= 7
                if event.key == pygame.K_UP:
                    player.speedy += 7

            
                
        #preenche a tela inicialmente com branco
        janela.fill((255, 255, 255))
        #coloca primeito o fundo
        janela.blit(fundo, (0, 0))

        
        #atualiza as sprites segundo o que foi definido nas suas respectivas classes
        all_sprites.update()

        #ve se a explosao e o zumbi colidiram
        hits = pygame.sprite.groupcollide(all_zombies, all_exp, True, False)
        for z in hits: # As chaves são os elementos do primeiro grupo (all_zombies) que colidiram com alguma explosao
            # O zumbi e morto e precisa ser recriado
            m = zombie(zumbi_img, anim_zom)
            all_sprites.add(m)
            all_zombies.add(m)
            placar += 10

        #sistema de vidas: se o zumbir encostar no pato, primeiro seje recriado com velocidade aleatoria definida anteriormente e depois confere com quntas vidas esta; desenhe o numero de vidas e se as vidas forem menores ou iguais a zero, parabens, voce morreu!
        hits_vidas = pygame.sprite.spritecollide(protag, all_zombies, True)
        for z in hits_vidas: # As chaves são os elementos do primeiro grupo (all_zombies) que colidiram com alguma explosao
            # O zumbi e morto e precisa ser recriado
            m = zombie(zumbi_img, anim_zom)
            all_sprites.add(m)
            all_zombies.add(m)
        if len(hits_vidas) > 0:
            hit_som.play()
            vidas -= 1
            hits_vidas = []
        if vidas <=0:
            alive = False
        if vidas == 1:
            janela.blit(vida1, (0,0))
        if vidas == 2:
            janela.blit(vida1, (0,0))
            janela.blit(vida2, (20,0))
        if vidas ==3:
            janela.blit(vida1, (0,0))
            janela.blit(vida2, (20,0))
            janela.blit(vida3, (40,0))
        if vidas == 4:
            janela.blit(vida1, (0,0))
            janela.blit(vida2, (20,0))
            janela.blit(vida3, (40,0))
            janela.blit(vida4, (60,0))
        
        
        hits_helic = pygame.sprite.spritecollide(cagante, grup_player, False ,pygame.sprite.collide_mask)
        if hits_helic:
            vidas -= 1
            cagante.hitou_helicoptero()

        if cagante.rect.bottom > 510:
            cagante = pessoa_cagando(pessoa_caindo, 0, player.rect.centerx)


        all_sprites.draw(janela)

        

        #vai movendo os 2 chaos para parecer que as coisas estao correndo (se um dos chaos passar da tela, volta para atras do segundo chao, dessa forma parece que o chao é continuo)
        chao_posicao = janela.blit(chao, (chao_x, constants.HEIGHTG - 90))
        chao_2posicao = janela.blit(chao2, (chao2_x, constants.HEIGHTG - 90))
        chao_x += chao_velocidade
        chao2_x += chao_velocidade
        if chao_x < -constants.WIDTHG:
            chao_x = constants.WIDTHG
        if chao2_x < -constants.WIDTHG:
            chao2_x = constants.WIDTHG

        #desenhando o placar
        text_surface = fonte_placar.render("{:08d}".format(placar), True, (255, 0,0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (constants.WIDTHG / 2,  450)
        janela.blit(text_surface, text_rect)

        pygame.display.update()





