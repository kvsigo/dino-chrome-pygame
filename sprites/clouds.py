import pygame
import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load(r"assets\images\cloud.png")

        self.rect = self.image.get_rect()
        x = self.surface.get_width() + self.image.get_width()
        y = random.randint(self.surface.get_height() / 4, self.surface.get_height() / 2)
        self.rect.center = (x, y)

        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.x -= self.speed

        # Удаление из всех групп, в которых состоит объект
        if self.rect.right < 0:
            for group in self.groups():
                group.remove(self)