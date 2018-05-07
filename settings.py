#_*_ coding: utf_8 _*_
class Settings(object):
    """存储《外星人入侵》所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #子弹属性
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 10
        #子弹颜色深灰色
        self.bullet_color = 60,60,60
        #未消失的子弹数量
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #飞船的设置
        self.ship_limit = 3
        self.ship_speed_factor = 1.1
        self.speedup_scale = 1.5 #按照什么样的节奏加快游戏

        self.initialize_dynamic_setting() #初始化动态数据

    def initialize_dynamic_setting(self):
        """重置动态设置"""
        self.bullet_speed_factor = 1
        self.ship_speed_factor = 1.1
        self.alien_speed_factor = 1
        self.alien_point = 50  #外星人的分值
        
        self.fleet_direction = 1 #外星人向右边移动

    def increase_speed(self):
        """提高游戏速度"""
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.speedup_scale)