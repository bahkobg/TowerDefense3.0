import pygame
import global_variables
import random
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.path = random.choice([global_variables.map_1_path_1, global_variables.map_1_path_2])
        self.image = None
        self.img_list = random.choice(
            [global_variables.enemy_1, global_variables.enemy_2, global_variables.enemy_3, global_variables.enemy_4,
             global_variables.enemy_5])
        self.animation_index = 0
        self.flipped = False
        self.change = ()
        self.path_pos = 0
        self.health = 100
        self.speed = 2
        self.worth = 1
        self.fire_resistance = 0
        self.freeze_resistance = 0
        self.lighting_resistance = 0
        self.poison_resistance = 0
        self.paused = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def set_paused(self, x):
        if self.paused != x:
            self.paused = x

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage

    def die(self):
        pass

    def jump(self):
        pass

    def move(self):
        """
             Moves the enemy. Called in enemy draw func.
             :return: None
             """

        # Increase the path position index, if the index is last in the list, move the enemy off the board
        x1, y1 = self.x, self.y
        x2, y2 = self.path[self.path_pos][0], self.path[self.path_pos][1]

        # Calculate the slope
        slope = (x2 - x1, y2 - y1)

        # Depending of the slope, change the image orientation
        if slope[0] > 0:
            self.flipped = False
        elif slope[0] < 0:
            self.flipped = True

        # Calculate the distance between the points
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Calculate the steps required, so it maintain constant speed.
        steps = distance // self.speed
        if steps != 0:
            self.change = (slope[0] / steps, slope[1] / steps)
        else:
            self.path_pos += 1

        if self.path_pos + 1 >= len(self.path):
            self.kill()
            global_variables.stats_player_health -= 1
        else:
            if not self.paused:
                self.x += self.change[0]
                self.y += self.change[1]

    def animation(self):
        pass

    def update(self):

        self.move()

    def draw(self, surface):
        if self.animation_index >= len(self.img_list):
            self.animation_index = 0
        self.image = pygame.transform.scale(self.img_list[self.animation_index], (self.width, self.height))
        if self.flipped:  # if the enemy is moving left
            surface.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
        elif not self.flipped and self.health > 0:  # if the enemy is moving right
            surface.blit(self.image, (self.x, self.y))
        if not self.paused:
            self.animation_index += 1