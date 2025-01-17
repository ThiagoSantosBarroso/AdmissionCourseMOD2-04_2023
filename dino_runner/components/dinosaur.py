import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import HAMMER_TYPE, RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}


X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8.5
DUCK_VEL = 8.5


class Dinosaur(Sprite):

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUNNING[0]
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_jump = False
        self.dino_run = True
        self.jump_vel = JUMP_VEL
        self.dino_duck = False
        self.duck_vel = DUCK_VEL
        self.setup_state()
        self.jump_sound = pygame.mixer.Sound('dino_runner/assets/Other/Jump_Sound.wav')


    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()

        elif self.dino_duck:
            self.ducking()

        if self.step_index >= 9:
            self.step_index = 0

        if user_input[pygame.K_DOWN] and not self.dino_duck and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True

        if user_input[pygame.K_UP] and not self.dino_jump and not self.dino_duck:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
            self.jump_sound.play(0)

        if not self.dino_jump and not self.dino_duck:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def ducking(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        if self.dino_duck:
            self.dino_rect.y = 340
            self.dino_rect.x = X_POS
            self.duck_vel -= 10
        if self.duck_vel < -DUCK_VEL:
            self.dino_duck = False
            self.duck_vel = DUCK_VEL
        self.step_index += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))