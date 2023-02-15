import pygame
from ld_img import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tiles_group, all_sprites, kratnostb):
        super().__init__(tiles_group, all_sprites)
        self.image = load_image('block.png')
        self.image = pygame.transform.scale(self.image, (15 * kratnostb, 15 * kratnostb))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(15 * kratnostb * pos_x, 15 * kratnostb * pos_y)


class Tron(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, side, tron_group, all_sprites, kratnostb):
        super().__init__(tron_group, all_sprites)
        self.image = load_image('tron.png')
        self.image = pygame.transform.scale(self.image, (45 * kratnostb, 45 * kratnostb))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.hp = 3000
        # нужно сделать разный цвет или разные картинки по переменной side


class Towers(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, side, tower_group, all_sprites, kratnostb):
        super().__init__(tower_group, all_sprites)
        self.delay_attack = 100
        self.image = load_image('tower.png')
        self.image = pygame.transform.scale(self.image, (25 * kratnostb, 25 * kratnostb))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.hp = 1000
        self.target = None
        # нужно сделать разный цвет или разные картинки по переменной side

    def check_collide(self, grounitov):
        '''
        возвращает юнит находящийся в радиусе башни
        1.5 - кратность радиуса
        '''
        return pygame.sprite.spritecollideany(self, grounitov, pygame.sprite.collide_circle_ratio(1.5))
