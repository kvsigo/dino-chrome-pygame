import pygame

class Road(pygame.sprite.Sprite):
    def __init__(self, surface, x, y):
        super().__init__()
        self.image = pygame.image.load(r"images\track.png")
        self.x = x
        self.y = y

class Dino(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, target):
        super().__init__()
        self.image = pygame.image.load(r"images\Dino\DinoStart.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))

        self.right1 = pygame.image.load(r"images\Dino\DinoRun1.png")
        self.right1 = pygame.transform.scale(self.right1, (self.right1.get_width() // 2, self.right1.get_height() // 2))
        self.right2 = pygame.image.load(r"images\Dino\DinoRun2.png")
        self.right2 = pygame.transform.scale(self.right2, (self.right2.get_width() // 2, self.right2.get_height() // 2))
        self.left1 = pygame.transform.flip(self.right1, True, False)
        self.left2 = pygame.transform.flip(self.right2, True, False)

        self.step = 0
        self.x = x
        self.y = y

        self.target = target


    def move_right(self):
        if self.step:
            self.image = self.right1
            self.step = 0
        else:
            self.image = self.right2
            self.step = 1
        # self.x += 5
        self.target.x -= 5

    def move_left(self):
        if self.step:
            self.image = self.left1
            self.step = 0
        else:
            self.image = self.left2
            self.step = 1
        # self.x -= 5
        self.target.x += 5


class Cloud(pygame.sprite.Sprite):
    def __init__(self, surface, x, y):
        super().__init__()
        self.image = pygame.image.load(r"images\cloud.png")
        self.x = x
        self.y = y

