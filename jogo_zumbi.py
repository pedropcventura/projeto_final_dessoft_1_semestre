import pygame
def roda_jogo_zumbi():
    pygame.init()
    janela = pygame.display.set_mode((550, 500))
    pygame.display.set_caption("Jogo de Zumbis")
    fundo = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/fundo.jpg")
    chao = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/chao_cortado.jpg")
    chao2 = chao = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/chao_cortado.jpg")
    zumbi = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/zumbi.png")
    zumbi = pygame.transform.scale(zumbi, (80,120))
    protagonista = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/protagonista.png")
    protagonista = pygame.transform.scale(protagonista, (120,120))
    helicoptero = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/helicoptero/helicoptero1.png")
    missil = pygame.image.load("Pasta_das_imagens_do_jogo_zombie/missiljogo.png")
    missil = pygame.transform.scale(missil, (120,120))
    missil = pygame.transform.rotate(missil, 180)

    chao_x = 0
    chao2_x = 550
    chao_velocidade = -1
    chao_velocidade = -1.7

    zumbi_x = 470
    zumbi_velocidade = -2.3
    zumbi_velocidade = -2

    clock = pygame.time.Clock()
    FPS = 60

    alive = True
    while alive:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
        
        janela.fill((255, 255, 255))
        janela.blit(fundo, (0, 0))
        chao_posicao = janela.blit(chao, (chao_x, 410))
        chao_2posicao = janela.blit(chao2, (chao2_x, 410))
        chao_x += chao_velocidade
        chao2_x += chao_velocidade
        if chao_x < -550:
            chao_x = 550
        if chao2_x < -550:
            chao2_x = 550
        janela.blit(zumbi, (zumbi_x, 290))
        zumbi_x += zumbi_velocidade
        if zumbi_x < -80:
            zumbi_x = 550

        janela.blit(protagonista, (15, 290))

        janela.blit(helicoptero, (130, 30))

        janela.blit(missil, (285, 125))


        pygame.display.update()


    pygame.quit()