#_*_ coding: utf_8 _*_

import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard(object):
    """管理分数板的类"""
    def __init__(self,screen,stats,ai_settings):
        self.screen = screen
        self.stats = stats
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        self.text_color = (30,30,30)
        self.board_color = (135,206,250)
        self.font = pygame.font.SysFont(None,48)
        self.prep_score()
        self.prep_height_score()
        self.prep_level()
        self.prep_ship()
		
    def prep_score(self):
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.image = self.font.render(score_str,True,self.text_color,self.board_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.right = self.screen_rect.right - 20
        self.image_rect.top = 20
		
    def prep_height_score(self):
        """设置最高分"""
        rounded_score = int(round(self.stats.height_score,-1))
        height_score_str = "{:,}".format(rounded_score)
        self.height_score_image = self.font.render(height_score_str,True,self.text_color,
                                                  self.board_color) #将最高分渲染成图片
        self.height_score_image_rect = self.height_score_image.get_rect()
        self.height_score_image_rect.top = self.screen_rect.top
        self.height_score_image_rect.centerx = self.screen_rect.centerx

    def prep_level(self):
        """显示等级"""
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,
                                            self.board_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.image_rect.right
        self.level_image_rect.top = self.image_rect.bottom + 10

    def prep_ship(self):
        """显示剩余飞船数"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen,self.ai_settings)
            ship.rect.centerx = 10 + ship.rect.width * ship_number
            ship.rect.centery = 10
            self.ships.add(ship)

    def blitme(self):
        self.screen.blit(self.image,self.image_rect)
        self.screen.blit(self.height_score_image,self.height_score_image_rect)
        self.screen.blit(self.level_image,self.level_image_rect)
        self.ships.draw(self.screen)