import pygame
import math
from PIL import Image
from main import Uni

class Worker(Uni):
    def __init__(self, x, y, im, spt):
        Uni.__init__(self, x, y, im, spt)

    def startwork(self):
        print("работа началась")
    def build(self, ob, im, spt):
        self.need_x = self.x
        self.need_y = self.y
        return ob(self.x, self.y, im, spt)

    def dob(self, res):
        self.chos = 0
        self.shahta = res
        self.resors = res.resors