from flyingObject import FlyingObject
from bullet import Bullet
import random


class Hero(FlyingObject):
    """英雄机"""
    index = 2  # 标志位

    def __init__(self, screen, images):
        # self.screen = screen
        self.images = images  # 英雄级图片数组,为Surface实例
        # image = pygame.image.load(images[0])
        image = images[0]
        x = screen.get_rect().centerx
        y = screen.get_rect().bottom
        super(Hero, self).__init__(screen, x, y, image)
        self.life = 3  # 生命值为3
        self.doubleFire = 100  # 初始火力值为0
        self.RED = 1
        self.PURPLE = 2
        self.Fire_MOD = self.RED
        self.Fire_speed_RED = 40
        self.Fire_speed_PURPLE = 40
        self.mod = 5
        self.difficulty = 0
    def addDifficulty(self):
        self.difficulty+=1
    def shoot_speed(self,x):
        if x==self.RED:
            return self.Fire_speed_RED
        else:
            return self.Fire_speed_PURPLE

    def getFire_MOD(self):
        """返回武器类型,RED为1 PURPLE为2"""
        return self.Fire_MOD

    def setFire_MOD(self, x):
        """设置武器类型"""

        if x == self.RED:
            if self.getFire_MOD() == x:
                self.addFire()
                if self.shoot_speed(x) > 30:
                    self.Fire_speed_RED -= 10

            else:
                self.clearFire()
                self.Fire_speed_PURPLE = 20
                self.Fire_MOD = self.RED
        if x == self.PURPLE:
            if self.getFire_MOD() == x:
                self.addFire()
                if self.shoot_speed(x) > 20:
                    self.Fire_speed_PURPLE -= 10

            else:
                self.clearFire()
                self.Fire_speed_RED = 20
                self.Fire_MOD = self.PURPLE

    def getFire(self):
        """获取火力值"""
        return self.doubleFire

    def setFire(self):
        """设置火力值"""
        self.doubleFire = 400

    def addFire(self):
        """增加火力值"""

        self.doubleFire += 100

    def clearFire(self):
        """清空火力值"""
        self.doubleFire = 100

    def addLife(self):
        """增命"""
        self.life += 1

    def sublife(self):
        """减命"""
        self.life -= 1

    def getLife(self):
        """获取生命值"""
        return self.life

    def reLife(self):
        """重置值"""
        self.life = 3
        self.clearFire()

    def outOfBounds(self):
        return False

    def step(self):
        """动态显示飞机"""
        if (len(self.images) > 0):
            # fclock = pygame.time.Clock()
            # fps = 10  # 帧数
            # fclock.tick(fps)

            Hero.index += 0.3
            Hero.index %= len(self.images)

            # self.image = pygame.image.load(self.images[int(Hero.index)])  # 切换图片
            self.image = self.images[int(Hero.index)]  # 切换图片

    def move(self, x, y):
        self.x = x - self.width / 2
        self.y = y - self.height / 2

    def shoot(self, image):
        """英雄机射击"""
        xStep = int(self.width / 4 - 5)
        yStep = 20
        if self.mod > 0:
            self.mod -= 1
        else:
            self.mod = 5

        if self.getFire_MOD() == 1:
            #print(self.getFire())
            if self.doubleFire >= 400:
                heroBullet = [Bullet(self.screen, image, (self.x - (self.mod - 1) * xStep), self.y - yStep),
                              Bullet(self.screen, image, (self.x + 2 * xStep), self.y - yStep),
                              Bullet(self.screen, image, (self.x + (self.mod + 3) * xStep), self.y - yStep)]
                return heroBullet
            elif self.doubleFire >= 200:
                heroBullet = [Bullet(self.screen, image, (self.x - (5-self.mod - 1) * xStep), self.y - yStep),
                              Bullet(self.screen, image, (self.x + (5-self.mod + 3) * xStep), self.y - yStep)]
                return heroBullet
            else:
                heroBullet = [Bullet(self.screen, image, self.x + 2 * xStep, self.y - yStep)]
                return heroBullet

        if self.getFire_MOD() == 2:
            if self.doubleFire >= 400:
                heroBullet = [Bullet(self.screen, image, self.x + 1 * xStep, self.y - yStep),
                              Bullet(self.screen, image, self.x + 2 * xStep, self.y - yStep),
                              Bullet(self.screen, image, self.x + 3 * xStep, self.y - yStep)]
                return heroBullet
            elif self.doubleFire >=200:
                heroBullet = [Bullet(self.screen, image, self.x + 1 * xStep, self.y - yStep),
                              Bullet(self.screen, image, self.x + 3 * xStep, self.y - yStep)]
                return heroBullet
            else:
                heroBullet = [Bullet(self.screen, image, self.x + 2 * xStep, self.y - yStep)]
                return heroBullet

    def hit(self, other):
        """英雄机和其他飞机"""
        x1 = other.x - self.width / 2
        x2 = other.x + self.width / 2 + other.width
        y1 = other.y - self.height / 2
        y2 = other.y + self.height / 2 + other.height
        x = self.x + self.width / 2
        y = self.y + self.height
        return x > x1 and x < x2 and y > y1 and y < y2
