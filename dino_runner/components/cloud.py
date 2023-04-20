import pygame
from pygame.sprite import Sprite
from random import randint

from dino_runner.utils.constants import CLOUD

X_POS = 1100
Y_POS = [80, 150, 180]

class Cloud(Sprite):

    def __init__(self):
        self.image = CLOUD
        self.randomization = randint(0, 1)
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = X_POS
        self.cloud_rect.y = Y_POS[self.randomization]

    def update(self):
        if self.cloud_rect.topright[0] < 0:
            self.cloud_rect.x = X_POS
        self.cloud_rect.x -= 10
            
    def draw(self, screen):
        screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))
