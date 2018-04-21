#_*_ coding:utf_8 _*_

import pygame

class Diamonds(object):
    """管理靶子的类"""
    def __init__(self,screen,al_settings):
        self.screen = screen
        self.al_settings = al_settings
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0,0,100,50)
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        self.color = (0,0,0)
        self.y = float(self.rect.y)

    def draw_dia(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

    def update(self):
        self.y += self.al_settings.dia_speed
        self.rect.y =self.y
