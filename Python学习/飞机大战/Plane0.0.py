import pygame
from plane_sprite import *

pygame.init()
screen = pygame.display.set_mode((500, 1000))
bg = pygame.image.load("/home/xqh/桌面/飞机大战/image/1.jpg")
screen.blit(bg, (0, 0))
hero = pygame.image.load("/home/xqh/桌面/飞机大战/image/3.png")
screen.blit(hero, (225, 750))
pygame.display.update()
clock = pygame.time.Clock()
hero_locate = pygame.Rect(255, 750, 51, 52)
enemy1 = GameSprite("./image/4.png")
enemy_group = pygame.sprite.Group(enemy1)

while True:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            exit()

    screen.blit(bg, (0, 0))
    hero_locate.y -= 1
    screen.blit(hero, hero_locate)
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()


