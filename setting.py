import pygame

class Settings(object):
    """设置常用的属性"""

    def __int__(self):
        self.backgroundImage = pygame.image.load('images/background.png')  # 背景图# Rect(left, top, width, height) -> Rect
        self.backgroundWidth = self.backgroundImage.get_rect()[2]  # 背景的高
        self.backgroundHeight = self.backgroundImage.get_rect()[3]  # 背景的宽
        self.heroImage = ["images/hero.png","images/hero1.png","images/hero2.png"]  # 英雄机图片
        self.heroBullet = pygame.image.load('images/bullet.png')  # 英雄机的子弹
    # def backgroundWidth(self):
    #     return self.backgroundImage.get_rect()[2]
    # def backgroundHeight(self):
    #     return self.backgroundImage.get_rect()[3]
# backgroundImage = pygame.image.load('images/background.png')  # 背景图
# # Rect(left, top, width, height) -> Rect
# backgroundWith = backgroundImage.get_rect()[2]  # 背景的高
# backgroundHeight = backgroundImage.get_rect()[3]  # 背景的宽
# heroImage = ["images/hero.png"]  # 英雄机图片
# heroBullet = pygame.image.load('images/bullet.png')  # 英雄机的子弹
