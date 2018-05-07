#_*_ coding: utf_8 _*_
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """关于飞船的类"""
    
    def __init__(self,screen,ai_settings):
        """初始化飞船位置"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/airship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放到屏幕的底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #保存飞船位置的浮点数
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        #飞船移动标志
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False


    def blitme(self):
        """在制定位置创建飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据移动标志来移动飞船"""
        #改变位置参数
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        elif self.move_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        elif self.move_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.ship_speed_factor
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor

        #更新位置
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def center_ship(self):
        """将飞船放置在屏幕中央"""
        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom
