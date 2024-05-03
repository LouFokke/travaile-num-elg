import numpy as np
import matplotlib.pyplot as plt

poten = np.full((61, 121), -100)
poten[0, 30:] = -300
poten[-1, 30:] = -300
poten[:, -1] = 0
poten[30, 45:] = 0
np.fill_diagonal(poten[30:], -300)
np.fill_diagonal(np.flipud(poten[:31, :]), -300)

for i in range(61):
    for j in range(121):
        if poten[i,j] == -300:
            break
        else:
            poten[i,j] = -600      # Ici les points avec -600 on veux les eliminer apres


def calcul(pot, n_iter):
    for n in range(n_iter):
        for x in range(1, 120):
            for y in range(1, 60):
                if pot[y, x] != 0 and pot[y, x] != -600 and pot[y, x] != -300:
                    if y == 30:
                        pot[y, x] = 0.5 * (pot[y, x + 1] + pot[y, x - 1])

                    #elif y == 30 and (x in range(0, 45)):
                        #0.25 * (pot[y, x + 1] + pot[y, x - 1] + pot[y + 1, x] + pot[y - 1, x])

                    elif y != 30:
                        pot[y, x] = 0.25 * (pot[y, x + 1] + pot[y, x - 1] + pot[y + 1, x] + pot[y - 1, x]) + 0.1 * (
                                    pot[y + 1, x] - pot[y - 1, x]) / (8 * abs(30 - y))
    return pot


poten = calcul(poten, 1000)

# Plotting the result
masked_poten = np.ma.masked_where(poten == -600, poten)

plt.figure(figsize=(10, 6))
plt.contourf(masked_poten, cmap='plasma', levels=1000)
plt.colorbar(label='Potential')
plt.title('Electric Potential')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
