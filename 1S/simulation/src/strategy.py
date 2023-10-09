import random 
from enum import Enum 

from setting import * 

random.seed(RANDOM_SEED)   # 再現性確保のため乱数のseedを固定

# バーの状態に関係なくバーに行く
def strategy_bar(bar_record_list : list[float]) -> bool : 
    return True 

# バーの状態に関係なくバーに行かない
def strategy_house(bar_record_list : list[float]) -> bool : 
    return False

# ランダムに決定、SATISFY_RATIOと同じ確率でバーに行く
def strategy_random(bar_record_list : list[float]) -> bool : 
    return random.random() <= SATISFY_RATIO

# 先週のバーの混雑率がSATISFY_RATIOを下回っていればバーに行く
def strategy_last_week(bar_record_list : list[float]) -> bool : 
    assert len(bar_record_list) > 0
    return bar_record_list[-1] <= SATISFY_RATIO

# 4週間のバーの混雑率がSATISFY_RATIOを下回っていればバーに行く
# 4週間分のデータがないときは、全てのデータを使う
def strategy_average(bar_record_list : list[float]) -> bool : 
    assert len(bar_record_list) > 0 
    average_size = min(4, len(bar_record_list))
    return sum(bar_record_list[-1 * average_size : ]) <= SATISFY_RATIO

# strategy_last_weekの逆の行動を取る天邪鬼
def strategy_contrary(bar_record_list : list[float]) -> bool : 
    assert len(bar_record_list) > 0
    return bar_record_list[-1] > SATISFY_RATIO

# Enumで関数を持つのは無理っぽい... Enum.nameが使えない
class Strategy(Enum) : 
    BAR = strategy_bar
    HOUSE = strategy_house
    RANDOM = strategy_random
    LAST_WEEK = strategy_last_week
    AVERAGE = strategy_average
    CONTRARY = strategy_contrary

strategy_list : list[Strategy] = [Strategy.BAR, 
                                  Strategy.HOUSE, 
                                  Strategy.RANDOM, 
                                  Strategy.LAST_WEEK, 
                                  Strategy.AVERAGE,
                                  Strategy.CONTRARY]
