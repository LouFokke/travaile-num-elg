import numpy as np
import matplotlib.pyplot as plt

# Matrice 4x4 quelconque
matrice_4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Affichage de la matrice sur un graphique
fig, ax = plt.subplots()

# Affichage des nombres sans couleur de fond
for (i, j), val in np.ndenumerate(matrice_4x4):
    ax.text(j, i, str(val), ha='center', va='center', fontsize=10, color='black')

ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)

plt.show()
