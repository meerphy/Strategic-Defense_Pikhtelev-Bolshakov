import pygame


class Cur(pygame.sprite.Sprite):
    def __init__(self, x, y, im, spt):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(im).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(self.x + 50, self.y + 50))
        self.add(spt)

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
