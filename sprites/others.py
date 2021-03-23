import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.points = 0

        self.font = pygame.font.Font(r'assets\fonts\game.ttf', 20)
        self.image = self.font.render(f"HI {self.points}", True, (83, 83, 83))

        self.rect = self.image.get_rect()
        self.rect.center = self.surface.get_width() / 1.25, self.surface.get_height() / 8

    def update(self):
        self.points += 1
        self.image = self.font.render(f"HI {self.points}", True, (83, 83, 83))

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class GameOver(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface

        self.font = pygame.font.Font(r'assets\fonts\game.ttf', 20)
        self.image = self.font.render("G A M E  O V E R", True, (83, 83, 83))

        self.rect = self.image.get_rect()
        self.rect.center = self.surface.get_width() / 2, self.surface.get_height() / 4

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        