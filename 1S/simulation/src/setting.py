from const import ROOT_DIR

RANDOM_SEED = 20230808   # 乱数のシード

SATISFY_RATIO = 0.60   # これを上回るとバーが混雑している判定
AGENT_SIZE = 1000   # agentの数
MAX_TURN = 1000   # 週の数

DECIDE_STRATEGY_METHOD = "softmax"   # 戦略の決定方法, softmax or argmax

RESULT_DIR = ROOT_DIR.joinpath("Result")


