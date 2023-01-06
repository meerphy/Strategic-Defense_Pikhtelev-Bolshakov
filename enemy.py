from main import Uni


class Enemy(Uni):
    def __init__(self, x, y, im, spt):
        Uni.__init__(self, x, y, im, spt, 1)
