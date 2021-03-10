import pygame

class Road(pygame.sprite.Sprite):
    def __init__(self, surface, x, y):
        super().__init__()
        self.image = pygame.image.load(r"images\track.png")
        self.x = x
        self.y = y

class Dino(pygame.sprite.Sprite):
    def __init__(self, surface, x, y):
        super().__init__()
        self.image = pygame.image.load(r"images\Dino\DinoStart.png")
        self.x = x
        self.y = y

class Cloud(pygame.sprite.Sprite):
    def __init__(self, surface, x, y):
        super().__init__()
        self.image = pygame.image.load(r"images\cloud.png")
        self.x = x
        self.y = y

