import numpy as np
import matplotlib.pyplot as plt

def funcPlot():
    f = lambda x: np.sin(x)
    start = 0
    end = 10
    points = 500

    x = np.linspace(start, end, points)
    y = f(x)
    plt.plot(x,y, label="f")
    plt.title("Function plot")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()


