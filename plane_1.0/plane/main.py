import pygame
import time
import sys
import random
import os
from setting import Settings
from bee import Bee
from hero import Hero
from enemy import Enemy
from award import Award
from airplane import Airplane

START = 0
RUNNING = 1
PAUSE = 2
GAMEOVER = 3
state = START
sets = Settings()
screen = pygame.display.set_mode(
    (sets.bgImageWidth, sets.bgImageHeight), 0, 32)  # 创建窗口
hero = Hero(screen, sets.heroImages)
flyings = []
bullets = []
score = 0
global FIRE_HERO
FIRE_HERO = 400
fclock = pygame.time.Clock()
fps = 144  # 帧数
pygame.mixer.init()
musicList = [
    pygame.mixer.Sound('music/bullet1.ogg')
]

history = 0


# 历史最高分
class History:
    # 读取历史最高分函数
    def ReadHistory(path='score.txt'):
        global history
        if os.path.exists(path):
            with open(path, 'r') as f_r:
                history = f_r.read()
        else:
            with open(path, 'w') as f_w:
                f_w.write('0')

    # 更新历史最高分函数
    def UpdateHistory(score, path='score.txt'):
        if os.path.exists(path):
            with open(path, 'r') as file_r:
                if int(file_r.read()) < score:
                    with open(path, 'w') as file_w:
                        file_w.write(str(score))


def hero_blitme():
    """画英雄机"""
    global hero
    hero.blitme()


def bullets_blitme():
    """画子弹"""
    for b in bullets:
        b.blitme()


def flyings_blitme():
    """画飞行物"""
    global sets
    for fly in flyings:
        fly.blitme()


def score_blitme():
    """画分数和生命值"""
    pygame.font.init()
    fontObj = pygame.font.Font("SIMYOU.TTF", 20)  # 创建font对象

    textSurfaceObj_life = fontObj.render(u'生命值：%d\n' % hero.getLife(), False,
                                         (135, 100, 184))
    textSurfaceObj_grade = fontObj.render(u'分数：%d\n' % score, False,
                                          (135, 100, 184))
    textRectObj_life = textSurfaceObj_life.get_rect()
    textRectObj_life.center = (60, 10)
    screen.blit(textSurfaceObj_life, textRectObj_life)

    textRectObj_grade = textSurfaceObj_grade.get_rect()
    textRectObj_grade.center = (410, 10)
    screen.blit(textSurfaceObj_grade, textRectObj_grade)


def state_blitme():
    """画状态"""
    global sets
    global state
    if state == START:
        screen.blit(sets.start, (0, 0))
        global score
        score = 0
    elif state == PAUSE:
        screen.blit(sets.pause, (0, 0))
    elif state == GAMEOVER:
        History.ReadHistory()
        screen.blit(sets.gameover, (0, 0))
        fontObj_over = pygame.font.Font("SIMYOU.TTF", 50)  # 创建font对象

        textSurfaceObj_over = fontObj_over.render(u'最高分数：%d\n' % int(history), False,
                                                  (51, 204, 250, 255))
        textRectObj_over = textSurfaceObj_over.get_rect()
        textRectObj_over.center = (400, 400)
        screen.blit(textSurfaceObj_over, textRectObj_over)

        fontObj_over2 = pygame.font.Font("SIMYOU.TTF", 50)  # 创建font对象

        textSurfaceObj_over2 = fontObj_over2.render(u'当前分数：%d\n' % score, False,
                                                    (51, 204, 250, 255))
        textRectObj_over2 = textSurfaceObj_over2.get_rect()
        textRectObj_over2.center = (400, 600)
        screen.blit(textSurfaceObj_over2, textRectObj_over2)


def blitmes():
    """画图"""
    hero_blitme()
    flyings_blitme()
    bullets_blitme()
    score_blitme()
    state_blitme()


def nextOne_air():
    """生成敌人"""
    type = random.randint(0, 100)
    if type < 50 and score < 3000:
        return Airplane(screen, sets.airImage[0], 1)
    elif type < 30 and type > 10:
        return Airplane(screen, sets.airImage[1], 2)
    elif type < 40 and type > 10:
        return Airplane(screen, sets.airImage[2], 3)
    elif type < 10 and score > 20000:
        return Airplane(screen, sets.airImage[3], 4)


def nextOne_goods():
    """生成奖励"""
    type = random.randint(0, 100)
    if type < 2:
        return Bee(screen, sets.beeImage[0], 1)
    elif type >= 2 and type < 5:
        return Bee(screen, sets.beeImage[1], 2)
    elif type >= 5 and type < 6:
        return Bee(screen, sets.beeImage[2], 0)


flyEnteredIndex = 0


def enterAction():
    """生成敌人"""

    global flyEnteredIndex
    flyEnteredIndex += 1
    if flyEnteredIndex % 20 == 0:
        flyingobj = nextOne_air()
        flyings.append(flyingobj)
    if flyEnteredIndex % 40 == 0:
        flyingobj = nextOne_goods()
        flyings.append(flyingobj)


shootIndex = 0


