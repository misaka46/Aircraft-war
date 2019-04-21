import abc


class Flyobject(object):
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = image.get_rect()[2]
        self.height = image.get_rect()[3]
        self.image = image
    @abc.abstractmethod
    def outOfBounds(self):
        """检查是否越界"""
        pass

    # @abc.abstractmethod
    # def step(self):
    #     """飞行物移动一步"""
    #     pass

    def shootBy(self, bullet):
        """检查当前飞行物是否被子弹bullet（x，y）击中"""
        x1 = self.x
        x2 = self.x + self.width
        y1 = self.y
        y2 = self.y + self.height
        x = bullet.x
        y = bullet.y
        return x > x1 and x < x2 and y > y1 and y < y2
    def blitme(self):
        """打印飞行物"""
        self.screen.blit(self.image, (self.x, self.y))

