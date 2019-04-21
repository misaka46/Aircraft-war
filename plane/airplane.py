import random
from plane.flyobject import Flyobject


# class Airplane(Flyobject):
#     def __init__(self, screen, image):
#         x = random.randint(0, screen.get_rect()[2] - 50)
#         y = -40
#         super(Airplane, self).__init__(screen, x, y, image)
#
#     # def outOfBound(self, screen):
#     #     """是否越界"""
#     #     return self.y < screen.get_rect()[3]
#     def outOfBounds(self):
#         """是否越界"""
#         return self.y < 715
#
#     def step(self):
#         self.y += 3
#
#
#     # 敌机血量
#     # def airlife(self):
#     #
class Airplane(Flyobject):
    """普通敌机"""

    def __init__(self, screen, image):

        x = random.randint(0, screen.get_rect()[2] - 50)
        y = -40
        super(Airplane, self).__init__(screen, x, y, image)

    def getScore(self):
        """获得的分数"""
        return 5

    def outOfBounds(self):
        """是否越界"""

        return self.y < 715

    def step(self):
        """移动"""
        self.y += 3  # 移动步数