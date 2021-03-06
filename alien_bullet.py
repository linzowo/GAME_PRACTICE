#_*_ coding: utf_8 _*_

import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    """子弹类"""
    def __init__(self,ai_seting,screen,alien):
        """在飞船所在的位置创建一个子弹"""
        super(AlienBullet,self).__init__()
        self.screen = screen

        #在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,5,10)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        #将子弹的移动坐标y存储为浮点数，以便能对子弹做微调
        self.y = float(self.rect.y)

        self.speed_factor = ai_seting.bullet_speed_factor
        self.color = ai_seting.bullet_color

    def update(self):
        """向下移动子弹"""
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)

