import pygame
import global_variables


class Effect(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 150
        self.height = 450
        self.damage = None
        self.radius = None
        self.exploded = None
        self.image = None
        self.animation_index = 0

    def draw(self, surface):
        if self.animation_index >= 38:
            self.kill()
        else:
            self.image = pygame.transform.scale(global_variables.rain[self.animation_index], (self.width, self.height))
        surface.blit(self.image, (self.x, self.y))
        self.animation_index += 1
