import pygame

class Road(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load(r"assets\track.png")

        self.rect = self.image.get_rect()
        self.rect.midleft = (0, self.surface.get_height() / 2)

    def update(self):
        self.rect.x -= 5
        
        # Дублирование изображения дороги, когда она закончится
        if 0 < self.rect.right < self.surface.get_width():
            self.surface.blit(self.image, (self.rect.right, self.rect.y))
        if self.rect.right < 0:
            self.rect.x = self.rect.right
