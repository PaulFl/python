def newton(f, df, u0, epsilon):
    u = u0
    while abs(f(u)) > epsilon:
        u -= f(u)/df(u)
    return u

import numpy as np
print(newton(np.sin, np.cos, 3.0, 0.1))
