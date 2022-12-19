import pygame
import math
from PIL import Image

class Uni(pygame.sprite.Sprite):
    def __init__(self, x, y, im, spt):
        self.x = x
        self.y = y
        self.h = 0
        self.v = pygame.Vector2()
        self.v.x = x + 50
        self.na = im
        self.v.y = y + 50
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(im).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x + 50, self.y + 50))
        self.original_image = self.image
        self.need_y = self.y
        self.need_x = self.x
        self.add(spt)
        self.k = 0

    def rotate(self, position):
        if self.h == 1:
            mousex, mousey = position
            angle = 10.
            self.need_y = mousey
            self.need_x = mousex
            rel_x, rel_y = mousex - self.x, mousey - self.y
            angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            print(int(angle))
            if abs(int(angle)) > 90:
                self.image = pygame.transform.flip(self.image, 0, 1)
            self.image = pygame.transform.rotate(self.image, int(angle))

    def updatepos(self, speed):
        if self.h == 1:
            if self.need_y != self.y or self.need_x != self.x:
                self.v.x = self.need_x - self.x
                self.v.y = self.need_y - self.y
                self.x = int(0.05 * self.v.x * self.k) + self.x
                self.y = int(0.05 * self.v.y * self.k) + self.y
                self.rect.y = self.y - 150
                self.rect.x = self.x - 150
                pygame.time.wait(speed)
                self.k += 1
            else:
                self.k = 0
                self.image = self.original_image

    def new(self):
        self.image = self.original_image

    def chos(self):
        self.h = (self.h + 1) % 2

