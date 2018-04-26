#_*_ coding:utf_8 _*_

import pygame
from pygame.sprite import Group

import game_function as gf
from ship import Ship
from settings import Settings
from diamonds import Diamonds
from game_stats import Stats
from play_button import Button

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,600))
    pygame.display.set_caption("Shoot Game")
    al_settings = Settings()
    stats = Stats()

    diamonds = Diamonds(screen,al_settings)
    ship = Ship(screen,al_settings)
    bullets = Group()
    button = Button(screen,"play")

    while True:
        gf.check_events(ship,al_settings,bullets,screen,button,stats)
        if stats.game_active:
            ship.update()
            gf.update_bullet(diamonds,bullets,stats)
            diamonds.update()
        gf.update_screen(screen,ship,diamonds,al_settings,bullets,stats,button)

run_game()
