import pygame

pygame.init()

window = pygame.display.set_mode((600, 380))
fundo = pygame.image.load('imagens/Do google/fundorestaurante.jpg').convert_alpha()
fundo = pygame.transform.scale(fundo, (600, 380))
bancada = pygame.image.load('imagens/Do google/Cinza.png')
bancada = pygame.transform.scale(bancada, (600, 200))
grelha = pygame.image.load('imagens/Png/Grelha.png')
grelha = pygame.transform.scale(grelha, (180, 90))
maquina = pygame.image.load('imagens/Png/Maquina_refri.png')
maquina = pygame.transform.scale(maquina, (250, 180))
alface = pygame.image.load('imagens/Png/Alface.png')
alface = pygame.transform.scale(alface, (50, 20))


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


game = True

clock = pygame.time.Clock()
FPS = 30
while game:
    clock.tick(FPS)

    for event in pygame.event.get():

        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if event.type == pygame.QUIT:
            game = False

    window.fill((255, 255, 255))  
    window.blit(fundo, (0,-120))
    window.blit(bancada, (0,230))
    window.blit(grelha, (400,230))
    window.blit(maquina, (-70,210))
    if click[0] == True:
        window.blit(alface, mouse_pos)
    else:
        window.blit(alface, (200,250))

    pygame.display.update()

pygame.quit()