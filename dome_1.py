# #test
# import pygame
#
# pygame.init()
# screen = pygame.display.set_mode((480, 700))
#
#
# bg = pygame.image.load('background.png')
# im = pygame.image.load('me1.png')
# enemy1 = pygame.image.load('enemy1.png')
# clock = pygame.time.Clock()
# hero = pygame.Rect(200, 500, 102, 126)
#
# enemy_1 = pygame.Rect(200, 100, 57, 43)
#
#
# while True:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print('游戏退出...')
#             pygame.quit()
#             exit()
#     hero.y -= 2
#     enemy_1.y += 1
#     screen.blit(bg, (0, 0))
#
#     screen.blit(im, hero)
#     screen.blit(enemy1, enemy_1)
#     pygame.display.update()
# pygame.quit()
#
#
#
import pygame
from dome_sprites import *


class GamePlay(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN.size)
        self.clock = pygame.time.Clock()
        self.__creat_sprite()
        pygame.time.set_timer(CREAT_EVENT, 1000)
        pygame.time.set_timer(BULLET_EVENT, 500)

    def start_game(self):
        while True:
            self.clock.tick(60)
            self.__update()
            pygame.display.update()
            self.__event()
            self.__chenck()

    def __chenck(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_gruop,self.enemy_group,True,True)
        # 敌机碰撞战机
        bullet_list = pygame.sprite.spritecollide(self.hero,self.enemy_group, True)
        if len(bullet_list) != 0:
            self.hero.kill()
            GamePlay.game_over()

    def __creat_sprite(self):
        # hero1=BackGround('./images/background.png')
        # hero2=BackGround('./images/background.png')
        # hero2.rect.y =-hero2.rect.height
        # 创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(is_flag=True)
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建战机精灵和精灵组
        self.hero = CreatHero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.hero.bullet_gp = pygame.sprite.Group()

    #  更新精灵的位置
    def __update(self):
        # 更新背景图片位置
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        # 更新敌机位置
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 更新战机位置
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        #  更新子弹位置
        self.hero.bullet_gruop.update()
        self.hero.bullet_gruop.draw(self.screen)

    # 事件监听
    def __event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 当监听事件为退出事件，则退出游戏
                print('游戏退出....')
                pygame.quit()  # 卸载所有模块
                exit()  # 退出整个系统
            elif event.type == CREAT_EVENT:  # 当监听事件为定时器发生的，则创建一个敌机
                enemy1 = CreatPlane()
                self.enemy_group.add(enemy1)
            elif event.type == BULLET_EVENT:
                self.hero.fire()
        keys_press = pygame.key.get_pressed()
        # 键盘操作战机左右移动
        if keys_press[pygame.K_RIGHT]:  # 按下右键，
            self.hero.speed = 2
        elif keys_press[pygame.K_LEFT]:  # 按下左键
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    @staticmethod
    def game_over():
        pygame.quit()

if __name__ == '__main__':
    game = GamePlay()
    game.start_game()