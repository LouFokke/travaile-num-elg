from numpy import pi, cos, sin, cosh, sinh
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


poten = np.full((61, 121), -100)
poten[0,30:] = -300 #90 car 9/h donne un indice de 90 
poten[-1, 30:] = -300
poten[:,-1] = 0
poten[30,45:] = 0 
np.fill_diagonal(poten[30:,:], -300)
np.fill_diagonal(np.flipud(poten[:31,:]), -300)

for i in range(61):
    for j in range(121):
        if poten[i,j] == -300:
            break
        else:
            poten[i,j] = 100      # Ici les points avec 50 on veux les eliminer apres





def calcul(pot, n_iter):
    for n in range(n_iter):
        pot_last = pot.copy()
        for x in range(121):
            for y in range(61):
                if pot[y, x] != 0 and pot[y, x] != 100 and pot[y,x] != -300: #Le potentiel seulement en dedans du detecteur
                    if y == 30:
                        pot[y,x] = 0.5*(pot[y,x + 1]+pot[y, x -1])
                    else:
                        pot[y,x] = 0.25*(pot[y,x + 1]+pot[y, x -1] + pot[y +1,x]+pot[y-1, x]) #+ (pot[y + 1,x]+pot[y-1, x]/(8 * y))  Faut tu mettre le h lors de la somme?
    return pot                                                                                # Deuxieme terme ne fonctionne pas



poten = calcul(poten, 1000)

# Plotting the result

# Masking the array to not display points equal to 50
masked_poten = np.ma.masked_where(poten == 100, poten)

# Plotting the result using contourf
plt.figure(figsize=(10, 6))
plt.contourf(masked_poten, cmap='plasma', levels = 70)
plt.colorbar(label='Potential')
plt.title('Electric Potential')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

