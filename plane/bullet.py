from plane.flyobject import Flyobject


class Bullet(Flyobject):
    def __init__(self, screen, image, x, y):
        x = x
        y = y
        super(Bullet, self).__init__(screen, x, y, image)

    def __str__(self):
        return "子弹:(%d,%d)" % (self.x, self.y)

    def step(self):
        self.y -= 3

    def outOfBounds(self):
        return self.y > 0
