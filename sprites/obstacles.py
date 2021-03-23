import pygame
import random

class Cactus(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load(r"assets\images\Cactus.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))

        self.rect = self.image.get_rect()
        self.rect.center = self.surface.get_width(), self.surface.get_height() / 2.15

    def update(self):
        self.rect.x -= 5
        
        # Удаление из всех групп, в которых состоит объект
        if self.rect.right < 0:
            for group in self.groups():
                group.remove(self)