def shootAction():
    """子弹入场，将子弹加到bullets"""
    global shootIndex
    shootIndex += 5
    # print(hero.shoot_speed())
    speed = hero.shoot_speed(hero.getFire_MOD())
    if shootIndex % speed == 0:
        if shootIndex > 100000:
            shootIndex = 0
        if hero.getFire_MOD() == 1:
            heroBullet = hero.shoot(sets.heroBullet[0])
            musicList[0].play()
        if hero.getFire_MOD() == 2:
            heroBullet = hero.shoot(sets.heroBullet[1])
            musicList[0].play()
        for bb in heroBullet:
            bullets.append(bb)


def stepAction_flyings():
    """飞行物走一步"""
    hero.step()
    for flyobj in flyings:
        if isinstance(flyobj, Airplane):
            flyobj.step()
        if isinstance(flyobj, Bee):
            flyobj.step()


def stepAction_bullets():
    """子弹走一步"""
    global bullets
    for b in bullets:
        b.step()


def outOfBoundAction():
    """删除越界的敌人和飞行物"""
    global flyings
    flyingLives = []
    index = 0
    for f in flyings:
        if isinstance(f, Airplane):
            if f.outOfBounds() == True:
                flyingLives.insert(index, f)
                index += 1
        if isinstance(f, Bee):
            if f.outOfBounds() == True:
                flyingLives.insert(index, f)
                index += 1
    flyings = flyingLives
    index = 0
    global bullets
    bulletsLive = []
    for b in bullets:
        if b.outOfBounds() == True:
            bulletsLive.insert(index, b)
            index += 1
    bullets = bulletsLive


j = 0


def bangAction():
    """子弹与敌人碰撞"""

    for b in bullets:
        bang(b)


def bang(b):
    """子弹与敌人碰撞检测"""

    for x in range(0, len(flyings)):
        one = flyings[x]
        if isinstance(one, Enemy):
            if flyings[x].shootBy(b):
                f = flyings[x]
                if b in bullets:
                    bullets.remove(b)
                if isinstance(f, Airplane):

                    print(f.get_air_life())
                    f.set_air_life(FIRE_HERO)

                    if (f.get_air_life() <= 0):
                        one = flyings[x]
                        if isinstance(one, Enemy):
                            f = flyings[x]
                            if isinstance(f, Airplane):
                                if f.get_air_life() <= 0:
                                    global score
                                    score += one.getScore()  # 获得分数
                                    flyings.remove(one)  # 删除
                                    break


# def bang(b):
#     """子弹与敌人碰撞检测"""
#     index = -1
#     for x in range(0, len(flyings)):
#         one = flyings[x]
#         if isinstance(one, Enemy):
#             f = flyings[x]
#             if f.shootBy(b):
#                 index = x
#                 break
#     if index != -1:
#         one = flyings[index]
#         if isinstance(one, Enemy):
#             global score
#             score += one.getScore()  # 获得分数
#             flyings.remove(one)  # 删除
#         bullets.remove(b)


def checkGameOverAction():
    if isGameOver():
        global state
        global score
        History.UpdateHistory(score)
        state = GAMEOVER
        hero.reLife()
        pygame.font.init()


def isGameOver():
    for f in flyings:
        # 与奖励碰撞

        if hero.hit(f) and isinstance(f, Award):
            type = f.getType()
            # print(type)
            # 获得不同类型的子弹和生命
            if type == Award.FIRE_RED:
                hero.setFire_MOD(1)
                # print("red")
            if type == Award.FIRE_PURPLE:
                hero.setFire_MOD(2)
                # print("purple")
            if type == Award.LIFE:
                hero.addLife()
            flyings.remove(f)
        # 与敌机碰撞
        if hero.hit(f) and isinstance(f, Enemy):
            hero.sublife()
            hero.clearFire()
            flyings.remove(f)

    return hero.getLife() <= 0


def action():
    x, y = pygame.mouse.get_pos()

    blitmes()  # 打印飞行物
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = pygame.mouse.get_pressed()[0]  # 左键单击事件
            midflag = pygame.mouse.get_pressed()[1]
            rflag = pygame.mouse.get_pressed()[2]  # 右键单击事件
            global state
            if midflag == True:

                for fly in flyings:
                    if isinstance(fly,Airplane):
                        global score
                        score += fly.getScore()  # 获得分数
                        flyings.remove(fly)  # 删除
                for fly in flyings:
                    if isinstance(fly,Airplane):
                        score += fly.getScore()  # 获得分数
                        flyings.remove(fly)  # 删除
            if flag == True and (state == START or state == PAUSE):
                state = RUNNING
            if flag == True and state == GAMEOVER:
                state = START
            if rflag == True:
                state = PAUSE

    if state == RUNNING:
        hero.move(x, y)
        enterAction()
        shootAction()
        outOfBoundAction()
        stepAction_bullets()
        stepAction_flyings()
        bangAction()
        checkGameOverAction()


def main():
    # 1. 创建窗口

    pygame.display.set_caption("飞机大战")
    while True:
        screen.blit(sets.bgImage, (0, 0))  # 加载屏幕
        action()
        pygame.display.update()  # 重新绘制屏幕
        fclock.tick(fps)


if __name__ == '__main__':
    pygame.mixer.music.load("music/Back.ogg")
    pygame.mixer.music.play(-1)
    main()
