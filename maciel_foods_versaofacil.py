import pygame
import random

pygame.init()

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d4fb5794c97ed6420d3eb0c6f0e2eb3547f7a987
window = pygame.display.set_mode((600, 380))
pygame.display.set_caption('maciel comendo')
fundo  = pygame.image.load('imagens/fundo.jpg').convert_alpha()
fundo_menor = pygame.transform.scale(fundo, (600, 380))
hamburguer = pygame.image.load('imagens/Png/hamburguer.png').convert_alpha()
hamburguer_menor = pygame.transform.scale(hamburguer, (30, 40))
cebola = pygame.image.load('imagens/Png/cebola.png').convert_alpha()
cebola_menor = pygame.transform.scale(cebola, (30, 40))
<<<<<<< HEAD
maciel = pygame.image.load('imagens/cabeça do macie2l.png').convert_alpha()
=======
maciel = pygame.image.load('imagens/maciel.png').convert_alpha()
>>>>>>> d4fb5794c97ed6420d3eb0c6f0e2eb3547f7a987
maciel_menor = pygame.transform.scale(maciel, (50, 60))
solo = pygame.image.load('imagens/chao.jpg').convert_alpha() 
solo_menor = pygame.transform.scale(solo, (600, 233))
fonte_pontuação = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
class corredor (pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.imagem = imagem 
        self.rect = self.imagem.get_rect()
        self.rect.x = 20
        self.rect.y = 233
        self.speedx = 0                 
        self.speedy = 3
        self.gravidade = 1            
<<<<<<< HEAD
=======
    window = pygame.display.set_mode((600, 380))
    pygame.display.set_caption('maciel comendo')
    fundo  = pygame.image.load('imagens/fundo.jpg').convert_alpha()
    fundo_menor = pygame.transform.scale(fundo, (600, 380))
    hamburguer = pygame.image.load('imagens/Png/hamburguer.png').convert_alpha()
    hamburguer_menor = pygame.transform.scale(hamburguer, (30, 40))
    cebola = pygame.image.load('imagens/Png/cebola.png').convert_alpha()
    cebola_menor = pygame.transform.scale(cebola, (30, 40))
    maciel = pygame.image.load('imagens/maciel.png').convert_alpha()
    maciel_menor = pygame.transform.scale(maciel, (50, 60))
    solo = pygame.image.load('imagens/chao.jpg').convert_alpha() 
    solo_menor = pygame.transform.scale(solo, (600, 233))
    fonte_pontuação = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
    class corredor (pygame.sprite.Sprite):
        def __init__(self, imagem):
            pygame.sprite.Sprite.__init__(self)
            self.imagem = imagem 
            self.rect = self.imagem.get_rect()
            self.rect.x = 20
            self.rect.y = 233
            self.speedx = 0                 
            self.speedy = 3
            self.gravidade = 1            
>>>>>>> 68de49c5f0e06d3ed7f84453ccc28fdfe08945a2
=======
>>>>>>> d4fb5794c97ed6420d3eb0c6f0e2eb3547f7a987

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x == 550:
            self.speedx = 0
        self.speedy -= self.gravidade
        self.rect.y -= self.speedy

    def pulo (self):
        self.rect.x += self.speedx
        self.speedy = 20
        
    
class comida (pygame.sprite.Sprite):
    def __init__(self, imagem, rect_x, rect_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem 
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speedx = 6

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0 :
            self.rect.left = random.randint(750, 950)
            


class chao (pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 292
        self.speedx = 5

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0 :
            self.rect.left = 600

chao_game = chao(solo_menor)
chao_game_2 = chao(solo_menor)
chao_game_2.rect.x = 600
todas_comidas = pygame.sprite.Group()
todos_chaos = pygame.sprite.Group()
todos_comestiveis = pygame.sprite.Group()
todos_não_comestiveis = pygame.sprite.Group()
pos = 0
for i in range(2):
    não_comestivel = comida(cebola_menor, 200 + pos, 260 )
    todas_comidas.add(não_comestivel)
    todos_não_comestiveis.add(não_comestivel)
    pos += 400
pos = 0
for i in range(4):
    comestivel = comida(hamburguer_menor, 100 + pos, 260 )
    todas_comidas.add(comestivel)
    todos_comestiveis.add(comestivel)
    pos += 400
cabeça_maciel = corredor(maciel_menor)
todos_chaos.add(chao_game)
todos_chaos.add(chao_game_2)

clock = pygame.time.Clock()
FPS = 30
pontuação = 0
vidas = 3 
finalizou = 0
jogando = 1
perdeu = 2
estado = jogando

# ===== Loop principal =====
while estado != finalizou :
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            estado = finalizou
        if estado == jogando:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cabeça_maciel.pulo()
    # ----- Gera saídas
    cabeça_maciel.update()
    todos_chaos.update()
    todas_comidas.update()
    if estado == jogando:
        esta_no_chao = pygame.sprite.spritecollide(cabeça_maciel, todos_chaos, False)
        comeu_comestivel = pygame.sprite.spritecollide(cabeça_maciel, todos_comestiveis, True)
        comeu_não_comestivel = pygame.sprite.spritecollide(cabeça_maciel, todos_não_comestiveis, True)
        for c in esta_no_chao:
            cabeça_maciel.rect.bottom = c.rect.top
            cabeça_maciel.speedy = 0
        for comestivel in comeu_comestivel:
            c =  comida(hamburguer_menor, 800, 260 )
            todos_comestiveis.add(c)
            todas_comidas.add(c)
            pontuação += 100
            if pontuação % 1000 == 0:
                vidas += 1
        for não_comestivel in comeu_não_comestivel:
            c =  comida(cebola_menor, 800, 260 )
            todos_não_comestiveis.add(c)
            todas_comidas.add(c)
            pos += 200
        if len(comeu_não_comestivel) > 0:
            vidas -= 1
            estado = perdeu
    elif estado == perdeu:
        if vidas == 0:
            estado = finalizou
        else:
            estado = jogando


    window.fill((255, 255, 255))  
    window.blit(fundo_menor, (0,0))
    window.blit(cabeça_maciel.imagem, cabeça_maciel.rect)
    todos_chaos.draw(window)
    todas_comidas.draw(window)

    text_surface = fonte_pontuação.render("{:08d}".format(pontuação), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (600/ 2,  10)
    window.blit(text_surface, text_rect)

    text_surface = fonte_pontuação.render(chr(9829) * vidas, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (10, 380 - 10)
    window.blit(text_surface, text_rect)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os r
