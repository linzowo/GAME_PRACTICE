#_*_ coding:utf_8 _*_

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹的类"""
    def __init__(self,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0,0,10,5)
        self.color = (0,0,0)

        self.rect.right = ship.rect.right
        self.rect.centery = ship.rect.centery

        self.x = float(self.rect.x)
        self.speed = 1.5

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

    def update(self):
        self.x += self.speed
        self.rect.x =self.x