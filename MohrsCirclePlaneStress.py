import numpy as np
import matplotlib.pyplot as plt

import math


def principal_stresses(nx, ny, tau):
    p1 = (nx + ny)/2 + math.sqrt(((nx - ny)/2)**2 + tau**2)
    p2 = (nx + ny)/2 - math.sqrt(((nx - ny)/2)**2 + tau**2)
    p_avg = (p1 + p2) / 2
    tau_max = math.sqrt(((nx - ny)/2)**2 + tau**2)
    theta_p = math.atan(tau/((nx-ny)/2))/2
    theta_s = math.atan((-(nx-ny)/2)/tau)/2

    return p1, p2, p_avg, tau_max, theta_p, theta_s

def MohrsCirclePlaneStress(nx, ny, tau):
    # Calculate average normal
    sigma_avg = (nx + ny) / 2
    # Calculate Radius
    R = np.sqrt(((nx - ny) / 2) ** 2 + tau ** 2)
    # Call principal stress Function to get principal stresses
    p1, p2, p_avg, tau_max, theta_p, theta_s = principal_stresses(nx, ny, tau)
    # Equation of circle
    y1 = np.linspace(-2.5 * abs(tau_max), 2.5*abs(tau_max), num=1000)
    y2 = np.linspace(2.5 * abs(tau_max), -2.5*abs(tau_max), num=1000)
    sigma_xprime1 = np.ones(y1.shape) * sigma_avg + np.sqrt(R ** 2 - y1 ** 2)
    sigma_xprime2 = np.ones(y2.shape) * sigma_avg - np.sqrt(R ** 2 - y2 ** 2)
    # Plot Circle
    plt.plot(sigma_xprime1, y1, label='shear(normal)')
    plt.plot(sigma_xprime2, y2, label='shear(normal)')
    plt.grid()
    plt.title('Mohr s Circle')
    plt.xlabel('sigma (normal stress)')
    plt.ylabel('-tau (shear stress)')
    plt.ylim([-2.5 * abs(tau_max), 2.5 * abs(tau_max)])
    # Plot important points
    plt.plot(p1, 0, '.', markersize=20)
    plt.plot(p2, 0, '.', markersize=20)
    plt.plot(p_avg, 0, '.', markersize=20)
    plt.plot(p_avg, -tau_max, '.', markersize=20)
    plt.plot(p_avg, tau_max, '.', markersize=20)
    plt.plot(nx, tau, '.', markersize=20)
    plt.plot(ny, tau, '.', markersize=20)
    plt.legend(['shear(normal)', 'shear(normal)', 'principal stress 1', 'principal stress 2',
                'average normal stress', '(p avg, -tau max)', '(p avg, tau max)',
                'REF1(nx, tau)', 'REF2(ny, tau)'])
    plt.axis('equal')
    plt.show()

nx = int(input("What is the Normal Stress in the x-direction?: "))

ny = int(input("What is the Normal Stress in the y-direction?: "))

tau = int(input("What is the Shear Stress?: "))

MohrsCirclePlaneStress(nx,ny,tau)