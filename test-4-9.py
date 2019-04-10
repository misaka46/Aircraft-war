import pygame, sys, random
from hero import Hero
from airplane import Airplane
from setting import Settings
from flyobject import Flyobject

# from setting import Settings
# 游戏状态
START = 0
RUNNING = 1
PAUSE = 2
GAMEOVER = 3

start = RUNNING
# 游戏素材
backgroundImage = pygame.image.load('images/background.png')  # 背景图# Rect(left, top, width, height) -> Rect
heroImage = ["images/hero.gif", "images/hero1.png", "images/hero2.png"]  # 英雄机图片
heroBullet = pygame.image.load('images/bullet.png')  # 英雄机的子弹
airimages = pygame.image.load('images/enemy1.png')

# 游戏窗口
backgroundWidth = backgroundImage.get_rect()[2]  # 背景的高
backgroundHeight = backgroundImage.get_rect()[3]  # 背景的宽
screen = pygame.display.set_mode((backgroundWidth, backgroundHeight), 0, 32)  # 创建窗口
fclock = pygame.time.Clock()
fps = 60  # 帧数
hero = Hero(screen, heroImage)
flying = []
bullets = []
# sets = Settings()


sets = Settings()


def hero_blitme():
    """画英雄机"""
    global hero
    hero.blitme()


# ?????
def flyings_blitme():
    for fly in flying:
        fly.blitme()

def state_blitme():
    """画状态"""
    global sets
    global start
    if start==START:
        screen.blit(sets.start, (0,0))
    elif start==PAUSE:
        screen.blit(sets.pause,(0,0))
    elif start== GAMEOVER:
        screen.blit(sets.gameover,(0,0))

def blitme():
    """画图"""
    flyings_blitme()
    hero_blitme()
    state_blitme()

def nextone():
    """生成敌人"""
    type = random.randint(0, 20)
    if (type > 5):
        return Airplane(screen, airimages)


flyEnteredIndex = 0



def enterAction():
    """生成敌人"""
    global flyEnteredIndex
    flyEnteredIndex+=1
    if flyEnteredIndex%40==0:
        flyingobj=nextone()
        flying.append(flyingobj)

def stepAction():
    """敌人移动"""
    hero.step()
    global flying
    for flyobj in flying:
        flyobj.step()
    global  bullets
    for b in bullets:
        b.step()
    # hero.step()
    # for fobj in flying:
    #     fobj.step()
    # global bullets
    # for b in bullets:
    #     b.step()


def outOfBoundAction():
    """删除越界的敌人和飞行物"""
    global flying
    flyingLives = []
    index = 0
    for f in flying:
        if f.outOfBounds() == True:
            flyingLives.insert(index, f)
            index += 1
        flying = flyingLives
    index = 0
    global bullets
    bulletsLive = []
    for b in bullets:
        if b.outOfBounds() == True:
            bulletsLive.insert(index, b)
            index += 1
    bullets = bulletsLive


def action():
    x, y = pygame.mouse.get_pos()
    blitme()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = pygame.mouse.get_pressed()[0]  # 左键单击事件
            rflag = pygame.mouse.get_pressed()[2]  # 右键单击事件
            global start
            if flag == True and (start == START or start == PAUSE):
                start = RUNNING
            if flag == True and start == GAMEOVER:
                start = START
            if rflag == True:
                start = PAUSE

    if start == RUNNING:
        hero.move(x, y)
        enterAction()
        # shootAction()
        stepAction()


# outOfBoundAction()
# bangAction()
# checkGameOverAction()


def main():
    # 创建窗口
    pygame.display.set_caption("飞机大战")
    while True:
        screen.blit(backgroundImage, (0, 0))  # 加载屏幕
        action()
        pygame.display.update()  # 重新绘制屏幕
        fclock.tick(fps)


if __name__ == '__main__':
    main()

# import pygame,sys
#
# pygame.init()
# size = width,height = 600,400
# speed = [2,2]
# BLACK = 0, 0, 0
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("test")
# ball = pygame.image.load('me1.png')
# ballrect = ball.get_rect()
# fclock = pygame.time.Clock()
# fps=300
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
#             elif event.key == pygame.K_RIGHT:
#                 speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
#             elif event.key == pygame.K_UP:
#                 speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
#             elif event.key == pygame.K_DOWN:
#                 speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
#     ballrect = ballrect.move(speed[0],speed[1])
#     if ballrect.left < 0 or ballrect.right>width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#        speed[1] = -speed[1]
#
#     screen.fill(BLACK)
#     screen.blit(ball,ballrect)
#     pygame.display.update()
#     fclock.tick(fps)
