import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False

        # Tower stuff
        self.radius = 60
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

    def update(self, *args):
        pass

    def draw(self):
        pass
