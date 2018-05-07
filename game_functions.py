#_*_ coding: utf_8 _*_
import sys
import pygame
import json

from bullet import Bullet
from alien import Alien
from time import sleep

#响应用户按键的函数
def check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #如果用户点了退出
            sys_out(stats)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets,stats,aliens,sb)

        elif event.type == pygame.KEYUP:
            check_keyup_events(ship,event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,ship,stats,play_button,mouse_x,mouse_y,
                      aliens,bullets,sb)

def check_keydown_events(event,ai_settings,screen,ship,bullets,stats,aliens,sb):
    """响应KEYDOWN事件"""
    if event.key == pygame.K_q:
        sys_out(stats)
    if event.key == pygame.K_RIGHT:
        #如果按键为right则向右移动一格
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    if event.key == pygame.K_UP:
        ship.move_up = True
    if event.key == pygame.K_DOWN:
        ship.move_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    if (event.key == pygame.K_p) and not stats.game_active:
        start_game(ai_settings,screen,stats,aliens,bullets,ship,sb)
        
def check_keyup_events(ship,event):
     """响应KEYUP事件"""
     if event.type == pygame.KEYUP:
        ship.move_right = False
        ship.move_left = False
        ship.move_up = False
        ship.move_down = False

def check_play_button(ai_settings,screen,ship,stats,play_button,mouse_x,mouse_y,
                      aliens,bullets,sb):
    """在玩家点击play按键时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings,screen,stats,aliens,bullets,ship,sb)

def start_game(ai_settings,screen,stats,aliens,bullets,ship,sb):
    """开始游戏时重置游戏元素"""
    #初始化玩家生命值
    stats.reset_stats()
    #将游戏变更为活动状态
    stats.game_active = True
    #消除屏幕上的子弹和外星人
    aliens.empty()
    bullets.empty()

    #创建一个新的舰队并让飞船居中
    creat_fleet(ai_settings,screen,aliens,ship)
    ship.center_ship()
    ai_settings.initialize_dynamic_setting()

    #重置计分板
    sb.prep_score()
    sb.prep_height_score()
    sb.prep_level()
    sb.prep_ship()

    #隐藏鼠标
    pygame.mouse.set_visible(False)


#关于子弹的函数

def update_bullets(aliens,bullets,ai_settings,screen,ship,stats,sb):
    """管理子弹数量的函数"""
    bullets.update()
    #删除已经飞出屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,aliens,ship,bullets,stats,sb)

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果子弹数还没有达到上限就创建一颗"""
    # 创建一颗子弹并把它加入到编组中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullets)

def check_bullet_alien_collisions(ai_settings,screen,aliens,ship,bullets,stats,sb):
    """检查子弹和外星人是否碰撞，如果碰撞就删除子弹和外星人"""
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for alien in collisions.values(): 
            stats.score += ai_settings.alien_point * len(alien)
            sb.prep_score()
            check_height_score(stats,sb)

    if len(aliens) == 0:
        #删除现有的子弹并创建一群外星人
        bullets.empty()
        creat_fleet(ai_settings,screen,aliens,ship)
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()

#关于外星人的函数
def get_number_alien_x(ai_settings,alien_width):
    """计算每行能够容纳几个外星人"""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_settings,alien_height,ship_height):
    """计算能有几行外星人"""
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def creat_alien(ai_settings,screen,aliens,number_alien,number_row):
    """创建一个外星人并将它加入编组"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * number_alien 
    alien.rect.x = alien.x
    alien.y = alien_height + 2 * alien_height * number_row
    alien.rect.y = alien.y
    aliens.add(alien)

def update_aliens(ai_settings,aliens,ship,screen,stats,bullets,sb):
    """更新外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #检查外星人和飞船碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ship,aliens,bullets,screen,ai_settings,stats,sb)
    check_alien_bottom(ship,aliens,bullets,screen,ai_settings,stats,sb)

def check_alien_bottom(ship,aliens,bullets,screen,ai_settings,stats,sb):
    """如果外星人到达屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ship,aliens,bullets,screen,ai_settings,stats,sb)
            break

def creat_fleet(ai_settings,screen,aliens,ship):
    """创建一个外星人编队"""
    alien = Alien(ai_settings,screen)
    number_alien_x = get_number_alien_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,alien.rect.height,ship.rect.height)
    #生成一个编组的外星人
    for row_number in range(number_rows):
        for number_alien in range(number_alien_x):
            creat_alien(ai_settings,screen,aliens,number_alien,row_number)

def change_fleet_direction(ai_settings,aliens):
    """让外星人下降并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
        
def check_fleet_edges(ai_settings,aliens):
    """判断飞船是否到达屏幕边界"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def ship_hit(ship,aliens,bullets,screen,ai_settings,stats,sb):
    """响应外星人撞击飞船"""
    if stats.ships_left > 0:
        #飞船数量减一
        stats.ships_left -= 1

        #清空子弹和外星人
        aliens.empty()
        bullets.empty()

        #创建一批新的外星人并将飞船放置到屏幕中央
        creat_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()
        sb.prep_ship()

        #让游戏暂停一会儿让玩家知道发生了什么
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_height_score(stats,sb):
    """如果产生了最高分，将最高分显示在屏幕上"""
    if stats.score > stats.height_score:
        stats.height_score = stats.score
        sb.prep_height_score()

def save_date(stats):
    """将游戏数据保存为文本"""
    with open("game_date.json",'r+') as game_date:
        json.dump(stats.height_score,game_date)

def sys_out(stats):
    """关闭程序"""
    save_date(stats)
    sys.exit()
    

def update_screen(ai_settings,screen,ship,aliens,bullets,stats,play_button,sb):
    """更新屏幕上的图像，并显示新屏幕"""   
    #更改屏幕颜色
    screen.fill(ai_settings.bg_color)
    #创建飞船
    ship.blitme()
    #ship2.blit_new()
    aliens.draw(screen)
    #创建一系列子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    sb.blitme()
    #如果游戏处于非活动状态就创建一个play按钮
    if not stats.game_active:
        play_button.draw_button()
    #显示最新的屏幕
    pygame.display.flip()