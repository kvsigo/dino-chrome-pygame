import pygame
import random

class Road(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load(r"images\track.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = (0, self.surface.get_height() / 2)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < self.surface.get_width():
            self.rect.left = 0

class Cloud(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load(r"images\cloud.png")
        self.rect = self.image.get_rect()

        x = random.randint(0, self.surface.get_width())
        y = random.randint(self.surface.get_height() / 4, self.surface.get_height() / 2)
        self.rect.center = (x, y)

        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = self.surface.get_width()


class Dino(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        
        self.run1 = pygame.image.load(r"images\Dino\DinoRun1.png")
        self.run1 = pygame.transform.scale(self.run1, (self.run1.get_width() // 2, self.run1.get_height() // 2))
        self.run2 = pygame.image.load(r"images\Dino\DinoRun2.png")
        self.run2 = pygame.transform.scale(self.run2, (self.run2.get_width() // 2, self.run2.get_height() // 2))

        self.image = self.run1

        self.rect = self.image.get_rect()
        self.rect.center = (self.surface.get_width() / 8, self.surface.get_height() / 2.1)

        self.step = 0

        self.jumping = False
        self.falling_speed = 15

    def update(self):
        if self.step % 7 == 0:
            if self.image == self.run1:
                self.image = self.run2
            else:
                self.image = self.run1
        self.step += 1
  
        if self.jumping:
            self.rect.y -= self.falling_speed
            self.falling_speed -= 1
            
            if self.falling_speed < -15:
                self.jumping = False
                self.falling_speed = 15  

    def jump(self):
        if self.falling_speed >= 15:
            self.falling_speed = 15
            self.jumping = True