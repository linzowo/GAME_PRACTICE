#_*_ coding: utf_8 _*_

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings=Settings()
    ai_settings.bg_color = (135,206,250)
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一个按钮
    play_button = Button(ai_settings,screen,"play")
    stats = GameStats(ai_settings)
    
    #创建一艘飞船
    ship = Ship(screen,ai_settings)
    bullets = Group()

    #创建外星人
    aliens = Group()
    gf.creat_fleet(ai_settings,screen,aliens,ship)
    #alien = Alien(ai_settings,screen)


    #游戏主循环开始
    while True:
        gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens)

        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens,bullets,ai_settings,screen,ship)
            gf.update_aliens(ai_settings,aliens,ship,screen,stats,bullets)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets,stats,play_button)



run_game()

