import random
from time import sleep
import pygame
from flyobject import Flyobject


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

    def step(self):
        if len(self.images) > 0:
            # sleep(0.009)
            Hero.index += 1
            Hero.index %= len(self.images)
            if random.randint(0, 10) < 3: #随机飞机动画变化
                self.image = pygame.image.load(self.images[int(Hero.index)])

    def move(self, x, y):
        # self.x -= x
        # self.y -= y
        self.x = x - self.width / 2
        self.y = y - self.height / 2
