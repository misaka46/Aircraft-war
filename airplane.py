import random
from flyobject import Flyobject


class Airplane(Flyobject):
    def __init__(self, screen, image):
        x = random.randint(0, screen.get_rect()[2] - 50)
        y = 40
        super(Airplane, self).__init__(screen, x, y, image)

    # def outOfBound(self, screen):
    #     """是否越界"""
    #     return self.y < screen.get_rect()[3]
    def outOfBounds(self):
        """是否越界"""
        return self.y < 715

    def step(self):
        self.y += 3
        

    # 敌机血量
    # def airlife(self):
    #
