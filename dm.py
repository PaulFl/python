import numpy as np
import matplotlib.pyplot as plt

def simulation(F0, n, tau):
    q = len(F0)
    r = tau * (q+1)**2
    Iq = np.eye(q)
    B = np.zeros((q,q))
    for i in range(q):
        for j in range(q):
            if abs(i-j) == 1:
                B[i,j] = 1
    A = (1-2*r)*Iq + r*B
    F = [F0]
    x = [i/(q+1) for i in range(q)]
    for i in range(n):
        F.append(A.dot(F[-1]))
        plt.plot(x, F[i])
    plt.show()
    return F[-1]
