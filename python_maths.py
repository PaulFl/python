import numpy as np

A = np.array([[0, 1/4, 1/4, 1/4, 1/4],
              [1/3, 0, 1/3, 0, 1/3],
              [1/3, 1/3, 0, 1/3, 0],
              [1/3, 0, 1/3, 0, 1/3],
              [1/3, 1/3, 0, 1/3, 0]])

eyeN = np.eye(5)

zerosN = np.zeros((5,5))

tL = np.linalg.solve((A-eyeN).transpose(), zerosN)

B = A.transpose()

P = np.poly(B)

C = 12*B

PC = np.poly(C)

racines = np.roots(PC)