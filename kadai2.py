import numpy as np
import random
import sys
import matplotlib.pyplot as plt


# 基本形
# M = 100  # 全固体数
# T = 1000  # 繰り返し回数
# p_c = 0.5  # 交叉確率
# p_m = 0.05  # 突然変異確率
# alpha = 0.05  # ペナルティ係数


M = 100  # 全固体数
T = 1000  # 繰り返し回数
p_c = 0.5  # 交叉確率
p_m = 0.05  # 突然変異確率
alpha = 0.05  # ペナルティ係数
path = 'kp20.txt'  # ファイルからデータを読みこむ


# num = 8: alpha = 1.75
# 最大適応度をもつ個体: [1 1 1 0 1 0 1 0]
# 最大適応度をもつ個体の価値: 45
# 最大適応度をもつ個体の容量: 25


# num = 20: alpha = 3.75
# 最大適応度をもつ個体: [0 1 1 1 0 1 0 1 0 1 0 1 1 0 1 0 0 0 0 1]
# 最大適応度をもつ個体の価値: 190
# 最大適応度をもつ個体の容量: 35


# num = 50: alpha = 4.8
# 最大適応度をもつ個体: [1 1 0 1 1 0 0 1 1 0 0 1 0 0 1 1 1 0 1 0 1 1 1 0 0 1 1 0 1 1 1 0 1 0 0 1 1
#              0 0 1 1 1 1 1 1 1 0 0 1 0]
# 最大適応度をもつ個体の価値: 827
# 最大適応度をもつ個体の容量: 85


# 100の時: alpha = 3.8
# 最大適応度をもつ個体: [1 0 1 0 1 1 1 0 0 1 0 0 0 1 0 1 0 1 1 0 0 0 1 0 1 1 0 1 0 1 0 0 0 1 1 1 0
#              1 1 0 1 0 1 1 1 0 0 1 0 1 1 1 1 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1 1 0 0 0
#              1 1 1 1 0 1 0 0 1 1 1 1 0 1 1 1 0 1 0 0 0 1 0 1 1 0]
# 最大適応度をもつ個体の価値: 1164
# 最大適応度をもつ個体の容量: 150


def Select(Knap, prize, weight, capa):  # 選択を行う関数
    sum_g = np.sum(Knap * prize, axis=1)
    sum_f = np.sum(Knap * weight, axis=1)
    diff = sum_f - capa
    diff = [0 if i < 0 else i for i in diff]
    diff = np.array(diff)
    g = sum_g - alpha * sum_f
    for i in range(len(sum_g)):
        if g[i] <= 0:
            g[i] = 0
            sum_g[i] = 0
        if sum_f[i] > capa:
            g[i] = 0
            sum_g[i] = 0
    g_max = np.argmax(sum_g)
    newG = np.sum(g)
    # 例外処理
    if newG == 0:
        print('Error!!!')
        sys.exit()
    p_G = g / newG
    new = []
    index = [i for i in range(M)]
    for i in range(M):
        s = np.random.choice(index, p=p_G)
        new.append(Knap[s])
    return np.array(new), np.average(sum_g), max(sum_g)


def Cross(Knap, num):  # 一点交叉
    cross = [i for i in range(M)]
    for i in range(int(M / 2)):
        p = random.random()
        if p < p_c:
            change_pair = random.sample(cross, 2)
            change_place = np.random.randint(0, num)
            temp = Knap[change_pair[0]][change_place]
            Knap[change_pair[0]][change_place] = Knap[change_pair[1]][change_place]
            Knap[change_pair[1]][change_place] = temp


def Mutation(Knap, num):  # 突然変異
    for i in range(int(M)):
        p = random.random()
        change_place = np.random.randint(0, num)
        if p < p_m:
            Knap[i][change_place] = 1 - Knap[i][change_place]


def main():
    with open(path) as f:
        s = f.read()
        l = [x.strip() for x in s.split()]
        m = [int(n) for n in l]
        num = int(l[0])
        capacity = int(l[1])
        prize = [m[n] for n in range(2, 2 + num)]
        weight = [m[n] for n in range(2+num, 2 + 2*num)]

    # 各種データ
    print('----------------------')
    print('個体数:', M)
    print('荷物数:', num)
    print('容量:', capacity)
    print('荷物の価値:', prize)
    print('荷物の容量:', weight)
    print('----------------------')

    # 初期世代の個体集合の生成
    Knapsack = np.random.randint(0, 2, (M, num))
    g_ave = []
    g_max = []

    # 世代交代
    for i in range(T):
        Knapsack, gave, gmax = Select(Knapsack, prize, weight, capacity)
        g_ave.append(gave)
        g_max.append(gmax)
        Cross(Knapsack, num)
        Mutation(Knapsack, num)

    print('最大適応度をもつ個体:', Knapsack[0])
    print('最大適応度:', g_max[T-1])
    print('平均適応度:', g_ave[T-1])

    t = [i for i in range(T)]
    plt.ylim(70, 200)
    plt.xscale('log')
    plt.xlabel('t', fontsize=16)
    plt.ylabel('f', fontsize=16)
    plt.plot(t, g_ave, label='g_ave')
    plt.plot(t, g_max, label='g_max')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
