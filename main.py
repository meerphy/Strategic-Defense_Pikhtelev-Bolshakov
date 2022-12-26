import pygame
import os
import sys

kratonostb = 5


def generate_map():
    for y in range(17):
        for x in range(26):
            Tile(x, y)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = load_image('block.png')
        self.image = pygame.transform.scale(self.image, (15 * kratonostb, 15 * kratonostb))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(15 * kratonostb * pos_x, 15 * kratonostb * pos_y)


class Tron(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, side):
        super().__init__(tron_group, all_sprites)
        self.image = load_image('tron.png')
        self.image = pygame.transform.scale(self.image, (45 * kratonostb, 45 * kratonostb))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.hp = 3000
        #нужно сделать разный цвет или разные картинки по переменной side


class Towers(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, side):
        super().__init__(tower_group, all_sprites)
        self.image = load_image('tower.png')
        self.image = pygame.transform.scale(self.image, (25 * kratonostb, 25 * kratonostb))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.hp = 1000
        #нужно сделать разный цвет или разные картинки по переменной side


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = -50 * kratonostb
        self.dy = -50 * kratonostb
        self.apply(all_sprites, self.dx, self.dy)

    def apply(self, obj, x, y):
        for sprite in obj:
            sprite.rect.x += x
            sprite.rect.y += y


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Strategic Defense')

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    tron_group = pygame.sprite.Group()
    tower_group = pygame.sprite.Group()


    size = width, height = 1300, 858
    screen = pygame.display.set_mode(size)

    generate_map()
    tron_left = Tron(5 * kratonostb, 205 * kratonostb, "левый")
    tron_right = Tron(340 * kratonostb, 5 * kratonostb, "правый")

    towers_left = {}
    towers_left[0] = Towers(5 * kratonostb, 165 * kratonostb, 'левый')
    towers_left[1] = Towers(70 * kratonostb, 165 * kratonostb, 'левый')
    towers_left[2] = Towers(70 * kratonostb, 225 * kratonostb, 'левый')
    towers_left[3] = Towers(35 * kratonostb, 195 * kratonostb, 'левый')

    towers_right = {}
    towers_right[0] = Towers(295 * kratonostb, 5 * kratonostb, 'левый')
    towers_right[1] = Towers(295 * kratonostb, 60 * kratonostb, 'левый')
    towers_right[2] = Towers(360 * kratonostb, 60 * kratonostb, 'левый')
    towers_right[3] = Towers(330 * kratonostb, 30 * kratonostb, 'левый')

    camera = Camera()
    fps = 240
    clock = pygame.time.Clock()
    moving = False

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    camera.apply(all_sprites, 100, 0)
                if event.key == pygame.K_RIGHT:
                    camera.apply(all_sprites, -100, 0)
                if event.key == pygame.K_DOWN:
                    camera.apply(all_sprites, 0, -100)
                if event.key == pygame.K_UP:
                    camera.apply(all_sprites, 0, 100)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                moving = True
            if event.type == pygame.MOUSEMOTION:
                if moving:
                    x_new, y_new = event.rel
                    camera.apply(all_sprites, x_new, y_new)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                moving = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
