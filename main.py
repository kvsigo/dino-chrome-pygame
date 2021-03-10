import sys
import pygame

from sprites import Dino, Road, Cloud

pygame.init()

WIDTH = 700
HEIGHT = 500
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()

road = Road(screen, 0, HEIGHT / 2)
dino = Dino(screen, WIDTH / 4, HEIGHT / 2.2, road)
cloud1 = Cloud(screen, WIDTH / 1.25, HEIGHT / 4)
cloud2 = Cloud(screen, WIDTH / 4, HEIGHT / 4)
cloud3 = Cloud(screen, WIDTH / 2, HEIGHT / 9)

while True:
    screen.fill(WHITE)

    screen.blit(road.image, (road.x, road.y))
    screen.blit(dino.image, (dino.x, dino.y))
    screen.blit(cloud1.image, (cloud1.x, cloud1.y))
    screen.blit(cloud2.image, (cloud2.x, cloud2.y))
    screen.blit(cloud3.image, (cloud3.x, cloud3.y))

    pygame.display.update()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == pygame.KEYDOWN:
        #     mods = pygame.key.get_mods()
        #     if event.key == pygame.K_RIGHT:
        #         road.x += 10
        #     elif event.key == pygame.K_LEFT:
        #         road.x -= 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dino.move_left()
    elif keys[pygame.K_RIGHT]:
        dino.move_right()

    clock.tick(30)