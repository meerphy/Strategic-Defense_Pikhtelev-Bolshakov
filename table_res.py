import pygame
from ld_img import load_image


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
