import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi)
y = np.sin(x)

plt.plot(x,y, label = "sin")
plt.show()
