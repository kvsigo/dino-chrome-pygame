import pygame
import random

class Road(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load(r"images\track.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = (0, self.surface.get_height() / 2)

class Cloud(pygame.sprite.Sprite):
    def __init__(self, surface, x=0, y=0):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load(r"images\cloud.png")
        self.rect = self.image.get_rect()

        x = random.randint(0, self.surface.get_width())
        y = random.randint(self.surface.get_height() / 4, self.surface.get_height() / 2)
        self.rect.center = (x, y)

