import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt
from matplotlib import cm
import shutil

width = shutil.get_terminal_size().columns
np.set_printoptions(linewidth=width)


def plot_surface(ax, x, y, z, alpha):
    
    ax.plot_surface(
        x, y, z, alpha=alpha, edgecolor='none'
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

def plot_mu(values=[1, 2, 3], alpha=0.2):
    for MU in values:
        nu = np.arange(-np.pi, np.pi, 0.1)
        phi = np.arange(-np.pi, np.pi, 0.1)
        
        NU, PHI = np.meshgrid(nu, phi)

        x = a * np.cosh(MU) * np.cos(NU) * np.cos(PHI)
        y = a * np.cosh(MU) * np.cos(NU) * np.sin(PHI)
        z = a * np.sinh(MU) * np.sin(NU)

        plot_surface(ax, x, y, z, alpha=alpha)

def plot_nu(values=[1, 1.5, 2, 2.5], alpha=0.7):
    for NU in values:
        mu = np.arange(-np.pi, np.pi, 0.01)
        phi = np.arange(-np.pi, np.pi, 0.01)
        
        MU, PHI = np.meshgrid(mu, phi)

        x = a * np.cosh(MU) * np.cos(NU) * np.cos(PHI)
        y = a * np.cosh(MU) * np.cos(NU) * np.sin(PHI)
        z = a * np.sinh(MU) * np.sin(NU)

        plot_surface(ax, x, y, z, alpha=alpha)

def plot_phi(values=[1, 1.5, 2, 2.5], alpha=0.5):
    for PHI in values:
        mu = np.arange(-np.pi, np.pi, 0.01)
        nu = np.arange(-np.pi, np.pi, 0.01)
        
        MU, NU = np.meshgrid(mu, nu)

        x = a * np.cosh(MU) * np.cos(NU) * np.cos(PHI)
        y = a * np.cosh(MU) * np.cos(NU) * np.sin(PHI)
        z = a * np.sinh(MU) * np.sin(NU)

        plot_surface(ax, x, y, z, alpha)

def plot_all():
    plot_nu(values=[1], alpha=0.5)
    plot_phi(values=[1, 2], alpha=0.5)
    plot_mu(values=[2.5], alpha=0.5)

if __name__ == "__main__":
    a = 1
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # plot_mu()
    # plot_nu()
    # plot_phi()
    plot_all()
    plt.show()


