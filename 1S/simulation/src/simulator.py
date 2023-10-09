
from agent import Agent
from bar import Bar
from setting import * 
from strategy import strategy_list
from visualize import * 

class Simulator : 
    def __init__(self) -> None:
        self.agent_list : list[Agent] = [Agent(number) for number in range(AGENT_SIZE)]
        self.bar = Bar()

        # 結果記録
        self.strategy_index_mat : list[list[int]] = []   # 各ターンでの各agentの戦略
    
    # シミュレーションスタート
    def start(self) -> None: 
        # シミュレーション
        for turn in range(MAX_TURN) : 
            self.loop(turn)

        # 結果の可視化
        self.visualize_result()

    # 1ターンの挙動
    def loop(self, turn) -> None :
        strategy_index_list : list[int] = []   # 各agentの戦略
        action_list : list[bool] = []   # バーに行くかどうか

        # agentが行動を決定
        for i in range(len(self.agent_list)) : 
            assert i == self.agent_list[i].number
            strategy_index, action = self.agent_list[i].decide_action(self.bar.bar_record_list, turn) 
            strategy_index_list.append(strategy_index)
            action_list.append(action)
        
        # agentの行動を記録
        self.strategy_index_mat.append(strategy_index_list)

        # barの結果
        result = self.bar.get_result(action_list)

        # barを更新
        self.bar.update(action_list)

        # agentを更新
        for i in range(len(self.agent_list)) : 
            assert i == self.agent_list[i].number
            self.agent_list[i].update(strategy_index_list[i], action_list[i], result)

    # 結果を可視化
    def visualize_result(self) -> None : 
        if RESULT_DIR.exists() == False : 
            RESULT_DIR.mkdir() 

        # バーの混雑率を可視化
        visualize_bar_record_list(RESULT_DIR.joinpath("bar_record.png"), 
                                  self.bar.bar_record_list)
        
        # 使われた戦略を可視化
        visualize_strategy(RESULT_DIR.joinpath("strategy.gif"), 
                           self.strategy_index_mat)
