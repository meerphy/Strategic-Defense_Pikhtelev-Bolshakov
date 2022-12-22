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
        self.image = pygame.transform.scale(self.image, (150, 150))
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
            koff = self.need_x - self.x
            if self.need_y != self.y or self.need_x != self.x:
                self.v.x = self.need_x - self.x
                self.v.y = self.need_y - self.y
                self.xi = int(0.001 * self.v.x * self.k)
                self.yi = int(0.001 * self.v.y * self.k)
                if self.xi > 5 and self.need_x != self.x and self.need_x > self.x:
                    self.x += 1
                else:
                    self.x += self.xi
                if self.yi > 5 and self.need_y != self.y and self.need_y > self.y:
                    self.y += 1
                else:
                    self.y += self.yi
                if self.xi < 5 and self.need_x != self.x and self.need_x < self.x:
                    self.x -= 1
                else:
                    self.x += self.xi
                if self.yi < 5 and self.need_y != self.y and self.need_y < self.y:
                    self.y -= 1
                else:
                    self.y += self.yi
                if ((abs(self.y) - abs(self.need_y) == 1 or abs(self.y) - abs(self.need_y) == -1) and
                    (abs(self.x) - abs(self.need_x) == 1 or abs(self.x) - abs(self.need_x) == -1)):
                    self.need_y = self.y
                    self.need_x = self.x
                self.rect.y = self.y - 60
                self.rect.x = self.x - 60
                pygame.time.wait(speed)
                self.k += 1
            else:
                self.k = 0
                self.image = self.original_image

    def new(self):
        self.image = self.original_image

    def chos(self):
        self.h = (self.h + 1) % 2

