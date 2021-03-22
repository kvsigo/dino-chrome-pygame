# Импортирование модулей
import sys
import pygame
import random

from sprites.road import Road
from sprites.clouds import Cloud
from sprites.others import *
from sprites.obstacles import Cactus
from sprites.player import Dino

# Подключение
pygame.init()

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


def main():
    # Спрайты и группы спрайтов
    background = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    road = Road(screen)
    player = Dino(screen)
    score = Score(screen)

    background.add(road, score)

    # Главный цикл
    running = True
    while running:
        # Частота обновления
        clock.tick(FPS)

        # Случайное генерирование объектов
        if len(clouds) < 3:
            clouds.add(Cloud(screen))
            background.add(clouds)

        if random.randint(1, 1000) in range(1, 10) and len(obstacles) < 1:
            obstacles.add(Cactus(screen))

        if pygame.sprite.spritecollide(player, obstacles, False):
            player.image = player.dead
            player.die_sound.play()
            background.add(GameOver(screen))
            running = False

        # Отрисовка фона и объектов
        screen.fill(WHITE)
        background.draw(screen)
        obstacles.draw(screen)
        player.draw(screen)

        # Обновление объектов
        background.update()
        obstacles.update()
        player.update()

        # События (нажатия на кнопку)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Переворачиваем доску
        pygame.display.flip()

        if not running:
            # Конец игры: можно либо выйти, либо начать заново при нажатии на пробел
            while True:
                clock.tick(5)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                    main()
                
        
if __name__ == '__main__':
    main()