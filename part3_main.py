# Импортирование модулей
import sys
import pygame
from part3_sprites import Road, Cloud

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
sprites.add(road, cloud1, cloud2, cloud3)

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

    # Переворачиваем доску
    pygame.display.flip()
    