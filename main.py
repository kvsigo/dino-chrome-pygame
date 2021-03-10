import sys
import pygame

pygame.init()

WIDTH = 700
HEIGHT = 500

# !
WHITE = (255, 255, 255)
BACKGROUND = pygame.image.load(r"sprites\track.png")
CLOUD = pygame.image.load(r"sprites\cloud.png")
DINO = pygame.image.load(r"sprites\Dino\DinoStart.png")

# !
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Dino")

clock = pygame.time.Clock()

while True:
    # !
    SCREEN.fill(WHITE)
    SCREEN.blit(BACKGROUND, (0, HEIGHT / 2))
    SCREEN.blit(CLOUD, (WIDTH / 1.25, HEIGHT / 4))
    SCREEN.blit(CLOUD, (WIDTH / 4, HEIGHT / 4))
    SCREEN.blit(CLOUD, (WIDTH / 2, HEIGHT / 9))
    SCREEN.blit(DINO, (0, HEIGHT / 2.75))

    


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(10)