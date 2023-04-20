import pygame
from random import randint

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Birds
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
    
        if len(self.obstacles) == 0:

            randomization = randint(0, 1)
            cactusSmallLarge = [SMALL_CACTUS, LARGE_CACTUS]
            cactus_Random = cactusSmallLarge[randomization]

            if randomization == 1:
                cactus = Cactus(cactus_Random, 300)

            else:
                cactus = Cactus(cactus_Random)

            bird = Birds(BIRD)

            cactus_Bird = [bird, cactus]

            self.obstacles.append(cactus_Bird[randomization])
            

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    pygame.mixer.music.play(0)
                    break
                else:
                    self.obstacles.remove(obstacle)

                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
