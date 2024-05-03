import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

start_time = time.time()
#Initialization du grid et des conditions frontieres, indices de lignes de 0 à 60 et de 0 à 121 pour les colonnes
poten = np.full((61, 121), -170, dtype=float)
poten[0,30:] = -300 
poten[-1, 30:] = -300
poten[:,-1] = 0
poten[30,45:] = 0 
#Conditions frontieres diagonales
np.fill_diagonal(poten[30:,:], -300)
np.fill_diagonal(np.flipud(poten[:31,:]), -300)

#Enlever les points à gauche des diagonales
for i in range(61):
    for j in range(121):
        if poten[i,j] == -300:
            break
        else:
            poten[i,j] = np.nan     


"""
#Vizualisation des condition frontieres
plt.imshow(poten, cmap='plasma')
plt.colorbar()
plt.show()

"""


def calcul(pot, n_iter):
    prev_pot = pot.copy() 
    for n in range(n_iter):
        for x in range(120): #columnes
            for y in range(60): #lignes
                if pot[y, x] != 0  and pot[y,x] != -300: #Le potentiel seulement en dedans du detecteur
                    if y == 30:
                        pot[y,x] = 0.5*(pot[y,x + 1]+pot[y, x -1])
                    else:
                        pot[y,x] = 0.25*(pot[y,x + 1]+pot[y, x -1] + pot[y +1,x]+pot[y-1, x]) + 0.1 * (pot[y + 1,x]-pot[y-1, x])/(8 * (abs(y - 30)))

        # Calcul de la différence maximale entre les array de potentiel actuel et précédent
        max_diff = np.nanmax(np.abs(pot - prev_pot))
        # Vérification si la différence maximale est inférieure à 0.01
        if max_diff < 0.01:
            print("Number of iterations:", n)
            break
        # Mise à jour de l'array de potentiel précédent pour la prochaine itération
        prev_pot = pot.copy()  
            
    return pot                                                                                



poten = calcul(poten, 10000)

print("Process finished --- %s seconds ---" % (time.time()-start_time))


plt.figure(figsize=(15, 6))
plt.contourf(poten, cmap='plasma', levels=50, vmin = -300, vmax=0)
plt.colorbar(label='Potentiel [V]', ticks = np.linspace(-300,0,7))
plt.title('Potentiel Électrique [r-z]')
plt.xlabel('Z [mm]')
plt.ylabel('R [mm]')
plt.xticks(np.arange(0, 121, 10), np.arange(0, 13, 1)) 
plt.yticks(np.arange(0, 61, 10), np.arange(-3, 4, 1)) 
plt.show()