import pygame

pygame.init()

pygame.display.set_mode((600, 380))
pygame.display.set_caption("Tela Inicial")

pixel = pygame.image.load('imagens/telainicial.png')
pixel = pygame.transform.scale(pixel, (300, 300))

image_4k = pygame.image.load("imagens/pexels-christian-heitz-842711.jpg")
image_4k = pygame.transform.scale(image_4k, (600, 380))

modo1 = pygame.image.load("imagens/modo1.png")
modo1 = pygame.transform.scale(modo1, (350, 350))
modo2 = pygame.image.load("imagens/modo2.png")
modo2 = pygame.transform.scale(modo2, (350, 350))

window = pygame.display.set_mode((600, 380))
pygame.mixer.init()
pygame.mixer.music.load("audios/duduc.mp3")
pygame.mixer.music.set_volume(100)
pygame.mixer.music.play()

game = True
while game:
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    window.fill((255, 255, 255)) 
    window.blit(image_4k, (0, 0))
    window.blit(pixel, (150, -20))
    
    window.blit(modo2, (300, 160))
    window.blit(modo1, (0, 155))
    pygame.display.update()

pygame.quit()