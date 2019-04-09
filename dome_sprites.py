import pygame
import random

SCREEN=pygame.Rect(0,0,480,700)  # 屏幕大小常量
CREAT_EVENT=pygame.USEREVENT  # 定时器常量，这个用于向屏幕定时添加敌机
BULLET_EVENT = pygame.USEREVENT+1 # 这也是定时器常量，用于定时发射子弹。


class PlaneSprites(pygame.sprite.Sprite):
    """创建精灵类"""
    def __init__(self, image, speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed



     #  重写update方法
    def update(self):
        self.rect.y += self.speed

class BackGround(PlaneSprites):
    def __init__(self,is_flag=False):
        super().__init__('background.png')
        if is_flag:
            self.rect.y =-self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN.height:  # 判断图片是否滚出屏幕，如果背景图片rect对象的y值大于屏幕的高度
            self.rect.y =-self.rect.height  # 将背景图的y值设置为背景图高度的负值，这张图片就在屏幕上方

# 创建敌机类
class CreatPlane(PlaneSprites):
    def __init__(self):
        super().__init__('enemy1.png')
        self.speed = random.randint(1,4)  # 利用随机数控制敌机飞行速度
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(0, SCREEN.width-self.rect.width)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN.height:
            self.kill()

    def __del__(self):
        print('敌机消失.....')

# 创建战机类
class CreatHero(PlaneSprites):
    def __init__(self):
        super().__init__('me1.png', speed=0)
        self.rect.centerx = SCREEN.centerx
        self.rect.bottom = SCREEN.bottom-120
        self.bullet_gruop = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN.right:
            self.rect.right = SCREEN.right

    # 发射子弹
    def fire(self):
        for i in (0, 1):
            bullt = CreatBullet()
            bullt.rect.bottom = self.rect.y-i*20
            bullt.rect.centerx = self.rect.centerx
            self.bullet_gruop.add(bullt)


# 创建子弹精灵类
class CreatBullet(PlaneSprites):
    def __init__(self):
        super().__init__('bullet.png', speed=-2)

    def update(self):
        super().update()
        if self.rect.y < SCREEN.y:
            self.kill()

    def __del__(self):
        print('子弹消失......')