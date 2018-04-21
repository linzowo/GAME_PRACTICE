#_*_ coding: utf_8 _*_
class Settings(object):
    """存储《外星人入侵》所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #子弹属性
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 5
        #子弹颜色深灰色
        self.bullet_color = 60,60,60
        #未消失的子弹数量
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        self.fleet_direction = 1

        #飞船的设置
        self.ship_limit = 3
        self.ship_speed_factor = 1.5
