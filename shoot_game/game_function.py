#_*_ coding:utf_8 _*_

import pygame
import sys
from time import sleep

from bullet import Bullet


def check_events(ship,al_settings,bullets,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                al_settings.ship_move_up = True
            if event.key == pygame.K_DOWN:
                al_settings.ship_move_down = True
            if event.key == pygame.K_SPACE:
                fire_bullet(bullets,screen,ship)
        if event.type == pygame.KEYUP:
            al_settings.ship_move_up = False
            al_settings.ship_move_down = False

def check_edges(diamonds):
    """检查靶子是否到达边界"""
    if diamonds.rect.bottom >= diamonds.screen_rect.bottom:
        return True
    if diamonds.rect.top <= 0:
        return True

def change_dia_direction(diamonds,al_settings):
    if check_edges(diamonds):
        al_settings.dia_speed *= al_settings.change_direction

def fire_bullet(bullets,screen,ship):
    bullet = Bullet(screen,ship)
    bullets.add(bullet)


def update_bullet(diamonds,bullets,stats):
    """管理子弹的函数"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= bullet.screen_rect.right:
            bullets.remove(bullet)
            stats.dog_life -= 1
    check_colli(diamonds,bullets,stats)


def check_colli(diamonds,bullets,stats):
    """检查子弹是否集中靶子"""
    if stats.dog_life <= 0:
        stats.game_active = False
    if pygame.sprite.spritecollideany(diamonds,bullets):
        hit_dia(bullets)

def hit_dia(bullets):
    """击中靶子后"""
    bullets.empty()  #清空子弹
    sleep(0.5) #暂停

def update_screen(screen,ship,diamonds,al_settings,bullets):
    screen.fill((255,255,255))
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    check_edges(diamonds)
    change_dia_direction(diamonds,al_settings)
    diamonds.draw_dia()
    pygame.display.flip()