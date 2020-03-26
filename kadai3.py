from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random


class GradientDescent:
    def __init__(self, f, df, eta=0.00005, eps=1e-6):
        self.f = f    # 最適化する関数
        self.df = df    # 関数の勾配
        self.eta = eta    # 学習率
        self.eps = eps    # 学習のストップ判定に用いる定数
        self.path = None  # 学習の経過、初期値は空
        self.eta_len = [0]

    def solve(self, x):
        path = []
        grad = self.df(x)    # 勾配
        path.append(x)

        while (grad**2).sum() > self.eps:
            x = x - self.eta * grad
            grad = self.df(x)
            path.append(x)
            self.eta_len.append(len(path))
        self.path_ = np.array(path)   # 学習の経過
        self.x_ = x    # 最適化された変数の値
        self.opt_ = f(x)    # 最適化後の f(x)の値
        self.grad_ = grad  # 最適化後の勾配


def f(xy):
    x = xy[0]
    y = xy[1]
    z = xy[2]
    return 30 + x**2 - 10 * np.cos(2*np.pi*x) + y**2 - \
        10 * np.cos(2*np.pi*y) + z**2 - 10 * np.cos(2*np.pi*z)


def df(xy):
    x = xy[0]
    y = xy[1]
    z = xy[2]
    return np.array([2*x + 20*np.pi*np.sin(2*np.pi*x), 2*y + 20*np.pi*np.sin(2*np.pi*y), 2*z + 20*np.pi*np.sin(2*np.pi*z)])


x = 0
result = []
for a in np.arange(-5, 5.12, 0.5):
    for b in np.arange(-5, 5.12, 0.5):
        for c in np.arange(-5, 5.12, 0.5):

            gd = GradientDescent(f, df)
            # a = random.uniform(-5.12, 5.12)
            # b = random.uniform(-5.12, 5.12)
            # c = random.uniform(-5.12, 5.12)
            initial = np.array([a, b, c])
            gd.solve(initial)

            # print('更新後の変数: {}'.format(gd.x_))    # 更新後の変数
            # print('更新後のf(x,y,z): {:.3}'.format(gd.opt_))  # 更新後のf(x,y)
            result.append(round(gd.opt_, 2))

            # pathのプロット
            x_path = gd.path_[:, 0]
            y_path = gd.path_[:, 1]
            z_path = gd.path_[:, 2]
            w_path = f(np.array((x_path, y_path, z_path)))

            eta_len = np.array(gd.eta_len)
            plt.plot(gd.eta_len, w_path)    # 更新を図示

            if x < len(eta_len):  # 最大繰り返し回数のカウント
                x = len(eta_len)

set_result = set(result)
print(set_result)
print(len(result))
print(len(set_result))
print(x)  # 最大繰り返し回数

# {0.99, 1.99, 2.98, 3.98, 4.97, 5.97, 0.0, 7.96, 8.95,
#  9.95, 10.94, 11.94, 12.93, 13.93, 15.92, 16.91, 17.91,
#  18.9, 19.9, 20.89, 21.89, 23.88, 24.87,
#  25.87, 26.86, 28.85, 29.85, 31.84, 32.83,
#  33.83, 34.82, 35.82, 37.81, 40.79, 41.79, 42.78, 44.77,
#  47.76, 49.75, 50.74, 53.73, 56.71, 58.7, 65.67, 74.62}
#  重複なし 45


# fig = plt.figure(figsize=(10, 7))
# ax = Axes3D(fig)
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("f(x, y)")
# ax.plot3D(x_path, y_path, z_path, color='red')

# # f(x, y)曲面のプロット
# x_curve = np.linspace(0, 5)
# y_curve = np.linspace(0, 5)
# X_curve, Y_curve = np.meshgrid(x_curve, y_curve)
# Z_curve = f(np.array((X_curve, Y_curve)))

# ax.plot_wireframe(X_curve, Y_curve, Z_curve)
# plt.legend()
plt.show()
