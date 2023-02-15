import pygame
import math
from uni import Uni


class Worker(Uni):
    def __init__(self, x, y, im, spt, spg):
        Uni.__init__(self, x, y, im, spt, spg)

    def startwork(self):
        print("работа началась")

    def build(self, ob, im, spt):
        self.need_x = self.x
        self.need_y = self.y
        return ob(self.x, self.y, im, spt)

    def dob(self, res):
        self.h = 0
        self.shahta = res
        self.resors = res
