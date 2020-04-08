import pygame
import global_variables
import time
import math


class Tower(pygame.sprite.Sprite):
    """
    Defines main tower class.
    """

    def __init__(self, x, y, game_map):
        pygame.sprite.Sprite.__init__(self)
        self.sound_bow = pygame.mixer.Sound('assets/sounds/bow.wav')
        self.x = x
        self.y = y
        self.width = 85
        self.height = 96
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False
        self.being_dragged = False
        self.image = None
        self.in_position = False
        self.timer = time.time()
        self.game_map = game_map

        # Tower stuff
        self.range = 120
        self.radius = 120
        self.damage = 1
        self.rate = 0.8
        self.price = 1
        self.bullets = []

        # Shoot animation
        self.animation_index = 0
        self.shoot_index = 0
        self.animation_list = []
        self.shoot_list = []
        self.flipped = False
        self.archer_rect = None
        self.arrow_rect = None

        # Archer
        self.enemy_in_range = False
        self.enemy_in_close_range = False

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """
        self.being_dragged = False
        self.in_position = True

    def get_range_rect(self):
        """
        Overrides the tower's rect bigger one = tower's range
        :return: pygame Sprite()
        """
        range_sprite = pygame.sprite.Sprite()
        range_sprite.rect = pygame.Rect(self.rect.centerx - self.range, self.rect.centery - self.range, self.range * 2, self.range * 2.)
        return range_sprite

    def set_enemy_in_close_range(self, x):
        """
        Sets enemy in range
        :param x: bool
        :return: None
        """
        if self.enemy_in_close_range != x:
            self.enemy_in_close_range = x

    def set_enemy_in_range(self, x):
        """
        Sets enemy in range
        :param x: bool
        :return: None
        """
        if self.enemy_in_range != x:
            self.enemy_in_range = x

    def set_being_dragged(self, x):
        """
        Indicates whether a sprite is being dragged.
        :param x: bool
        :return: None
        """
        if self.being_dragged != x:
            self.being_dragged = x

    def set_archer_flipped(self, x):
        """
        Flips the archers image.
        :param x: bool
        :return: None
        """
        self.flipped = x

    def attack(self, enemy):
        """
        Attack logic goes here.
        :param enemy:
        :return:
        """
        pass

    def shoot(self):
        """
        Shoot logic goes here.
        :return:
        """
        pass

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
            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                self.animation(surface)

    def animation(self, surface):
        """
        All animation logic goes here.
        :param surface: pygame Surface()
        :return: None
        """

        if self.shoot_index >= len(self.shoot_list):
            self.shoot_index = 0
        if self.animation_index >= len(self.animation_list):
            pygame.mixer.Sound.play(self.sound_bow)
            self.animation_index = 0

        arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))
        archer = pygame.transform.scale(self.animation_list[self.animation_index], (self.archer_rect.width, self.archer_rect.height))

        if self.enemy_in_range:
            if time.time() - self.timer > 0.15:
                self.shoot_index += 1
                self.animation_index += 1
                self.timer = time.time()
        else:
            arrow = pygame.transform.scale(self.shoot_list[0], (0, 0))
            archer = pygame.transform.scale(self.animation_list[0], (self.archer_rect.width, self.archer_rect.height))

        if self.flipped:  # if the enemy is left
            surface.blit(arrow, self.arrow_rect)
            self.arrow_rect.x = self.archer_rect.topleft[0] - self.archer_rect.width // 2
            surface.blit(pygame.transform.flip(archer, True, False), self.archer_rect)

        else:  # if the enemy is right
            self.arrow_rect.x = self.archer_rect.topright[0]
            surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)
            surface.blit(archer, self.archer_rect)

    def click(self, x, y):
        """
        All logic when the tower is clicked
        :param x: int
        :param y: int
        :return: bool
        """
        if self.rect.collidepoint(x, y):
            if self.clicked:
                self.clicked = False
                return True
            else:
                self.clicked = True
                return True


class TowerArcher1(Tower):
    """
    Tower subclass
    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_archer[4], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[6], (self.width, self.height))
        self.animation_list = global_variables.towers_archer[38:43]
        self.shoot_list = global_variables.towers_archer[77:82]

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """
        if not self.in_position:
            self.in_position = True
            self.archer_rect = pygame.Rect(self.rect.x + 20, self.rect.y - 36, 45, 45)
            self.arrow_rect = pygame.Rect(self.archer_rect.topright[0], self.archer_rect.y - 30, 30, 30)


class TowerArcher2(Tower):
    """
        Tower subclass
    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_archer[7], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[8], (self.width, self.height))
        self.animation_list = global_variables.towers_archer[38:43]
        self.shoot_list = global_variables.towers_archer[77:82]
        # Tower stuff
        self.range = 130
        self.damage = 3
        self.rate = 0.7
        self.price = 2
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """
        if not self.in_position:
            self.in_position = True
            self.archer_rect = pygame.Rect(self.rect.x + 20, self.rect.y - 24, 45, 45)
            self.arrow_rect = pygame.Rect(self.archer_rect.topright[0], self.archer_rect.y - 30, 30, 30)


class TowerArcher3(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_archer[9], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[10], (self.width, self.height))
        self.animation_list = global_variables.towers_archer[51:56]
        self.shoot_list = global_variables.towers_archer[77:82]
        # Tower stuff
        self.range = 140
        self.damage = 5
        self.rate = 0.6
        self.price = 3
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """
        if not self.in_position:
            self.in_position = True
            self.archer_rect = pygame.Rect(self.rect.x + 20, self.rect.y - 24, 45, 45)
            self.arrow_rect = pygame.Rect(self.archer_rect.topright[0], self.archer_rect.y - 30, 30, 30)


