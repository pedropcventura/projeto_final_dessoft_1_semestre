import pygame

pygame.init()

window = pygame.display.set_mode((600, 380))
pygame.display.set_caption('hamburguers')
fundo  = pygame.image.load('imagens/fundo restaurante.jpg').convert_alpha()
cliente1 = pygame.image.load('imagens/cliente_homen.png').convert_alpha()
cliente2 = pygame.image.load('imagens/cliente_mulher.png').convert_alpha()
cliente3 = pygame.image.load('imagens/cliente_criança.png').convert_alpha()
cliente3_menor = pygame.transform.scale(cliente3, (200, 300))
hamburguer = pygame.image.load('imagens/hamburguer.png').convert_alpha()
hamburguer_menor = pygame.transform.scale(hamburguer, (80, 90))
milkshake = pygame.image.load('imagens/milkshake.png').convert_alpha()
milkshake_menor = pygame.transform.scale(milkshake, (80, 90))
game = True
tempo = 60
tentativas = 0

class cliente:
    def __init__(self):
        pass
    def comer(self):
        pass
    def vai_embora(self):
        pass

class comida:
    def __init__(self):
        pass

    def mover()


# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  
    window.blit(fundo, (0,0))
    window.blit(cliente1,(100,100))
    window.blit(cliente3_menor ,(300,100))
    window.blit(hamburguer_menor,(250,100))
    window.blit(milkshake_menor,(250,200))
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os r