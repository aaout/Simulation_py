from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


class GradientDescent:
    def __init__(self, f, df, eta=0.004, eps=1e-6):
        self.f = f    # 最適化する関数
        self.df = df    # 関数の勾配（１次導関数）
        self.eta = eta    # 学習率
        self.eps = eps    # 学習のストップ判定に用いる定数
        self.path = None  # 学習の経過、初期値は空
        self.eta_len = [0]

    def solve(self, x):
        path = []
        grad = self.df(x)    # 勾配
        path.append(x)

        # 多変数の場合のノルムの大きさとself.epsを比較
        # self.epsの二乗より大きい場合、xの更新を続ける
        while (grad**2).sum() > self.eps**2:
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
    return np.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1


def df(xy):
    x = xy[0]
    y = xy[1]
    return np.array([2*x - 2*y + np.cos(x + y) - 1.5, -2*x + 2*y + np.cos(x + y) + 2.5])


gd = GradientDescent(f, df)
initial = np.array([2, 4])
gd.solve(initial)

np.set_printoptions(precision=7, suppress=True)    # 有効桁数の設定

print('更新後の変数: {}'.format(gd.x_))    # 更新後の変数: [-0.173913 -1.086956]
print('更新後のf(x,y): {:.3}'.format(gd.opt_))    # 更新後のf(x,y): -0.238
print('更新後の勾配: {}'.format(gd.grad_))    # 更新後の勾配: [0.0000001 0.000001 ]


# pathのプロット
x_path = gd.path_[:, 0]
y_path = gd.path_[:, 1]
z_path = f(np.array((x_path, y_path)))

eta_len = np.array(gd.eta_len)
plt.xlabel('n')
plt.ylabel('x_n')
plt.plot(gd.eta_len, z_path)    # 更新を図示
print(len(eta_len))  # 繰り返し回数

fig = plt.figure(figsize=(10, 7))
ax = Axes3D(fig)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.plot3D(x_path, y_path, z_path, color='red')

# f(x, y)曲面のプロット
x_curve = np.linspace(0, 5)
y_curve = np.linspace(0, 5)
X_curve, Y_curve = np.meshgrid(x_curve, y_curve)
Z_curve = f(np.array((X_curve, Y_curve)))

ax.plot_wireframe(X_curve, Y_curve, Z_curve)
plt.legend()
plt.show()
