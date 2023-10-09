
from util import * 
from setting import * 

class Bar : 
    def __init__(self) -> None:
        self.bar_record_list : list[float] = []

    # バーに行くべきだったかどうかの判定を行う
    def get_result(self, action_list : list[bool]) -> Result : 
        assert len(action_list) == AGENT_SIZE
        visit_count = sum(action_list)   # バーに来た人数
        visit_ratio = visit_count / AGENT_SIZE   # バーに来た割合

        # visit_ratioがSATISFY_RATIOを下回っているならバーに来て満足、上回っているならバーに行かない方が良かった
        if visit_ratio <= SATISFY_RATIO : 
            return Result.EMPTY 
        else : 
            return Result.CROWDED
        
    # barの状態を更新
    def update(self, action_list : list[bool]) -> None : 
        assert len(action_list) == AGENT_SIZE
        visit_count = sum(action_list)   # バーに来た人数
        visit_ratio = visit_count / AGENT_SIZE   # バーに来た割合
        self.bar_record_list.append(visit_ratio)


