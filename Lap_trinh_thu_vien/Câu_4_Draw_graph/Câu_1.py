import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def ve_do_thi_yen_ngua():
    def ham_Rosenbrock(b, x, y):
        z = (x/3)**2-(y/2)**2
        return z
    x = np.linspace(start=-20.0, stop=20.0,num=200)
    y = np.linspace(start=-20.0, stop=20.0,num=200)
    x, y = np.meshgrid(x, y)
    z = ham_Rosenbrock(0, x, y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    rosen_surf = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
    ax.set_zlim(0, 200)
    fig.colorbar(rosen_surf, shrink=0.5,aspect=5)
    plt.show()
ve_do_thi_yen_ngua()