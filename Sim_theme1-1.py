# 時間経過による感情の変化とベクトル状態図を描画するプログラム

import numpy as np
import matplotlib.pyplot as plt

# 行列の積を求める関数


def f(A, X):
    return np.dot(A, X)


# システムパラメータの設定
# a:ロミオ自身
# b:ジュリエット→ロミオ
# c:ロミオ→ジュリエット
# d:ジュリエット自身
# R:ロミオの感情の初期値
# J:ジュリエットの感情の初期値
a = float(-5)
b = float(1)
c = float(1)
d = float(2)
R = float(3)
J = float(5)

# その他のシステムパラメータ
# T:シミュレーション時間
# n:試行回数
# delta_T:刻み幅
T = 0
n = 30
delta_T = 0.05


# 各行列を作成
A = np.array([[a, b], [c, d]])
X = np.array([R, J])


# 横軸と縦軸のリスト
plot_t = []
plot_beforeR = []
plot_afterR = []
plot_beforeJ = []
plot_afterJ = []
i = 0
while i < n:
    plot_beforeR.append(X[0])
    plot_beforeJ.append(X[1])
    X += f(A, X) * delta_T
    T += delta_T
    plot_t.append(T)
    plot_afterR.append(X[0])
    plot_afterJ.append(X[1])
    i += 1

# 時間経過による感情の変化をプロット
# 横軸:時間
# 縦軸:R(t),J(t)
plt.figure()
plt.xlabel("time", fontsize=14)
plt.ylabel("R(t),   J(t)", fontsize=14)
plt.plot(plot_t, plot_afterR, color='b', label='Romeo')
plt.plot(plot_t, plot_afterJ, color='r', label='Juliet')
plt.legend()


# ベクトル状態図をプロット
# 横軸:R
# 縦軸:J
plt.figure()
plt.xlabel("R", fontsize=14)
plt.ylabel("J", fontsize=14)
vectorR = [(x - y)*9 for (x, y) in zip(plot_afterR, plot_beforeR)]
vectorJ = [(x - y)*9 for (x, y) in zip(plot_afterJ, plot_beforeJ)]
plt.quiver(plot_beforeR, plot_beforeJ, vectorR, vectorJ,
           angles='xy', scale_units='xy', scale=10, label='Vector')
plt.legend()


# 相図
#gamma_ngtv = np.arange(-100, 0, 0.1)
#gamma_pstv = np.arange(0, 100, 0.1)
#gamma = np.arange(-100, 100, 0.1)
#delta_ngtv = 1 / 4 * gamma_ngtv ** 2
#delta_pstv = 1 / 4 * gamma_pstv ** 2
#fig = plt.figure(figsize=(8, 6))
#ax = fig.add_subplot(111)
# ax.grid()
#ax.set_xlabel("τ", fontsize=14)
#ax.set_ylabel("⊿", fontsize=14)
#ax.set_xlim(-100, 100)
#ax.set_ylim(-100, 100)
# Axesにグラフをプロット
#ax.plot(gamma_ngtv, delta_ngtv, color="green")
#ax.plot(gamma_pstv, delta_pstv, color="yellow")
#ax.axhline(0, color="blue")
#x = [0, 0]
#y = [0, 100]
#ax.plot(x, y, color='black', alpha=2)
#x = [0, -100]
#y = [0, 0]
#ax.plot(x, y, color='red', alpha=2)


# y1とy1の間を塗り潰す
#ax.fill_between(gamma_ngtv, 0, delta_ngtv, alpha=0.5)
#ax.fill_between(gamma_ngtv, delta_ngtv, 100, alpha=0.5)
#ax.fill_between(gamma_pstv, 0, delta_pstv, alpha=0.5)
#ax.fill_between(gamma_pstv, delta_pstv, 100, alpha=0.5)
#ax.fill_between(gamma, -100, 0, alpha=0.5)

plt.show()
