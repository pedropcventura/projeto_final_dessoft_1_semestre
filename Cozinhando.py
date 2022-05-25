import pygame

pygame.init()

window = pygame.display.set_mode((600, 380))
fundo = pygame.image.load('imagens/Do google/fundorestaurante.jpg').convert_alpha()
fundo_menor = pygame.transform.scale(fundo, (600, 380))
bancada = pygame.image.load('imagens/Do google/Cinza.png')
bancada_menor = pygame.transform.scale(bancada, (600, 150))

game = True

clock = pygame.time.Clock()
FPS = 30
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    window.fill((255, 255, 255))  
    window.blit(fundo_menor, (0,0))
    window.blit(bancada_menor, (0,0))

    pygame.display.update()

pygame.quit()