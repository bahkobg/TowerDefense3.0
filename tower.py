import pygame
import global_variables


class Tower(pygame.sprite.Sprite):
    """
    Defines main tower class.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = 85
        self.height = 96
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False
        self.being_dragged = False
        self.image = None

        # Tower stuff
        self.range = 120
        self.damage = 1
        self.rate = 1
        self.price = 1
        self.bullets = []

    def get_nearest_enemy(self):
        pass

    def detect_enemy(self):
        pass

    def attack(self, enemy):
        pass

    def shoot(self):
        pass

    def animate(self):
        pass

    def drag(self, center):
        self.rect.center = center

    def update(self, *args):
        pass

    def draw(self, surface):
        if self.clicked:
            circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
            pygame.draw.circle(circle_surface, (128, 128, 128, 128), (self.range, self.range), self.range, 0)
            surface.blit(circle_surface, (self.rect.center[0] - self.range, self.rect.center[1] - self.range))
        surface.blit(self.image, self.rect)

    def click(self, x, y):
        if self.rect.collidepoint(x, y):
            if self.clicked:
                self.clicked = False
                return True
            else:
                self.clicked = True
                return True


class TowerArcher1(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(global_variables.towers_archer[4], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[6], (self.width, self.height))


class TowerArcher2(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(global_variables.towers_archer[7], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[8], (self.width, self.height))
        # Tower stuff
        self.range = 130
        self.damage = 2
        self.rate = 1
        self.price = 2
        self.bullets = []


class TowerArcher3(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(global_variables.towers_archer[9], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[10], (self.width, self.height))
        # Tower stuff
        self.range = 140
        self.damage = 3
        self.rate = 1
        self.price = 3
        self.bullets = []


class TowerArcher4(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(global_variables.towers_archer[11], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[12], (self.width, self.height))
        # Tower stuff
        self.range = 150
        self.damage = 4
        self.rate = 1
        self.price = 4
        self.bullets = []


class TowerMagic1(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(global_variables.towers_archer[2], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[3], (self.width, self.height))
        # Tower stuff
        self.range = 120
        self.damage = 5
        self.rate = 1
        self.price = 5
        self.bullets = []


class TowerMagic2(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(global_variables.towers_archer[6], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[7], (self.width, self.height))
        # Tower stuff
        self.range = 130
        self.damage = 6
        self.rate = 1
        self.price = 6
        self.bullets = []


class TowerMagic3(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(global_variables.towers_archer[11], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[12], (self.width, self.height))
        # Tower stuff
        self.range = 140
        self.damage = 7
        self.rate = 1
        self.price = 7
        self.bullets = []


class TowerMagic4(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(global_variables.towers_archer[16], (self.width, self.height))
        self.image_upgrade = pygame.transform.scale(global_variables.towers_archer[17], (self.width, self.height))
        # Tower stuff
        self.range = 150
        self.damage = 8
        self.rate = 1
        self.price = 8
        self.bullets = []
