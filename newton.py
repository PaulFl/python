def newton(f, df, u0, epsilon):
    u = u0
    while abs(f(u)) > epsilon:
        u -= f(u)/df(u)
    return u

import numpy as np
print(newton(np.sin, np.cos, 3.0, 0.1))

def f(x):
    return (x+x**3/3+1)*np.exp(x**2/2)

def df(x):
    return (1+x+2*x**2+x**4/3)*np.exp(x**2/2)


def newton2(f, df, a1):
    fin = False
    a = a1
    while not fin:
        a -= f(a)/df(a)
        #if (f(a) < 0 and f(a+1e-6) > 0) or (f(a) > 0 and f(a-1e-6) < 0):
        if f(a) * f(a+1e-6) < 0 or f(a) * f(a-1e-6) < 0:
            fin = True
    return a