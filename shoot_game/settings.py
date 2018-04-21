#_*_ coding:utf_8 _*_

class Settings(object):
    """管理游戏设置"""
    def __init__(self):
        #飞船移动标志
        self.ship_move_up = False
        self.ship_move_down = False

        #靶子变向标记
        self.dia_speed = 1
        self.change_direction = -1