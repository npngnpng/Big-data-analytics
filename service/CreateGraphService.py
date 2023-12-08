import numpy as np
import matplotlib.pyplot as plt


def createDoubleStickGraph(ax, x, y, before: dict, after: dict, title: str, length: int):
    index = np.arange(length)
    bar_width = 0.25

    ax[x, y].bar(index, before.values(), bar_width, alpha=0.4, color='red', label='코로나 이전')
    ax[x, y].bar(index + bar_width, after.values(), bar_width, alpha=0.4, color='blue', label='코로나 이후')
    ax[x, y].set_xticks(np.arange(bar_width, length + bar_width, 1), before.keys(), rotation=90)
    if y == 0:
        ax[x, y].set_yticks(np.arange(10000000, 200000000, 20000000), np.arange(10000000, 200000000, 20000000))
    elif y == 1:
        ax[x, y].set_yticks(np.arange(10000, 2000000, 200000), np.arange(10000, 2000000, 200000))

    ax[x, y].set_xlabel('지역', size=13)
    ax[x, y].set_ylabel('방문자수', size=13)
    ax[x, y].set_title(title)
    ax[x, y].legend()


def createStickGraph(value: dict, length: int):
    index = np.arange(length)
    plt.bar(index, value.values(), alpha=0.4, color='red', label='코로나 이전')
    plt.xticks(index, value.keys())
