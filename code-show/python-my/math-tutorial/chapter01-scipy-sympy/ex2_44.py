from scipy.optimize import fsolve, root

# 求解非线性方程
fun44 = lambda x: (x ** 980) - 5.01 * (x ** 979) + 7.398 * (x ** 978) - 3.388 * (x ** 977) - (x ** 3) \
                  + 5.01 * (x ** 2) - 7.398 * x + 3.388
x1 = fsolve(fun44, 1.5, maxfev=4000)  # 在给定初值1.5附近有一个实根  函数调用4000次
x2 = root(fun44, 1.5)
print(f"{x1}\n\n{x2}\n\n")

# 求解非线性方程组 -> F(X)=0 向量函数
fun44_vec = lambda x: [x[0] ** 2 + x[1] ** 2 - 1, x[0] - x[1]]
s1 = fsolve(fun44_vec, [1, 1])
s2 = root(fun44_vec, [1, 1])
print(f"{s1}\n\n{s2}\n\n")
