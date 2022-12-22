import pygame
import math
from PIL import Image

class Resorse(pygame.sprite.Sprite):
    def __init__(self, x, y, im, spt):
        self.x = x
        self.y = y
        self.h = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(im).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.add(spt)
        self.rect = self.image.get_rect(center=(self.x + 50, self.y + 50))
        self.isworkon = 0
        self.resors = 'Med'
    def work(self):
        self.isworkon = 1
