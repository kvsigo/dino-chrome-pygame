# Импортирование модулей
import sys
import pygame
from part4_sprites import Road, Cloud, Dino, Cactus

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
cactus = Ca
sprites.add(road, cloud1, cloud2, cloud3, player)

# Главный цикл
while True:
    # Частота обновления
    clock.tick(FPS)

    # Отображение цветов и объектов
    screen.fill(WHITE)
    sprites.draw(screen)

    # Обновление объектов
    sprites.update()

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            player.jump()

    # Переворачиваем доску
    pygame.display.flip()
    