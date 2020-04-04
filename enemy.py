import pygame
import global_variables
import random
import math
import time


class Enemy(pygame.sprite.Sprite):
    """
    Defines the main enemy class.
    """
    def __init__(self, x, y, health, map_number):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.radius = 64
        self.path = random.choice([global_variables.game_settings[map_number][2], global_variables.game_settings[map_number][3]])
        self.image = None
        self.img_list = random.choice(
            [global_variables.enemy_1, global_variables.enemy_2, global_variables.enemy_3, global_variables.enemy_4,
             global_variables.enemy_5])
        self.animation_index = 0
        self.flipped = False
        self.dying = False
        self.change = ()
        self.path_pos = 1
        self.health_max = health
        self.health = self.health_max
        self.speed = 2
        self.worth = random.randint(1,5)
        self.fire_resistance = 0
        self.freeze_resistance = 0
        self.lighting_resistance = 0
        self.poison_resistance = 0
        self.paused = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.timer = time.time()

    def set_paused(self, x):
        if self.paused != x:
            self.paused = x

    def take_damage(self, damage, rate):
        if self.health <= 0:
            self.die()
        if time.time() - self.timer > rate:
            if self.health > 0:
                self.health -= damage
            self.timer = time.time()

    def die(self):
        self.dying = True
        global_variables.stats_kills += 1
        global_variables.stats_money += self.worth
        self.kill()

    def health_bar(self, surface):
        width = 40  # length of the bar
        health_bar = width * (self.health / self.health_max)

        if self.flipped and self.health > 0:
            pygame.draw.rect(surface, (255, 0, 0), (self.x + 16, self.y, width, 8))
            pygame.draw.rect(surface, (0, 255, 0), (self.x + 16, self.y, health_bar, 8))
        elif not self.flipped and self.health > 0:
            pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, width, 8))
            pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, health_bar, 8))

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
                self.rect.topleft = self.x, self.y

    def animation(self):
        pass

    def draw(self, surface, game_state):
        if game_state == 2:
            if self.animation_index >= 10:
                self.animation_index = 0
            self.image = pygame.transform.scale(self.img_list[self.animation_index], (self.width, self.height))
            if self.flipped:  # if the enemy is moving left
                surface.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))
            elif not self.flipped and self.health > 0:  # if the enemy is moving right
                surface.blit(self.image, (self.x, self.y))
            if not self.paused:
                self.animation_index += 1
            self.health_bar(surface)
            self.move()

