from numpy import pi, cos, sin, cosh, sinh
import numpy as np
import matplotlib.pyplot as plt

#Grid, pas h = 0.1 mm, plan r(-3 mm à 3mm) et z(0 mm à 12 mm)
h = 0.1
r = np.linspace(-3, 3, int(6 / h) + 1)  # Adjusting the number of points to match h
z = np.linspace(0, 12, int(12 / h) + 1)

R,Z = np.meshgrid(r,z) 

z_9 = int(9 / h)
z_7_5 = int(7.5/h)

#Intiialiser la grid à 0 partout
grid = np.zeros_like(Z)

#Mettre des conditions frontieres faciles
grid[:z_9,0] = -300
grid[:z_9,-1] = -300
grid[0,:] = 50
grid[0:z_7_5,r == 0] = 50



# Cf Triangle 
np.fill_diagonal(grid, 50)

plt.figure(figsize=(8, 6))
plt.imshow(grid, extent=[r[0], r[-1], z[0], z[-1]], cmap='jet', aspect='auto', origin='lower')
plt.colorbar(label='Voltage (V)')
plt.title('Voltage Distribution on the Grid')
plt.xlabel('r (mm)')
plt.ylabel('z (mm)')
plt.grid(True)
plt.show()