import pygame
from ld_img import load_image


class Resourse(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img, resourse_group, all_sprites, kratnostb):
        super().__init__(resourse_group, all_sprites)
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, (35 * kratnostb, 35 * kratnostb))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
