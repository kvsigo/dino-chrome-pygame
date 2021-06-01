import pygame
import sys

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 0
        self.points = 0

        self.font = pygame.font.Font(r"assets\fonts\gamefont.ttf", 20)
        self.image = self.font.render(f"HI {self.points}", True, (83, 83, 83))
        self.rect = self.image.get_rect()

        surface = pygame.display.get_surface()
        self.rect.x = surface.get_width() / 1.3
        self.rect.y = surface.get_height() / 8

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f"HI {self.points}", True, (83, 83, 83))

    def update(self):
        self.step += 1
        if self.step % 10 == 0:
            self.points += 1

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # ⭐ Конец игры
        self.font = pygame.font.Font(r"assets\fonts\gamefont.ttf", 20)
        self.image = self.font.render(f"G A M E  O V E R", True, (83, 83, 83))
        self.rect = self.image.get_rect()
        self.image1 = pygame.image.load(r"assets\images\reset.png")
        self.rect1 = self.image1.get_rect()

        surface = pygame.display.get_surface()
        self.rect.center = surface.get_width() / 2, surface.get_height() / 4
        self.rect1.center = surface.get_width() / 2, surface.get_height() / 2.75

    # ⭐ Конец игры
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)