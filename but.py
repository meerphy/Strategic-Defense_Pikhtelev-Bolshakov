import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, im, g):
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
        self.add(g)

    def clicked(self, per):
        return (per + 1) % 2
