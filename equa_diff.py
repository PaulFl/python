import numpy as np
import matplotlib.pyplot as plt

def equa_diff(x0, dt, f):
    x = [x0]
    y = [0]
    for i in range(1000):
        x.append(x[-1] + f(x[-1])*dt)
        y.append(y[-1]+dt)
    return(x,y)

def capa(y):
    return(y)

def harmonique(y):
    return np.array([y[1], -y[0]])
