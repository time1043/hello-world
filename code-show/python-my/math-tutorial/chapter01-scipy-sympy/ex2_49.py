import sympy as sp

a, b, c, x = sp.symbols('a,b,c,x')
fun49 = lambda x: a * (x ** 2) + b * x + c
x0 = sp.solve(fun49(x), x)
print(x0)
