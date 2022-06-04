import pygame

pygame.init()

WIDTH = 1200
HIGHT = 760

window = pygame.display.set_mode((WIDTH, HIGHT))

fundo = pygame.image.load('imagens/Do google/fundorestaurante.jpg').convert_alpha()
fundo = pygame.transform.scale(fundo, (WIDTH, HIGHT))

bancada = pygame.image.load('imagens/Do google/Cinza.png')
bancada = pygame.transform.scale(bancada, (WIDTH, 400))

tabua = pygame.image.load('imagens/Png/Tábua.png')
tabua = pygame.transform.scale(tabua, (180, 320))

grelha = pygame.image.load('imagens/Png/Grelha.png')
grelha = pygame.transform.scale(grelha, (360, 180))

maquina = pygame.image.load('imagens/Png/Maquina_refri.png')
maquina = pygame.transform.scale(maquina, (500, 360))

escala = (100, 40)

alface = pygame.image.load('imagens/Png/Alface.png')
alface_img = pygame.transform.scale(alface, escala)
alface_pos = (400, 480)



class Comida (pygame.sprite.Sprite):
    def __init__(self, imagem, pos, escala):
        pygame.sprite.Sprite.__init__(self)
        self.pressed = False
        self.image = imagem 
        self.rect = pygame.Rect(pos, escala)
        self.rect.centerx = escala[0]/2+pos[0]
        self.rect.centery = escala[1]/2+pos[1]

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True

            
        if self.pressed:
            window.blit(alface_img, mouse_pos)
            self.rect.topleft = mouse_pos
        
            if self.rect.centerx < 650 or self.rect.centerx > 180+650:
                self.rect.center = (400,500)
            if self.rect.centery < 460 or self.rect.centery > 320+460:
                self.rect.center = (400,500)
            if pygame.mouse.get_pressed()[0] != True:
                self.pressed = False
                
        else:
            window.blit(alface_img, self.rect.topleft)

game = True

alface = Comida(alface_img, alface_pos, escala)

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
    window.blit(tabua, (650,460))
    window.blit(maquina, (-140,420))
    
    alface.update()
    pygame.display.update()

pygame.quit()