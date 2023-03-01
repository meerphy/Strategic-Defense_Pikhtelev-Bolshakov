import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Towers(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, side, g1, g2):
        super().__init__(g1, g2)
        self.image = load_image('tower.png')
        self.image = pygame.transform.scale(self.image, (25 * 5, 25 * 5))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.hp = 1000
        # нужно сделать разный цвет или разные картинки по переменной side