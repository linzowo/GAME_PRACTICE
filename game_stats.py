#_*_ coding: utf_8 _*_
import json

class GameStats(object):
    """管理游戏分数的类"""
    def __init__(self,ai_settings):
        """计分项属性"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        #self.height_score = 0
        self.load_height_score()
    def reset_stats(self):
        """初始化游戏期间可能变化的数据"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1 

    def load_height_score(self):
        with open("game_date.json",'r+') as game_date:
            self.height_score = json.load(game_date)
