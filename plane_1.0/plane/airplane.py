import random
from flyingObject import FlyingObject
from enemy import Enemy


class Airplane(FlyingObject, Enemy):
    """敌机"""

    def __init__(self, screen, image, life):

        x = random.randint(0, screen.get_rect()[2] - 50)
        y = -40
        super(Airplane, self).__init__(screen, x, y, image)
        self.index = life #敌机等级
        self.air_life = 0  # 初始化敌机血量
        if self.index == 1:
            self.air_life=1000
        if self.index == 2:
            self.air_life=2000
        if self.index == 3:
            self.air_life=5000
        if self.index == 4:
            self.air_life=30000
    def set_air_life(self,li):
        """返回敌机血量"""
        self.air_life -= li
    def get_air_life(self):
        """返回敌机血量"""
        return self.air_life

    def getScore(self):
        """获得的分数"""

        if self.index == 1:
            return 100
        if self.index == 2:
            return 200
        if self.index == 3:
            return 1000
        if self.index == 4:
            return 100000

    def outOfBounds(self):
        """是否越界"""
        if self.y < 1000:
            return True
        else:
            return False

    def step(self):
        """移动"""
        if self.index == 1:
            self.y += 3  # 移动步数
        if self.index == 2:
            self.y += 2  # 移动步数

        if self.index == 3:
            self.y += 0.5  # 移动步数
        if self.index == 4:
            self.y += 0.1  # 移动步数
