import pygame
import random
from .. import constants


class pessoa_cagando(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 7  # Velocidade fixa 

    def update(self):
        # o cagante só se move no eixo y
        self.rect.y += self.speedy

        # se o cagante chegar no chao morre
        if self.rect.bottom > 510: 
            self.rect.bottom = 0
            self.rect.centerx = random.randint(200, constants.WIDTHG)

    def hitou_helicoptero(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randint(200, constants.WIDTHG)
