from scipy.misc import derivative

fx = lambda x: x ** 3 + x ** 2
derivative(fx, 1.0, dx=1e-6)
