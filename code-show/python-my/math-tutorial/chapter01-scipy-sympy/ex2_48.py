import sympy as sym

x, y, z = sym.symbols('x, y, z')  # 定义符号变量 (逗号分隔 或空格分隔)
f, g = sym.symbols('f, g', cls=sym.Function)  # 定义符号函数
y = sym.Function('y')  # 定义符号

sym.var('x, y, z')  # 定义符号变量 (逗号分隔 或空格分隔)
sym.var('f, g', cls=sym.Function)  # 定义符号函数
