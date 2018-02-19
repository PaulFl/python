import numpy as np

tailleMatrice = (4,4)

matrice = np.ones(tailleMatrice);
matrice = matrice*(-1)
print(matrice)

for i in range(4):
    matrice[i][i] = 0

print(matrice)
matrice[1][0] = matrice[0][1] = 1 #Tous les indices sont décalés de parce que les tableaux commencent à 0
print(matrice)
#etc...