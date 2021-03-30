import pygame
import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets\images\cloud.png")
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()

        self.rect.x = surface.get_width()
        self.rect.y = random.randint(0, surface.get_height() / 2 - self.rect.height)

        self.speed = random.randint(2, 5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.speed

        surface = pygame.display.get_surface()
        if self.rect.right < 0:
            self.kill()
