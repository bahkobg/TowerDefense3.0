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
        self.shoot_index = 0
        self.img_list = []
        self.upg_list = []
        self.shoot_list = []
        self.flipped = False
        self.paused = False
        self.timer = time.time()
        self.enemy_in_range = False
        self.image_shoot = None

    def set_enemy_in_range(self, x):
        """
        Sets enemy in range
        :param x: bool
        :return: None
        """
        if self.enemy_in_range != x:
            self.enemy_in_range = x

    def draw(self, surface):
        if self.shoot_index >= len(self.shoot_list):
            self.shoot_index = 0
        if self.animation_index >= len(self.img_list):
            pygame.mixer.Sound.play(self.sound_bow)
            self.animation_index = 0

        self.image_shoot = self.shoot_list[self.shoot_index]
        self.image = pygame.transform.scale(self.img_list[self.animation_index], (self.width, self.height))

        if self.enemy_in_range:
            if time.time() - self.timer > 0.15:
                self.shoot_index += 1
                self.animation_index += 1
                self.timer = time.time()
        else:
            self.image_shoot = self.shoot_list[0]
            self.image = pygame.transform.scale(self.img_list[0], (self.width, self.height))

        if self.flipped:  # if the enemy is left
            surface.blit(self.image_shoot, (self.x - 25, self.y - 25))
            surface.blit(pygame.transform.flip(self.image, True, False), self.rect)

        else:  # if the enemy is right
            surface.blit(pygame.transform.flip(self.image_shoot, True, False), (self.x + 50, self.y - 25))
            surface.blit(self.image, self.rect)


class ArcherArcherTower(Archer):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img_list = global_variables.towers_archer[38:44]
        self.upg_list_1 = global_variables.towers_archer[51:56]
        self.upg_list_2 = global_variables.towers_archer[64:69]
        self.shoot_list = [pygame.transform.scale(global_variables.towers_archer[35], (5 * x, 5 * x)) for x in range(6)]


class ArcherMagicTower(Archer):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img_list = [global_variables.towers_magic[27]]
        self.upg_list_1 = global_variables.towers_magic[28]
        self.upg_list_2 = global_variables.towers_magic[29]
        self.shoot_list = global_variables.towers_magic[19:26]
        self.width = 34
        self.height = 55


class ArcherStoneTower(Archer):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img_list = global_variables.towers_stone[27:28]
        self.upg_list_1 = global_variables.towers_stone[4:5]
        self.upg_list_2 = global_variables.towers_stone[10:11]
        self.shoot_list_1 = global_variables.towers_stone[29:34]
        self.shoot_list_2 = global_variables.towers_stone[35:39]
        self.shoot_list = global_variables.towers_stone[40:44]
        self.width = 66
        self.height = 97


class ArcherSupportTower(Archer):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img_list = [global_variables.towers_support[16]]
