from itertools import chain
import pygame
pygame.init()

window = pygame.display.set_mode((600, 380))
pygame.display.set_caption('hamburguers')
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
   
game = True
vidas = 3
class corredor (pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.imagem = imagem 
        self.rect = self.imagem.get_rect()
        self.rect.x = 0
        self.rect.y = 233
        self.speedx = 3
        self.speedy = 3
        self.gravidade = 3

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x == 550:
            self.speedx = 0
        self.speedy -= self.gravidade
        self.rect.y -= self.speedy

    def pulo (self):
        self.rect.x += self.speedx
        self.speedy = 30
        
    
class comida (pygame.sprite.Sprite):
    def __init__(self, imagem, rect_x, rect_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem 
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def update(self):
        if self.rect.left > 600:
            pass

            


class chao (pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 292
        self.speedx = 3

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.rect.left = 600

chao_game = chao(solo_menor)
todas_comidas = pygame.sprite.Group()
todos_chaos = pygame.sprite.Group()
pos = 0
for i in range(4):
    não_comestivel = comida(cebola_menor, 100 + pos, 260 )
    todas_comidas.add(não_comestivel)
    pos += 150
pos = 0
for i in range(4):
    comestivel = comida(hamburguer_menor, 50 + pos, 260 )
    todas_comidas.add(comestivel)
    pos += 150
cabeça_maciel = corredor(maciel_menor)
todos_chaos.add(chao_game)

clock = pygame.time.Clock()
FPS = 30
# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cabeça_maciel.pulo()
    # ----- Gera saídas
    cabeça_maciel.update()
    chao_game.update()

    esta_no_chao = pygame.sprite.spritecollide(cabeça_maciel, todos_chaos, False)
    for c in esta_no_chao:
        cabeça_maciel.rect.bottom = c.rect.top
        cabeça_maciel.speedy = 0



    window.fill((255, 255, 255))  
    window.blit(fundo_menor, (0,0))
    window.blit(cabeça_maciel.imagem, cabeça_maciel.rect)
    window.blit(chao_game.image, chao_game.rect) 
    todas_comidas.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os r