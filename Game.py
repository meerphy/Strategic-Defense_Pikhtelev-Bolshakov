import pygame
import math
from PIL import Image
from main import Uni
from worker import Worker
from building import Trone
pygame.init()
res = 100
pygame.time.set_timer(pygame.USEREVENT, 1000)
clock = pygame.time.Clock()
sz = pygame.display.set_mode((1920, 1024), pygame.RESIZABLE)
surf = pygame.Surface((100, 100))
surf.fill((255, 255, 255))
snus = pygame.Surface((100, 100))
snus.fill((0, 0, 0))
grounitov = pygame.sprite.Group()
grozdaniy = pygame.sprite.Group()
grores = pygame.sprite.Group()
bg = pygame.image.load("ima/bg.jpg").convert()
bg = pygame.transform.scale(bg, (1920, 1024))
mu = Worker(200, 150, 'ima/test.png', grounitov)
my = Worker(200, 50, 'ima/test.png', grounitov)
pygame.display.set_caption("My dream")
k = 0
while 1:
    flag = 0
    sz.blit(bg, (0, 0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            print(event)
        if event.type == pygame.USEREVENT:
            sum = 0
            for i in grores:
                if i.isworkon:
                    sum += 1
            res += 1 * sum
            print("данные посланы")
            #база данных передаётся в сеть и забирается из сервера
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in grounitov:
                    if i.rect.collidepoint(pygame.mouse.get_pos()):
                        if keys[pygame.K_LALT]:
                            i.build(Trone, "ima/trone.png", grozdaniy)
                            flag = 1
                        else:
                            i.chos()
                if flag == 0:
                    for i in grozdaniy:
                        if i.rect.collidepoint(pygame.mouse.get_pos()):
                            res = i.spawner(grounitov, res)
                            flag = 1
            if event.button == 3:
                if keys[pygame.K_LALT]:
                    for i in grores:
                        if i.rect.collidepoint(pygame.mouse.get_pos()):
                            if i.isworkon == 0:
                                for k in grounitov:
                                    if k.rect.collidepoint(pygame.mouse.get_pos()) and k.chos == 1:
                                        k.dob(res)
                                        i.work()
                else:
                    for i in grounitov:
                        i.new()
                        i.rotate(pygame.mouse.get_pos())
                        i.k = 0

    for i in grounitov:
        i.updatepos(0)
    grozdaniy.draw(sz)
    grounitov.draw(sz)
    clock.tick(60)
    pygame.display.update()