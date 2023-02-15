import pygame
from worker import Worker
from table_res import Clres, Res
from builds import Tile, Tron, Towers
from menu import start_screen

kratnostb = 5
kolvo_golda = 99
kolvo_aluminum = 99
kolvo_titan = 99


def generate_map():
    for y in range(17):
        for x in range(26):
            Tile(x, y, tiles_group, all_sprites, kratnostb)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = -50 * kratnostb
        self.dy = -50 * kratnostb
        self.apply(all_sprites, self.dx, self.dy)

    def apply(self, obj, x, y):
        for sprite in obj:
            sprite.rect.x += x
            sprite.rect.y += y


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Strategic Defense')
    res = 100
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = pygame.time.Clock()
    size = width, height = 1300, 858
    screen = pygame.display.set_mode(size)
    fps = 240

    pygame.mixer.music.load('data/music1.mp3')
    pygame.mixer.music.set_volume(.01)
    pygame.mixer.music.play(-1)

    while True:
        status = start_screen(screen, width, height, clock, fps)
        if status == 'duo':
            pass              #подключить сетевую часть
        elif status == 'settings':
            pass
        else:
            break

    grozdaniy = pygame.sprite.Group()
    grounitov = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    tron_group = pygame.sprite.Group()
    tower_group = pygame.sprite.Group()

    font_res = pygame.font.Font(None, 40)
    resourse_group = pygame.sprite.Group()
    res_table = Res(100 * 5, 2 * 5, 'res.png', resourse_group)
    golda = Clres(102 * 5, 4.7 * 5, 'gold.png', resourse_group)
    aluminum = Clres(115.5 * 5, 4.5 * 5, 'aluminum.png', resourse_group)
    titan = Clres(129.5 * 5, 4.5 * 5, 'titan.png', resourse_group)
    font_golda = font_res.render(str(kolvo_golda), True, (0, 0, 0))
    font_aluminum = font_res.render(str(kolvo_aluminum), True, (0, 0, 0))
    font_titan = font_res.render(str(kolvo_titan), True, (0, 0, 0))

    generate_map()
    tron_left = Tron(5 * kratnostb, 205 * kratnostb, 'left', tron_group, all_sprites, kratnostb)
    tron_right = Tron(340 * kratnostb, 5 * kratnostb, 'right', tron_group, all_sprites, kratnostb)

    towers_left = {}
    towers_left[0] = Towers(5 * kratnostb, 165 * kratnostb, 'левый', tower_group, all_sprites, kratnostb)
    towers_left[1] = Towers(70 * kratnostb, 165 * kratnostb, 'левый', tower_group, all_sprites, kratnostb)
    towers_left[2] = Towers(70 * kratnostb, 225 * kratnostb, 'левый', tower_group, all_sprites, kratnostb)
    towers_left[3] = Towers(35 * kratnostb, 195 * kratnostb, 'левый', tower_group, all_sprites, kratnostb)

    towers_right = {}
    towers_right[0] = Towers(295 * kratnostb, 5 * kratnostb, 'левый', tower_group, all_sprites, kratnostb)
    towers_right[1] = Towers(295 * kratnostb, 60 * kratnostb, 'левый', tower_group, all_sprites, kratnostb)
    towers_right[2] = Towers(360 * kratnostb, 60 * kratnostb, 'левый', tower_group, all_sprites, kratnostb)
    towers_right[3] = Towers(330 * kratnostb, 30 * kratnostb, 'левый', tower_group, all_sprites, kratnostb)

    grores = pygame.sprite.Group()
    mu = Worker(200, 150, 'data/samolet.png', grounitov, all_sprites)
    my = Worker(200, 50, 'data/samolet.png', grounitov, all_sprites)
    k = 0
    camera = Camera()
    moving = False

    running = True
    while running:
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
                if event.key == pygame.K_RIGHT:
                    camera.apply(all_sprites, -100, 0)
                    camera.apply(grounitov, -100, 0)
                if event.key == pygame.K_DOWN:
                    camera.apply(all_sprites, 0, -100)
                    camera.apply(grounitov, 0, -100)
                if event.key == pygame.K_UP:
                    camera.apply(all_sprites, 0, 100)
                    camera.apply(grounitov, 0, 100)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                moving = True
            if event.type == pygame.MOUSEMOTION:
                if moving:
                    x_new, y_new = event.rel
                    camera.apply(all_sprites, x_new, y_new)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                moving = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in grounitov:
                        if i.rect.collidepoint(pygame.mouse.get_pos()):
                            i.chos()
                    if flag == 0:
                        for i in grozdaniy:
                            if i.rect.collidepoint(pygame.mouse.get_pos()):
                                res = i.spawner(grounitov, res)
                                print(1)
                                flag = 1
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
        grounitov.update(0)

        for tower in tower_group:
            col_unit = tower.check_collide(grounitov)
            '''
            происходит нанесение урона юниту, если он в радиусе атаки башни
            сделано замеделение нанесения урона, чтобы не было слишком быстро
            '''
            if col_unit:
                if not tower.target or not (col_unit == tower.target or pygame.sprite.collide_circle(tower, tower.target)):
                    tower.target = col_unit
                if tower.delay_attack == 300:
                    tower.delay_attack = 0
                    print(tower.target.hp)
                    tower.target.hp -= 15
                    if tower.target.hp <= 0:
                        tower.target.kill()
                        tower.target = None
                else:
                    tower.delay_attack += 1
        all_sprites.draw(screen)
        resourse_group.draw(screen)
        screen.blit(font_golda, (109.5 * 5, 5.7 * 5))
        screen.blit(font_aluminum, (122.5 * 5, 5.7 * 5))
        screen.blit(font_titan, (136.7 * 5, 5.7 * 5))
        grounitov.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
