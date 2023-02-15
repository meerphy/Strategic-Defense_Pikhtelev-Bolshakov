import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Res(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, group):
        super().__init__(group)
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (45 * 5, 12 * 5))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)


class Clres(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, group):
        super().__init__(group)
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (7 * 5, 7 * 5))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
