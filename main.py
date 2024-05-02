from numpy import pi, cos, sin, cosh, sinh
import numpy as np
import pylab as plt


#Grid, pas h = 0.1 mm, plan r(-3 mm à 3mm) et z(0 mm à 12 mm)

r = np.linspace(0,12,(12/0.1))
z = np.linspace(-3,3, 6/0.1)
r,z = np.meshgrid(r,z) 