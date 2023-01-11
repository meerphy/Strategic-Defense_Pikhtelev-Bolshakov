import pygame
import math
from main import Uni


class Worker(Uni):
    def __init__(self, x, y, im, spt, g1, g2):
        Uni.__init__(self, x, y, im, spt, 0, "Worker", g1, g2)
        self.buil = 0

    def startwork(self):
        print("работа началась")

    def build(self, ob):
        print(1)
        self.need_x = self.x
        self.need_y = self.y
        ob(self.x, self.y, 1, self.g1, self.g2)

    def dob(self, res):
        self.h = 0
        self.shahta = res
        self.resors = res