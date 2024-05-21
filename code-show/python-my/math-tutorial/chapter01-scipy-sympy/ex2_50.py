import sympy as sp

sp.var('x1 x2')
fun50_1 = lambda x1, x2: x1 ** 2 + x2 ** 2 - 1
fun50_2 = lambda x1, x2: x1 - x2
s = sp.solve([fun50_1(x1, x2), fun50_2(x1, x2)], [x1, x2])
print(f"第一组解为：{s[0]}")
print(f"第二组解为：{s[1]}")

# 定义符号数组
x = sp.var('x:2')  # x0 x1
s2 = sp.solve([fun50_1(x[0], x[1]), fun50_2(x[0], x[1])], x)
print(f"所有解为：{s2}")
