import pygame
from plane_sprite import *


class PlaneGame(object):
    def __init__(self):
        print("初始化游戏")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprite()

    def start_game(self):
        print("开始游戏")
        while True:
            self.clock.tick(GAME_PER)
            self.__event_listener()
            self.__check_boom()
            self.__update_sprite()
            pygame.display.update()
            pass

    def __create_sprite(self):
        bg1 = BackGroud("./image/1.jpg")
        bg2 = BackGroud("./image/1.jpg")
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)

    def __event_listener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.___game_over()

    def __check_boom(self):
        pass

    def __update_sprite(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def ___game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
