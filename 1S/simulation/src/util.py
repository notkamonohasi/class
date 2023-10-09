import math 
import random 
from enum import Enum

from setting import * 

random.seed(RANDOM_SEED)

class Result(Enum) : 
    CROWDED = -1 
    EMPTY = 1

def softmax(score_list : list) -> int : 
    exp_score_list = [math.exp(score) for score in score_list]
    exp_score_sum = sum(exp_score_list)
    ratio_list = [exp_score / exp_score_sum for exp_score in exp_score_list] 
    r = random.random()
    pos = 0 
    for idx in range(len(ratio_list)) : 
        pos += ratio_list[idx]
        if pos >= r : 
            return idx 
    assert False 

# argmaxを計算
# 同一scoreが存在するときは、その中からrandomに計算
def argmax(score_list : list) -> int : 
    best_score = -1 * 1e10
    best_index_list = []   # 同率1位のindexをまとめて入れておく
    for i in range(len(score_list)) : 
        score = score_list[i]
        if best_score == score : 
            best_index_list.append(i)
        elif best_score < score : 
            best_score = score
            best_index_list = [i] 
    return best_index_list[random.randrange(0, len(best_index_list))]
