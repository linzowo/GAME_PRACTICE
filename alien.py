#_*_ coding: utf_8 _*_

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人管理类"""
    def __init__(self,ai_settings,screen):
       """外星人的基本属性"""
       super(Alien,self).__init__()
       self.ai_settings = ai_settings
       self.screen = screen

       #加载外星人图像
       self.image = pygame.image.load('image/alien.bmp')
       self.rect = self.image.get_rect()

       #把外星人放置在屏幕左上角
       self.rect.x = self.rect.width
       self.rect.y = self.rect.height

       #为了精确的存储外星人的位置
       self.rect.x = float(self.rect.x)

       #外星人编号
       self.number = 0

    def blitme(self):
        """在屏幕上创建外星人"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """让外星人向左右移动"""
        self.x += (self.ai_settings.alien_speed_factor * 
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """判断外星人是否到达屏幕边缘"""
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True


        
