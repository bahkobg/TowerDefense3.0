import pygame
import global_variables
import time


class Effect(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.x = x
        self.y = y
        self.damage = None
        self.radius = None
        self.exploded = None
        self.image = None
        self.animation_index = 0
        self.being_dragged = None
        self.in_position = None
        self.enemy_in_range = None
        self.timer = time.time()
        self.width, self.height, self.animation_list = self.buy_effect(name)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = self.animation_list[0]

    def set_in_position(self):
        """
        Spawn the effect in position on the board.
        :return: None
        """
        self.being_dragged = False
        self.in_position = True

    def drag(self, center):
        """
        Sets the tower position equal to the current mouse position.
        :param center: tuple -> (x, y) mouse coordinates
        :return: None
        """
        self.rect.center = center

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:
            surface.blit(self.image, self.rect)
            if self.in_position:
                self.animation(surface)

    def set_enemy_in_range(self, x):
        if self.enemy_in_range != x:
            self.enemy_in_range = x

    def animation(self, surface):

        if self.animation_index >= len(self.animation_list):
            # Play sound in here
            self.animation_index = 0

        self.image = pygame.transform.scale(self.animation_list[self.animation_index], (self.width, self.height))

        if self.enemy_in_range:
            if time.time() - self.timer > 0.15:
                self.animation_index += 1
                self.timer = time.time()
        else:
            self.image = pygame.transform.scale(self.animation_list[0], (self.width, self.height))

        surface.blit(self.image, self.rect)

    @staticmethod
    def buy_effect(name):
        if name == 'FIRE':
            return 10, 10, global_variables.fire
        elif name == 'STONES':
            return 10, 10, global_variables.stone
        elif name == 'FREEZE':
            return 10, 10, global_variables.freeze
        elif name == 'RAIN':
            return 10, 10, global_variables.rain
        else:
            return False
