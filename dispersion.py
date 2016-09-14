'''This script plots in 3d the dispersion relation for the shallow water equations'''

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

f = 2*10**(-4) #Coriolis parameter (/s)
g = 9.81 #Acceleration due to gravity (m/s)
#g = 9.81*10**(-6) #1000km/s
H = 3*10**3 #Scale height for oceans (m)
#H = 3*10**(-3) #In 1000km

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-3*10**(-6), 3*10**(-6) , 1*10**(-7)) #In per m
Y = np.arange(-3*10**(-6), 3*10**(-6) , 1*10**(-7))

#X = np.arange(-1, 1 , 0.1) #In per micrometre
#Y = np.arange(-1, 1 , 0.1)

X, Y = np.meshgrid(X, Y)

#Z = np.sqrt(f**2 + g*H*(X**2 + Y**2))
Z = (f**2 + g*H*(X**2 + Y**2))**(1./2)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

#ax.set_zlim(0, 10000)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.set_xlabel('k, wavenumber')
ax.set_ylabel('l, wavenumber')
ax.set_zlabel('w, frequency')

fig.colorbar(surf, shrink=0.5, aspect=5)


plt.show()
