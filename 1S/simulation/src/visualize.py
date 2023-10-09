from pathlib import Path 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

from setting import * 
from strategy import strategy_list

# バーの混雑率を可視化
def visualize_bar_record_list(fig_save_path : Path, 
                              bar_record_list : list[int]) -> None : 
    time_list = [i for i in range(len(bar_record_list))]
    plt.plot(time_list, bar_record_list)
    plt.hlines(SATISFY_RATIO, 0, MAX_TURN * 1.05, colors="red", linewidth=3)
    plt.ylim(min(0.2, SATISFY_RATIO - 0.1), max(0.8, SATISFY_RATIO + 0.1))
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel("turn", fontsize=14)
    plt.ylabel("congestion rate", fontsize=14)
    plt.title("congestion rate", fontsize=18)
    plt.grid()
    plt.savefig(fig_save_path)
    plt.close()

# 使われている戦略の変化を動画で可視化する
"""
    Args: fig_save_path: 動画を保存するファイル名
          strategy_index_mat: iターン目でj番目のagentがとった戦略
"""
def visualize_strategy(fig_save_path : Path, 
                       strategy_index_mat : list[list[int]]) -> None : 
    assert fig_save_path.suffix == ".gif"

    # frameを作成する関数
    def plot(frame_number : int): 
        plt.cla()
        plt.bar([i for i in range(len(strategy_list))], 
                [strategy_index_mat[frame_number].count(i) / AGENT_SIZE for i in range(len(strategy_list))], 
                tick_label=[strategy_list[i].__name__ for i in range(len(strategy_list))], 
                color="blue")
        plt.ylim(0, 1)
        plt.xticks(rotation=90)
        plt.yticks(fontsize=12)
        plt.xlabel("strategy name", fontsize=14)
        plt.ylabel("acceptance rate", fontsize=14)
        plt.title(f'turn={frame_number}', fontsize=18)
        plt.grid()

    plt.rcParams["figure.subplot.bottom"] = 0.40
    fig = plt.figure()
    anim = FuncAnimation(fig, plot, frames=MAX_TURN, interval=100)
    anim.save(fig_save_path, writer="pillow")
    plt.close()