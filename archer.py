import pygame
import global_variables
import time


class Archer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sound_bow = pygame.mixer.Sound('assets/sounds/bow.wav')
        self.x = x
        self.y = y
        self.width = 45
        self.height = 45
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = None
        self.animation_index = 0
        self.img_list = global_variables.towers_archer[38:44]
        self.flipped = False
        self.paused = False
        self.timer = time.time()
        self.enemy_in_range = False

    def set_enemy_in_range(self, x):
        """
        Sets enemy in range
        :param x: bool
        :return: None
        """
        if self.enemy_in_range != x:
            self.enemy_in_range = x
            self.animation_index = 0

    def draw(self, surface):
        if self.animation_index >= len(self.img_list):
            pygame.mixer.Sound.play(self.sound_bow)
            self.animation_index = 0
        self.image = pygame.transform.scale(self.img_list[self.animation_index], (self.width, self.height))
        if self.enemy_in_range:
            if time.time() - self.timer > 0.15:
                self.animation_index += 1
                self.timer = time.time()

        if self.flipped:  # if the enemy is left
            surface.blit(pygame.transform.flip(self.image, True, False), self.rect)

        else:  # if the enemy is right
            surface.blit(self.image, self.rect)
