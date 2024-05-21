from scipy.integrate import quad

fun46 = lambda x, a, b: a * x ** 2 + b * x
I1 = quad(fun46, 0, 1, args=(2, 1))
I2 = quad(fun46, 0, 1, args=(2, 10))
print("I1 =", I1[0], ", 精度 ", I1[1])
print("I2 =", I2[0], ", 精度 ", I2[1])
