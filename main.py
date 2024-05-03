from numpy import pi, cos, sin, cosh, sinh
import numpy as np
import matplotlib.pyplot as plt


#Grid, pas h = 0.1 mm, plan r(-3 mm à 3mm) et z(0 mm à 12 mm)
h = 0.1
r = np.linspace(-3, 3, int(6 / h)) 
z = np.linspace(0, 12, int(12 / h))


R,Z = np.meshgrid(r,z) 

z_9 = int(9 / h)
z_7_5 = int(7.5/h) 

#Intiialiser la grid à 0 partout
#grid = np.zeros_like(Z)
grid = np.full_like(Z, 30)



#Mettre des conditions frontieres faciles
grid[:z_9,0] = -300
grid[:z_9,-1] = -300
grid[0,:] = 0
grid[0:z_7_5,r == 0] = 0


# Cf Triangle 
np.fill_diagonal(grid[z_9:,:], -300)
np.fill_diagonal(np.fliplr(grid[z_9:,:]), -300)


def calculer(potentiel, n_iter):
    for _ in range(n_iter):
        S = 0
        for j in range(121): #Pour avoir nos 120 lignes de notre grid , soit z
            for i in range(61): #Pour avoir nos 60 colonnes, soit r
                if potentiel[j,i] != 0 and potentiel[j,i] != -300: #Si le pt est ailleurs que les conditions frontieres
                    if i == 30: # Point ou R = 0
                        potentiel[j,i] = 1/2*(potentiel[j+1,i]+potentiel[j-1,i])
                    else:
                        potentiel[i,j]= (potentiel[j,i+1] + potentiel[j,i-1] + potentiel[j+1,i]+ potentiel[j-1,i])/4 + (
                            potentiel[j,i +1] + potentiel[j, i-1])/(8*(30-i))
                        
    return potentiel

potentiel = calculer(grid, n_iter=10000)


plt.contourf(R, Z, potentiel, cmap='coolwarm')
plt.xlabel('r (mm)')
plt.ylabel('z (mm)')
plt.colorbar(label='Potential (V)')
plt.title('Electric Potential Distribution')
plt.show()


'''plt.figure(figsize=(8, 6))
plt.imshow(grid, extent=[r[0], r[-1], z[0], z[-1]], cmap='plasma', aspect='auto', origin='lower')
plt.colorbar(label='Voltage (V)')
plt.title('Voltage Distribution on the Grid')
plt.xlabel('r (mm)')
plt.ylabel('z (mm)')
plt.grid(True)
plt.show()'''
