# ベクトル場を描画するプログラム

import numpy as np
import matplotlib.pyplot as plt


# システムパラメータの設定
# a:ロミオ自身
# b:ジュリエット→ロミオ
# c:ロミオ→ジュリエット
# d:ジュリエット自身
a = float(-4)
b = float(4)
c = float(4)
d = float(-4)


plot_beforeR = []
plot_afterR = []
plot_beforeJ = []
plot_afterJ = []


for R in range(-20, 21, 2):
    for J in range(-20, 21, 2):
        dR = a * R + b * J
        dJ = c * R + d * J
        plot_beforeR.append(R)
        plot_beforeJ.append(J)
        plot_afterR.append(dR)
        plot_afterJ.append(dJ)


# ベクトル場をプロット
# 横軸:R
# 縦軸:J
plt.figure()
plt.xlabel("R", fontsize=14)
plt.ylabel("J", fontsize=14)
plt.quiver(plot_beforeR, plot_beforeJ, plot_afterR, plot_afterJ,
           angles='xy', scale_units='xy', label='Vector')
plt.legend()
plt.show()
