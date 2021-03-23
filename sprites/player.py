import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        
        self.run1 = pygame.image.load(r"assets\images\DinoRun1.png")
        self.run1 = pygame.transform.scale(self.run1, (self.run1.get_width() // 2, self.run1.get_height() // 2))
        self.run2 = pygame.image.load(r"assets\images\DinoRun2.png")
        self.run2 = pygame.transform.scale(self.run2, (self.run2.get_width() // 2, self.run2.get_height() // 2))
        self.dead = pygame.image.load(r"assets\images\DinoDead.png")
        self.dead = pygame.transform.scale(self.dead, (self.dead.get_width() // 2, self.dead.get_height() // 2))

        self.die_sound = pygame.mixer.Sound(r'assets\sounds\die.wav')
        self.jump_sound = pygame.mixer.Sound(r'assets\sounds\jump.wav')

        self.image = self.run1

        self.rect = self.image.get_rect()
        self.rect.center = (self.surface.get_width() / 8, self.surface.get_height() / 2.15)
        
        self.step = 0

        self.jumping = False
        self.height = 15

    def update(self):
        if self.step % 7 == 0:
            if self.image == self.run1:
                self.image = self.run2
            else:
                self.image = self.run1
        self.step += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            if self.jumping == False:
                self.jumping = True
                self.jump_sound.play()
  
        if self.jumping:
            self.rect.y -= self.height
            self.height -= 1
            if self.height < -15:
                self.height = 15
                self.jumping = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)