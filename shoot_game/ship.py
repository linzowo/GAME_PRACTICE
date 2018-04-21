#_*_ coding:utf_8 _*_

import pygame

class Ship(object):
    """管理飞船的类"""
    def __init__(self,screen,al_settings):
        self.al_settings = al_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        #jiangfeichuan放置在屏幕中间
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        """移动飞船"""
        if self.al_settings.ship_move_up and (self.rect.top >= 0):
            self.rect.y -= 1
        if self.al_settings.ship_move_down and (self.rect.bottom <= self.screen_rect.bottom):
            self.rect.y += 1
