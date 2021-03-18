# Импортирование модулей
import sys
import pygame

# Подключение
pygame.init()
pygame.mixer.init()

# Константы
WIDTH = 700
HEIGHT = 500
FPS = 30

# Цвета
WHITE = (255, 255, 255)

# Параметры окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()

# Спрайты

# Главный цикл
while True:
    # Частота обновления
    clock.tick(FPS)

    # Отображение цветов и объектов
    screen.fill(WHITE)

    # Обновление объектов

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Переворачиваем доску
    pygame.display.flip()