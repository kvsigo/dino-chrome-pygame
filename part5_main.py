# Импортирование модулей
import sys
import pygame
import random
from part5_sprites import Road, Cloud, Dino, Cactus

# Подключение
pygame.init()
pygame.mixer.init()

# Константы
WIDTH = 700
HEIGHT = 500
FPS = 60

# Цвета
WHITE = (255, 255, 255)

# Параметры окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()

# Спрайты
sprites = pygame.sprite.Group()
road = Road(screen)
cloud1 = Cloud(screen)
cloud2 = Cloud(screen)
cloud3 = Cloud(screen)
player = Dino(screen)
sprites.add(road, cloud1, cloud2, cloud3, player)

obstacles = pygame.sprite.Group()

# Главный цикл
running = True
while running:
    # Частота обновления
    clock.tick(FPS)

    # Игровые события
    if random.randint(1, 1000) in range(1, 5):
        cactus = Cactus(screen)
        obstacles.add(cactus)

    if pygame.sprite.spritecollide(player, obstacles, False):
        print('Есть касание!')
        # ending = True
        # while ending:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             ending = False
        #             running = False

    # Отрисовка цветов и объектов
    screen.fill(WHITE)
    sprites.draw(screen)
    obstacles.draw(screen)

    # Обновление объектов
    sprites.update()
    obstacles.update()

    # События (нажатия на кнопку)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            player.jump()

    # Переворачиваем доску
    pygame.display.flip()
    