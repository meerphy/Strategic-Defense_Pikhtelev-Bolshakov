import pygame
import math
from PIL import Image
from main import Uni
from worker import Worker

class Trone(pygame.sprite.Sprite):
    def __init__(self, x, y, im, spt):
        self.x = x
        self.y = y
        self.h = 0
        self.hp = 3000
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(im).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect(center=(self.x + 50, self.y + 50))
        self.add(spt)
        self.k = 0

    def spawner(self, g, res):
        if res >= 50:
            Worker(self.x + 150, self.y + 150, 'ima/test.png', g)
            return res - 50