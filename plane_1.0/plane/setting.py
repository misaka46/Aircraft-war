import pygame


class Settings(object):
    """设置常用的属性"""

    def __init__(self):
        self.bgImage = pygame.transform.scale(pygame.image.load('img/background.jpg'),(800,1000))  # 背景图

        self.bgImageWidth = self.bgImage.get_rect()[2]  # 背景图宽
        self.bgImageHeight = self.bgImage.get_rect()[3]  # 背景图高
        self.start = pygame.transform.scale(pygame.image.load("img/start.png"),(800,1000))
        self.pause = pygame.image.load("img/btn_finish.png")
        self.gameover = pygame.transform.scale(pygame.image.load("img/back3.png"),(800,1000))
        # self.heroImages = ["img/hero.gif",
        #                    "img/hero1.png", "img/hero2.png"]  # 英雄机图片
        self.heroImages = [
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship1.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship2.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship3.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship4.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship5.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship6.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship7.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship8.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship9.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship8.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship7.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship6.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship5.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship4.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship3.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship2.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("img/shipBlue/ship1.png"), (100, 100))
        ]
        self.airImage = [
            pygame.transform.scale(pygame.image.load("img/enemy/enemy_0.png"),(80,80)),
            pygame.transform.scale(pygame.image.load("img/enemy/enemy_1.png"), (80, 80)),
            pygame.transform.scale(pygame.image.load("img/enemy/enemy_2.png"), (80, 80)),
            pygame.transform.scale(pygame.image.load("img/enemy/enemy_3.png"), (200, 200))
        ]  # airplane的图片
        self.beeImage = pygame.image.load("img/bee.png")  # bee的图片
        self.beeImage = [
            pygame.image.load("img/bullet/red_bullet_goods.png"),
            pygame.image.load("img/bullet/purple_bullet_goods.png"),
            pygame.image.load("img/bullet/life_goods.png")
        ]  # bee的图片
        # self.heroBullet=pygame.image.load("img/bullet.png")# 英雄机的子弹
        self.heroBullet = [
            pygame.transform.scale(pygame.image.load("img/bullet/red_bullet.png"), (20, 40)),
            pygame.transform.scale(pygame.image.load("img/bullet/purple_bullet.png"), (20, 40))
        ]  # 英雄机的子弹

