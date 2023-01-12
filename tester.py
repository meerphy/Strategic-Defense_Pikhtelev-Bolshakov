from socket import *
import pygame
import os
import sys
from worker import Worker
from resourse import Resorse
from building import Trone
from enemy import Enemy
from but import Button
from cursor import Cur
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
        # нужно сделать разный цвет или разные картинки по переменной side


class Towers(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, side, g1, g2):
        super().__init__(g1, g2)
        self.image = load_image('tower.png')
        self.image = pygame.transform.scale(self.image, (25 * kratonostb, 25 * kratonostb))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.hp = 1000
        # нужно сделать разный цвет или разные картинки по переменной side


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = -100 * kratonostb
        self.dy = -20 * kratonostb
        self.apply(all_sprites, self.dx, self.dy)

    def apply(self, obj, x, y):
        for sprite in obj:
            sprite.rect.x += x
            sprite.rect.y += y

gs = socket(AF_INET, SOCK_STREAM)
gs.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
gs.connect(("localhost", 9999))
star = ""
while star != "Start":
    star = gs.recv(1024).decode()
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Strategic Defense')
    res = 100
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    enemy_group = pygame.sprite.Group()
    grozdaniy = pygame.sprite.Group()
    grounitov = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    tron_group = pygame.sprite.Group()
    tower_group = pygame.sprite.Group()

    size = width, height = 1300, 700
    screen = pygame.display.set_mode(size)

    generate_map()
    tron_left = Trone(5 * kratonostb, 205 * kratonostb, "data/tron.png", grozdaniy, all_sprites)
    tron_right = Trone(340 * kratonostb, 5 * kratonostb, "data/tron.png", grozdaniy, all_sprites)

    towers_left = {}
    towers_left[0] = Towers(5 * kratonostb, 165 * kratonostb, 'левый', tower_group, all_sprites)
    towers_left[1] = Towers(70 * kratonostb, 165 * kratonostb, 'левый', tower_group, all_sprites)
    towers_left[2] = Towers(70 * kratonostb, 225 * kratonostb, 'левый', tower_group, all_sprites)
    towers_left[3] = Towers(35 * kratonostb, 195 * kratonostb, 'левый', tower_group, all_sprites)

    towers_right = {}
    towers_right[0] = Towers(295 * kratonostb, 5 * kratonostb, 'левый', tower_group, all_sprites)
    towers_right[1] = Towers(295 * kratonostb, 60 * kratonostb, 'левый', tower_group, all_sprites)
    towers_right[2] = Towers(360 * kratonostb, 60 * kratonostb, 'левый', tower_group, all_sprites)
    towers_right[3] = Towers(330 * kratonostb, 30 * kratonostb, 'левый', tower_group, all_sprites)
    menu = pygame.sprite.Group()
    grores = pygame.sprite.Group()
    curs_grou = pygame.sprite.Group()
    menu_b = Button(560, 570, "data/menu.png", menu)
    dob_butto = Button(1120, 570, "data/zn_dob.png", menu)
    btow_butto = Button(900, 570, "data/zn_towera.png", menu)
    mu = Worker(700, 150, 'data/samolet.png', grounitov, tower_group, all_sprites)
    my = Worker(700, 50, 'data/samolet.png', grounitov, tower_group, all_sprites)
    k = 0
    camera = Camera()
    fps = 240
    ndb = 0
    ntb = 0
    moving = False
    running = True
    while running:
        d = []
        flag = 0
        keys = pygame.key.get_pressed()
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    camera.apply(all_sprites, 100, 0)
                    camera.apply(grounitov, 100, 0)
                    camera.apply(enemy_group, 100, 0)
                if event.key == pygame.K_RIGHT:
                    camera.apply(all_sprites, -100, 0)
                    camera.apply(grounitov, -100, 0)
                    camera.apply(enemy_group, -100, 0)
                if event.key == pygame.K_DOWN:
                    camera.apply(all_sprites, 0, -100)
                    camera.apply(grounitov, 0, -100)
                    camera.apply(enemy_group, 0, -100)
                if event.key == pygame.K_UP:
                    camera.apply(all_sprites, 0, 100)
                    camera.apply(grounitov, 0, 100)
                    camera.apply(enemy_group, 0, 100)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(tron_left.rect)
                    if ntb == 1:
                        for i in grounitov:
                            i.new()
                            i.rotate(pygame.mouse.get_pos())
                            if i.h:
                                i.buil == 1
                                curs.kill()
                                pygame.mouse.set_visible(True)
                    for i in grounitov:
                        if i.rect.collidepoint(pygame.mouse.get_pos()):
                            i.chos()

                    if flag == 0:
                        for i in grozdaniy:
                            if i.rect.collidepoint(pygame.mouse.get_pos()):
                                res = i.spawner(grounitov, res)
                                print(1)
                                flag = 1
                        for i in menu:
                            if i.rect.collidepoint(pygame.mouse.get_pos()):
                                pygame.mouse.set_visible(False)
                                if i == dob_butto:
                                    ndb = 1
                                    curs = Cur(20, 20, "data/dob.png", curs_grou)
                                if i == btow_butto:
                                    ntb = 1
                                    curs = Cur(20, 20, "data/ctoow.png", curs_grou)

                if event.button == 3:
                    if keys[pygame.K_LALT]:
                        for i in grores:
                            print(1)
                            if i.rect.collidepoint(pygame.mouse.get_pos()):
                                print(2)
                                if i.isworkon < 3:
                                    print(3)
                                    for k in grounitov:
                                        print(4)
                                        if k.rect.collidepoint(pygame.mouse.get_pos()) and k.h == 1:
                                            print(5)
                                            k.dob(res)
                                            i.work()
                    else:
                        for i in grounitov:
                            i.new()
                            i.rotate(pygame.mouse.get_pos())
                            i.k = 0

        for i in grounitov:
            i.updatepos(0)
            d.append([i.tip, str(i.y), str(i.x)])
        for i in d:
            gs.send((' '.join(i) + ',').encode())
        dat = gs.recv(1024).decode()

        datas = dat.split(',')[:-1]
        enemy = datas.copy()
        print(datas)
        try:
            cl, x, y = datas[0].split()
            enemy_group.empty()
        except:
            pass
        for j in datas:
            try:
                cl, y, x = j.split()
                for i in grounitov:
                    if i.x == int(x) and i.y == int(y):
                        enemy.remove(j)
            except:
                pass
        for ene in enemy:
            try:
                cl, y, x = ene.split()
                if cl == 'Worker':
                    Enemy(int(x), int(y), "data/samolet.png", enemy_group, ene[0], all_sprites, Towers)
                    print("yay")
            except:
                pass
        flagok = 0
        for i in grounitov:
            if i.h == 1:
                flagok = 1
                break
        all_sprites.draw(screen)
        enemy_group.draw(screen)
        grounitov.draw(screen)
        if flagok == 1:
            menu.draw(screen)
        for i in curs_grou:
            i.update()
        curs_grou.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
