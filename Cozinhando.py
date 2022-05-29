import pygame

pygame.init()

WIDTH = 1200
HIGHT = 760

window = pygame.display.set_mode((WIDTH, HIGHT))

fundo = pygame.image.load('imagens/Do google/fundorestaurante.jpg').convert_alpha()
fundo = pygame.transform.scale(fundo, (WIDTH, HIGHT))

bancada = pygame.image.load('imagens/Do google/Cinza.png')
bancada = pygame.transform.scale(bancada, (WIDTH, 400))

grelha = pygame.image.load('imagens/Png/Grelha.png')
grelha = pygame.transform.scale(grelha, (360, 180))

maquina = pygame.image.load('imagens/Png/Maquina_refri.png')
maquina = pygame.transform.scale(maquina, (500, 360))

alface = pygame.image.load('imagens/Png/Alface.png')
alface_img = pygame.transform.scale(alface, (100, 40))
alface_pos = (400, 500)


class Comida (pygame.sprite.Sprite):
    def __init__(self, imagem, pos):
        pygame.sprite.Sprite.__init__(self)
        self.pressed = False
        self.image = imagem 
        self.rect = pygame.Rect(pos, (100, 40))
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            
        if self.pressed:
            window.blit(alface_img, mouse_pos)
            if pygame.mouse.get_pressed()[0] != True:
                self.pressed = False

        else:
            window.blit(alface_img, (400, 500))

game = True

alface1 = Comida(alface_img, alface_pos)

clock = pygame.time.Clock()
FPS = 30
while game:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    window.fill((255, 255, 255))  
    window.blit(fundo, (0,-240))
    window.blit(bancada, (0,460))
    window.blit(grelha, (800,460))
    window.blit(maquina, (-140,420))
    
    alface1.update()
    pygame.display.update()

pygame.quit()