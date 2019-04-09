import pygame, sys, random

# from setting import Settings

backgroundImage = pygame.image.load('images/background.png')  # 背景图# Rect(left, top, width, height) -> Rect
backgroundWidth = backgroundImage.get_rect()[2]  # 背景的高
backgroundHeight = backgroundImage.get_rect()[3]  # 背景的宽
heroImage = ["images/hero.png"]  # 英雄机图片
heroBullet = pygame.image.load('images/bullet.png')  # 英雄机的子弹

#sets = Settings()
screen = pygame.display.set_mode((backgroundWidth, backgroundHeight), 0, 32)  # 创建窗口
fclock = pygame.time.Clock()
fps = 60  # 帧数


def main():
    # 创建窗口
    pygame.display.set_caption("飞机大战")
    while True:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
                     sys.exit()
        screen.blit(backgroundImage, (0, 0))  # 加载屏幕
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