class TowerArcher4(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_archer[11], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[12], (self.width, self.height))
        self.animation_list = global_variables.towers_archer[64:69]
        self.shoot_list = global_variables.towers_archer[77:82]
        # Tower stuff
        self.range = 150
        self.damage = 7
        self.rate = 0.5
        self.price = 4
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """
        if not self.in_position:
            self.in_position = True
            self.archer_rect = pygame.Rect(self.rect.x + 20, self.rect.y - 24, 45, 45)
            self.arrow_rect = pygame.Rect(self.archer_rect.topright[0], self.archer_rect.y - 30, 30, 30)


class TowerMagic1(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_magic[2], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_magic[3], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.freeze
        # Tower stuff
        self.range = 120
        self.damage = 8
        self.rate = 0.8
        self.price = 5
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 15, self.height + 15)
            self.arrow_rect.centerx = x
            self.arrow_rect.centery = y

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if self.enemy_in_range:
                    if time.time() - self.timer > 0.15:
                        self.shoot_index += 1
                        self.timer = time.time()
                else:
                    self.shoot_index = 0

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerMagic2(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_magic[6], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_magic[7], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.freeze
        # Tower stuff
        self.range = 130
        self.damage = 12
        self.rate = 0.7
        self.price = 6
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 15, self.height + 15)
            self.arrow_rect.centerx = x
            self.arrow_rect.centery = y

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if self.enemy_in_range:
                    if time.time() - self.timer > 0.15:
                        self.shoot_index += 1
                        self.timer = time.time()
                else:
                    self.shoot_index = 0

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerMagic3(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_magic[11], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_magic[12], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.freeze
        # Tower stuff
        self.range = 140
        self.damage = 16
        self.rate = 0.6
        self.price = 7
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 5, self.height + 5)
            self.arrow_rect.centerx = x
            self.arrow_rect.centery = y

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if self.enemy_in_range:
                    if time.time() - self.timer > 0.15:
                        self.shoot_index += 1
                        self.timer = time.time()
                else:
                    self.shoot_index = 0

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerMagic4(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_magic[16], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_magic[17], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.fire[19:27]
        # Tower stuff
        self.range = 150
        self.damage = 30
        self.rate = 0.5  # in seconds
        self.price = 8
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 5, self.height + 5)
            self.arrow_rect.centerx = x
            self.arrow_rect.centery = y

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if self.enemy_in_range:
                    if time.time() - self.timer > 0.15:
                        self.shoot_index += 1
                        self.timer = time.time()
                else:
                    self.shoot_index = 0

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerStone1(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_stone[3], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_stone[6], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.stone
        # Tower stuff
        self.range = 120
        self.damage = 10
        self.rate = 0.8
        self.price = 9
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 5, self.height * 2.5)
            self.arrow_rect.midbottom = (x, y)

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if time.time() - self.timer > 0.10:
                    self.shoot_index += 1
                    self.timer = time.time()

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerStone2(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_stone[6], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_stone[7], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.stone
        # Tower stuff
        self.range = 130
        self.damage = 12
        self.rate = 0.7
        self.price = 10
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 5, self.height * 2.5)
            self.arrow_rect.midbottom = (x, y)

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if time.time() - self.timer > 0.10:
                    self.shoot_index += 1
                    self.timer = time.time()

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerStone3(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_stone[12], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_stone[13], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.stone
        # Tower stuff
        self.range = 140
        self.damage = 18
        self.rate = 0.7
        self.price = 11
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 5, self.height * 2.5)
            self.arrow_rect.midbottom = (x, y)

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if time.time() - self.timer > 0.10:
                    self.shoot_index += 1
                    self.timer = time.time()

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerStone4(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_stone[16], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_stone[17], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.stone
        # Tower stuff
        self.range = 150
        self.damage = 24
        self.rate = 0.5
        self.price = 12
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 5, self.height * 2.5)
            self.arrow_rect.midbottom = (x, y)

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if time.time() - self.timer > 0.10:
                    self.shoot_index += 1
                    self.timer = time.time()

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerSupport1(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_support[1], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_support[2], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.time[0:14]
        # Tower stuff
        self.range = 120
        self.damage = 4
        self.rate = 0.8
        self.price = 13
        self.bullets = []

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if self.enemy_in_range:
                    if time.time() - self.timer > 0.15:
                        self.shoot_index += 1
                        self.timer = time.time()
                else:
                    self.shoot_index = 0

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width, self.height)
            self.arrow_rect.centerx = x
            self.arrow_rect.centery = y


class TowerSupport2(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_support[4], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_support[5], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.time[0:14]
        # Tower stuff
        self.range = 130
        self.damage = 6
        self.rate = 0.7
        self.price = 14
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 5, self.height + 5)
            self.arrow_rect.centerx = x
            self.arrow_rect.centery = y

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if self.enemy_in_range:
                    if time.time() - self.timer > 0.15:
                        self.shoot_index += 1
                        self.timer = time.time()
                else:
                    self.shoot_index = 0

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerSupport3(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_support[7], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_support[8], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.time[0:14]
        # Tower stuff
        self.range = 140
        self.damage = 8
        self.rate = 0.6
        self.price = 15
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 10, self.height + 10)
            self.arrow_rect.centerx = x
            self.arrow_rect.centery = y

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if self.enemy_in_range:
                    if time.time() - self.timer > 0.15:
                        self.shoot_index += 1
                        self.timer = time.time()
                else:
                    self.shoot_index = 0

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)


class TowerSupport4(Tower):
    """
        Tower subclass

    """

    def __init__(self, x, y, game_map):
        super().__init__(x, y, game_map)
        self.image = pygame.transform.scale(global_variables.towers_support[10], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_support[11], (self.width, self.height))
        self.animation_list = []
        self.shoot_list = global_variables.time[0:14]
        # Tower stuff
        self.range = 150
        self.damage = 10
        self.rate = 0.5
        self.price = 16
        self.bullets = []

    def set_in_position(self):
        """
        Spawn the archer after the tower is set in position on the board.
        :return: None
        """

        distance_min = 1000
        x, y = 0, 0
        if not self.in_position:
            for point in global_variables.game_settings[self.game_map][4]:
                distance = math.sqrt((point[0] - self.rect.x) ** 2 + (point[1] - self.rect.y) ** 2)
                if distance < distance_min:
                    distance_min = distance
                    x, y = point[0], point[1]
            self.in_position = True
            self.arrow_rect = pygame.Rect(0, 0, self.width + 15, self.height + 15)
            self.arrow_rect.centerx = x
            self.arrow_rect.centery = y

    def draw(self, surface, game_state):
        """
        All tower's drawing logic goes here.
        :param surface: pygame Surface()
        :param game_state: int
        :return: None
        """
        if game_state == 2:

            if self.clicked:
                circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
                pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
                surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
            surface.blit(self.image, self.rect)
            if self.in_position:
                if self.shoot_index >= len(self.shoot_list):
                    self.shoot_index = 0

                arrow = pygame.transform.scale(self.shoot_list[self.shoot_index], (self.arrow_rect.width, self.arrow_rect.height))

                if self.enemy_in_range:
                    if time.time() - self.timer > 0.15:
                        self.shoot_index += 1
                        self.timer = time.time()
                else:
                    self.shoot_index = 0

                if self.flipped:  # if the enemy is left
                    surface.blit(arrow, self.arrow_rect)

                else:  # if the enemy is right
                    surface.blit(pygame.transform.flip(arrow, True, False), self.arrow_rect)
