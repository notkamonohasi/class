
from setting import * 
from strategy import strategy_list
from util import * 

class Agent : 
    def __init__(self, number) -> None :
        self.number = number
        self.strategy_score_list = [0 for _ in range(len(strategy_list))]

    # softmaxを用いて戦略を決定する
    def decide_strategy(self, turn) -> int : 
        # 最初のターンはランダム
        if turn == 0 : 
            return 2
        else : 
            assert DECIDE_STRATEGY_METHOD in ["argmax", "softmax"]
            if DECIDE_STRATEGY_METHOD == "argmax" : 
                return argmax(self.strategy_score_list)
            elif DECIDE_STRATEGY_METHOD == "softmax" : 
                return softmax(self.strategy_score_list)
            else : 
                assert False 

    # バーに行くかどうかを決定
    # return: 戦略のindex, バーに行くか
    def decide_action(self, bar_record_list : list[float], turn) -> tuple[int, bool] : 
        strategy_index = self.decide_strategy(turn)
        assert 0 <= strategy_index and strategy_index < len(strategy_list)
        action = strategy_list[strategy_index](bar_record_list)
        return strategy_index, action
    
    # agentの状態を更新
    """
        Args: strategy_index: このターンに使ったstrategyのindex
              action: バーに行ったか
              result: バーは空いていたか
    """    
    def update(self, strategy_index : int, action : bool, result : Result) -> None : 
        # バーが混んでいた
        if result == Result.CROWDED : 
            if action == False : 
                self.strategy_score_list[strategy_index] += 1 
            else : 
                self.strategy_score_list[strategy_index] -= 1 
        # バーが空いていた
        elif result == Result.EMPTY : 
            if action == True : 
                self.strategy_score_list[strategy_index] += 1 
            else : 
                self.strategy_score_list[strategy_index] -= 1 



