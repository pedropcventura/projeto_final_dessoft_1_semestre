todos_chaos = pygame.sprite.Group()
todos_comestiveis = pygame.sprite.Group()
todos_não_comestiveis = pygame.sprite.Group()
pos = 0
for i in range(3):
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