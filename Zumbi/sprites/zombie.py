import pygame
import random
from .. import constants


class zombie(pygame.sprite.Sprite):
    def __init__(self, img, anim_zom):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.anim_zom = anim_zom

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(constants.WIDTHG, 600)
        self.rect.y = 370
        self.speedx = random.randint(-4,-1)
        self.framez = 0

    def update(self):
        #anima o zombie
        self.image = self.anim_zom[self.framez]
        if self.framez < 9:
            self.framez +=1
        else:
            self.framez = 0
        
        # Atualizando a posição do zumbi
        self.rect.x += self.speedx

        if self.rect.x < 125:
            self.rect.x = random.randint(constants.WIDTHG, 600)
            self.rect.y = 270
            self.speedx = random.randint(-4,-1)