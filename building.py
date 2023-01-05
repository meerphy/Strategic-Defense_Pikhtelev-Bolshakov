import pygame
import math
from main import Uni
from worker import Worker


class Trone(pygame.sprite.Sprite):
    def __init__(self, x, y, im, spt, spg):
        super().__init__(spt, spg)
        self.x = x
        self.y = y
        self.h = 0
        self.hp = 3000
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(im).convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.rect = self.image.get_rect(center=(self.x + 50, self.y + 50))
        self.add(spt)
        self.k = 0

    def spawner(self, g, res):
        if res >= 50:
            Worker(self.x + 150, self.y + 150, 'data/samolet.png', g)
            print(self.x + 150, self.y + 150)
            return res - 50
        else:
            return res
