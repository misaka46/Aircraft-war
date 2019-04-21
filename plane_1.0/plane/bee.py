import random
from flyingObject import FlyingObject
from award import Award


class Bee(FlyingObject, Award):

    def __init__(self, screen, image, t):
        x = random.randint(0, screen.get_rect()[2] - 60)
        y = -50
        super(Bee, self).__init__(screen, x, y, image)
        self.awardType = t
        self.index = True
        self.speed = [2,2]

    def outOfBounds(self):
        """是否越界"""
        return (self.y < 1000 )

    def step(self):
        """移动"""
        if self.x + self.width > 800:
            self.index = False
        if self.x + self.width <50:
            self.index = True
        if self.index == True:
            self.x += 3
        else:
            self.x -= 3
        self.y += 1  # 移动步数

    def getType(self):
        return self.awardType
