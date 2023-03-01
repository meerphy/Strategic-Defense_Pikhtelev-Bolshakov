from main import Uni


class Enemy(Uni):
    def __init__(self, x, y, im, spt, tip, g1, g2):
        Uni.__init__(self, x, y, im, spt, 1, tip, g1, g2)
