import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def ham_Rosenbrock(b, x, y):
    z = (x+2)**2+(y-1)**2+(z-4)**2
    return z
x = np.linspace(start=-30.0, stop=30.0,num=200)
y = np.linspace(start=-30.0, stop=30.0,num=200)
x, y = np.meshgrid(x, y)
z = ham_Rosenbrock(10, x, y)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
rosen_surf = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
ax.set_zlim(0, 200)
fig.colorbar(rosen_surf, shrink=0.5,aspect=5)
plt.show()