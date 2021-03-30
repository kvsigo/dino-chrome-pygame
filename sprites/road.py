import pygame

class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets\images\road.png")
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load(r"assets\images\road.png")
        self.rect1 = self.image1.get_rect()

        surface = pygame.display.get_surface()
        self.rect.midleft = (0, surface.get_height() / 2)
        self.rect1.midleft = self.rect.midright

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)

    def update(self):
        self.rect.x -= 5
        self.rect1.x -= 5

        if self.rect.right < 0:
            self.rect.midleft = self.rect1.midright
        
        if self.rect1.right < 0:
            self.rect1.midleft = self.rect.midright