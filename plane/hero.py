import random
import pygame
from plane.flyobject import Flyobject
from plane.bullet import Bullet


class Hero(Flyobject):
    """英雄机"""
    index = 2

    def __init__(self, screen, images):
        self.images = images  # 英雄图片数组
        image = pygame.image.load(images[1])
        x = screen.get_rect().centerx
        y = screen.get_rect().bottom
        super(Hero, self).__init__(screen, x, y, image)
        self.Fire = 0  # 火力类型
        self.life = 3

    def addLife(self):
        """加命"""
        self.life += 1

    def subLife(self):
        """减命"""
        self.life -= 1

    def getLife(self):
        """获取生命值"""
        return self.life

    def regLife(self):
        """# 还原生命值&还原fire"""
        self.life = 3

    def outOfBounds(self):
        return False

    def step(self):
        if len(self.images) > 0:
            # sleep(0.009)
            Hero.index += 1
            Hero.index %= len(self.images)
            if random.randint(0, 10) < 3:  # 随机飞机动画变化
                self.image = pygame.image.load(self.images[int(Hero.index)])

    def shoot(self, image):
        """英雄机射击"""
        xStep = int(self.width / 4 - 5)
        yStep = 20
        heroBullet = [Bullet(self.screen, image, self.x + 2 * xStep, self.y - yStep)]
        return heroBullet
        # if self.doubleFire >= 100:
        #     heroBullet = [Bullet(self.screen, image, self.x + 1 * xStep, self.y - yStep),
        #                   Bullet(self.screen, image, self.x + 2 * xStep, self.y - yStep),
        #                   Bullet(self.screen, image, self.x + 3 * xStep, self.y - yStep)]
        #     self.doubleFire -= 3
        #     return heroBullet
        # elif self.doubleFire < 100 and self.doubleFire > 0:
        #     heroBullet = [Bullet(self.screen, image, self.x + 1 * xStep, self.y - yStep),
        #                   Bullet(self.screen, image, self.x + 3 * xStep, self.y - yStep)]
        #     self.doubleFire -= 2
        #     return heroBullet
        # else:
        #     heroBullet = [Bullet(self.screen, image, self.x + 2 * xStep, self.y - yStep)]
        #     return heroBullet

    def move(self, x, y):
        # self.x -= x
        # self.y -= y
        self.x = x - self.width / 2
        self.y = y - self.height / 2

    def hit(self, other):
        """英雄机和其他飞机"""
        x1 = other.x - self.width / 2
        x2 = other.x + self.width / 2 + other.width
        y1 = other.y - self.height / 2
        y2 = other.y + self.height / 2 + other.height
        x = self.x + self.width / 2
        y = self.y + self.height
        return x > x1 and x < x2 and y > y1 and y < y2
