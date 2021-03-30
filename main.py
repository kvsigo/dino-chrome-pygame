import pygame
import sys
from sprites.road import Road
from sprites.cloud import Cloud
from sprites.dino import Dino
from sprites.obstacles import Cactus
from sprites.game import Score, Game
 
pygame.init()
 
# Константы
WIDTH = 700
HEIGHT = 500
FPS = 60
 
# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()
 
def main():
    # Спрайты
    road = Road()
    clouds = pygame.sprite.Group()
    player = Dino()
    obstacles = pygame.sprite.Group()
    score = Score()
    
    running = True
    while running:
        # Частота обновления экрана
        clock.tick(FPS)
    
        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for obstacle in obstacles:
            if pygame.sprite.collide_mask(player, obstacle):
                player.sound_die.play()
                game = Game()
                game.draw(screen)
                pygame.display.update()
                game.over(main)
    
        # Рендеринг
        screen.fill((255, 255, 255))
        road.draw(screen)
        clouds.draw(screen)
        player.draw(screen)
        obstacles.draw(screen)
        score.draw(screen)
    
        # Обновление спрайтов
        road.update()
        clouds.update()
        player.update()
        obstacles.update()
        score.update()

        if len(clouds) < 3:
            cloud = Cloud()
            clouds.add(cloud)

        if len(obstacles) < 1:
            cactus = Cactus()
            obstacles.add(cactus)
    
        # Обновление экрана
        pygame.display.update()
 
if __name__ == "__main__":
    main()