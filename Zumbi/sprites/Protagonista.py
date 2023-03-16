import pygame

class Protagonista(pygame.sprite.Sprite):
    def __init__(self, img, anim_pro):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 374
        self.framep = 0

        self.anim_pro = anim_pro

    def update(self):
        #anima o protagonista pato
        self.image = self.anim_pro[self.framep]
        if self.framep < 13:
            self.framep +=1
        else:
            self.framep = 0
