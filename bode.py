import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

# Coefficients in numerator of transfer function
num = [1]
# Coefficients in denominator of transfer function
# High order to low order, eg 1*s^2 + 0.1*s + 1

# Scan over zeta, a parameter for a second-order system

f1 = plt.figure()
den = [1, 1, 1]
s1 = signal.lti(num, den)

range: np.arange(0.1, 5, 0.01)
w, mag, phase = signal.bode(s1, np.arange(0.1, 5, 0.01).tolist())
plt.semilogx(w, mag, color="blue", linewidth="1")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.savefig("c:\\mag.png", dpi=300, format="png")

plt.figure()


den = [1, 1.4, 1]
s1 = signal.lti(num, den)
w, mag, phase = signal.bode(s1, np.arange(0.1, 10, 0.02).tolist())
plt.semilogx(w, phase, color="red", linewidth="1.1")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
