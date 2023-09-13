# 1) inicialização
# 1.1) importa e inicia os pacotes
import pygame
import random
def roda_jogo_maciel():

    pygame.init()
    pygame.mixer.init()
    # 1.2) gera tela principal

    window = pygame.display.set_mode((600, 380))
    pygame.display.set_caption('maciel comendo') 
    
    # 1.3)inicializa imagens
    def carrega_imagem(arquivo, width, heigth):
        img = pygame.image.load(arquivo).convert_alpha()
        img_menor = pygame.transform.scale(img, (width, heigth))
        return img_menor

    fundo_menor  = carrega_imagem('imagens/fundo.jpg' , 600, 380)
    hamburguer_menor = carrega_imagem('imagens/Png/hamburguer.png', 30, 40)
    cebola_menor = carrega_imagem('imagens/cebola.png', 35, 45)
    maciel_menor = carrega_imagem('imagens/cabeça do macie2l.png', 40, 60)
    solo_menor = carrega_imagem('imagens/chao.jpg',  600, 233)
    fonte_pontuação = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

    # 1.4) inicializa sons
    pygame.mixer.music.load('sou_foda_mp3.ogg.mp3')
    pygame.mixer.music.set_volume(400)
    pygame.mixer.music.load('audios/duduc.mp3')
    pygame.mixer.music.set_volume(1)

    # 1.5) inicia estruturas de dados
    class corredor (pygame.sprite.Sprite):
        def __init__(self, imagem):

            # construor da classe corredoe
            pygame.sprite.Sprite.__init__(self)
            self.imagem = imagem 
            self.rect = self.imagem.get_rect()
            self.rect.x = 20
            self.rect.y = 233
            self.speedx = 0                 
            self.speedy = 3
            self.gravidade = 1            

        def update(self):

            #atualizaçao da posiçao do corredor
            self.rect.x += self.speedx
            if self.rect.x == 550:
                self.speedx = 0
            self.speedy -= self.gravidade
            self.rect.y -= self.speedy

        def pulo (self):
            # veriifica se o usuarios pode pular para poder desviar dos inimigos
            if self.speedy < -10 or self.speedy == 0:
                self.rect.x += self.speedx
                self.speedy = 20
        
    
    
        
    class comida (pygame.sprite.Sprite):
        def __init__(self, imagem, rect_x, rect_y):
            # define a classe comida
            pygame.sprite.Sprite.__init__(self)
            self.image = imagem 
            self.rect = self.image.get_rect()
            self.rect.x = rect_x
            self.rect.y = rect_y
            self.speedx = 6

        def update(self):
            #atualiza a posiçao da comida
            self.rect.x -= self.speedx
            if self.rect.right < 0 :
                self.rect.left = random.randint(750, 950)
                


    class chao (pygame.sprite.Sprite):
        def __init__(self, imagem):
            # define a classe chao
            pygame.sprite.Sprite.__init__(self)
            self.image = imagem
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 292
            self.speedx = 5

        def update(self):
            # atualiza o chao para ele se mover 
            self.rect.x -= self.speedx
            if self.rect.right < 0 :
                self.rect.left = 600



    chao_game = chao(solo_menor)
    chao_game_2 = chao(solo_menor)
    chao_game_2.rect.x = 600
    todos_chaos = pygame.sprite.Group()
    todas_comidas = pygame.sprite.Group()
    todos_comestiveis = pygame.sprite.Group()
    todos_não_comestiveis = pygame.sprite.Group()
    pos = 0 

    # criando grupo das cebolas 
    for i in range(3):
        não_comestivel = comida(cebola_menor, 200 + pos, 250 )
        todas_comidas.add(não_comestivel)
        todos_não_comestiveis.add(não_comestivel)
        pos += 400
        pos = 0

    # criando grupo dos hamburgueres
    for i in range(4):
        comestivel = comida(hamburguer_menor, 100 + pos, 260 )
        todas_comidas.add(comestivel)
        todos_comestiveis.add(comestivel)
        pos += 400

    # criando o jogador
    cabeça_maciel = corredor(maciel_menor)
    
    # criando o chaos
    todos_chaos.add(chao_game)
    todos_chaos.add(chao_game_2)

    # ajustando a velocidade do game
    clock = pygame.time.Clock()
    FPS = 30


    # inicializando pontuaçao e vidas
    pontuação = 0
    vidas = 3 

    # adicionando estadods
    finalizou = 0
    jogando = 1
    perdeu = 2
    estado = jogando

    # 2) loop principal
    pygame.mixer.music.play(loops=-1)
    while estado != finalizou :
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                estado = finalizou
                pygame.quit()
            if estado == jogando:
                # verifica se apertou na barra de espaço
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        cabeça_maciel.pulo()
        # atualiza estado do jogo
        cabeça_maciel.update()
        todos_chaos.update()
        todas_comidas.update()
        if estado == jogando:
            # verificsa colisoes
            esta_no_chao = pygame.sprite.spritecollide(cabeça_maciel, todos_chaos, False)
            comeu_comestivel = pygame.sprite.spritecollide(cabeça_maciel, todos_comestiveis, True)
            comeu_não_comestivel = pygame.sprite.spritecollide(cabeça_maciel, todos_não_comestiveis, True)
            for c in esta_no_chao:
                # o jogador se mantem no chao
                cabeça_maciel.rect.bottom = c.rect.top
                cabeça_maciel.speedy = 0
            for comestivel in comeu_comestivel:
                # verifica se o jogador comeu um hamburguer e aumenta a pontusaçao a cada vez que isso aconteçe
                c =  comida(hamburguer_menor, 800, 260 )
                todos_comestiveis.add(c)
                todas_comidas.add(c)
                pontuação += 100

                # a cada 1000 pontos o jogador ganha uma vida
                if pontuação % 1000 == 0:
                    vidas += 1
            for não_comestivel in comeu_não_comestivel:
                # verifica se o jogador comeu uma cebola e
                c =  comida(cebola_menor, 800, 260 )
                todos_não_comestiveis.add(c)
                todas_comidas.add(c)
                pos += 200
            if len(comeu_não_comestivel) > 0:
                 # diminui uma vida a cada vez que o usuario come uma cebola 
                vidas -= 1
                estado = perdeu
        elif estado == perdeu:
            if vidas == 0:
                # o jogo finaliza quando o jogador ´perde todas suas vidas
                estado = finalizou
            else:
                estado = jogando


        # desenha o jogo 
        window.fill((255, 255, 255))  
        window.blit(fundo_menor, (0,0))
        window.blit(cabeça_maciel.imagem, cabeça_maciel.rect)
        todos_chaos.draw(window)
        todas_comidas.draw(window)


        # desenha a pontuaçao
        text_surface = fonte_pontuação.render("{:08d}".format(pontuação), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (600/ 2,  10)
        window.blit(text_surface, text_rect)

        # desenha a vidas
        text_surface = fonte_pontuação.render(chr(9829) * vidas, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, 380 - 10)
        window.blit(text_surface, text_rect)

        
        pygame.display.update()
