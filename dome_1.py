#test
import pygame

pygame.init()
screen = pygame.display.set_mode((480, 700))


bg = pygame.image.load('./images/background.png')
im = pygame.image.load('./images/me1.png')
enemy1 = pygame.image.load('./images/enemy1.png')
clock = pygame.time.Clock()
hero = pygame.Rect(200, 500, 102, 126)

enemy_1 = pygame.Rect(200, 100, 57, 43)


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('游戏退出...')
            pygame.quit()
            exit()
    hero.y -= 2
    enemy_1.y += 1
    screen.blit(bg, (0, 0))

    screen.blit(im, hero)
    screen.blit(enemy1, enemy_1)
    pygame.display.update()
pygame.quit()