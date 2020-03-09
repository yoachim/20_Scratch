import numpy as np
from scipy.optimize import minimize
from numba import jit


def thetaphi2xyz(theta, phi):
    x = np.sin(phi)*np.cos(theta)
    y = np.sin(phi)*np.sin(theta)
    z = np.cos(phi)
    return x, y, z


def xyz2thetaphi(x, y, z):
    phi = np.arccos(z)
    theta = np.arctan2(y, x)
    return theta, phi


def fib_sphere_grid(npoints):
    """
    Use a Fibonacci spiral to distribute points uniformly on a sphere.

    based on https://people.sc.fsu.edu/~jburkardt/py_src/sphere_fibonacci_grid/sphere_fibonacci_grid_points.py

    Returns theta and phi in radians
    """

    phi = (1.0 + np.sqrt(5.0)) / 2.0

    i = np.arange(npoints, dtype=float)
    i2 = 2*i - (npoints-1)
    theta = (2.0*np.pi * i2/phi) % (2.*np.pi)
    sphi = i2/npoints
    phi = np.arccos(sphi)
    return theta, phi


def x02sphere(x0):
    x0 = x0.reshape(3, int(x0.size/3))
    x = x0[0, :]
    y = x0[1, :]
    z = x0[2, :]

    r = np.sqrt(x**2 + y**2 + z**2)
    x = x/r
    y = y/r
    z = z/r

    return np.concatenate((x, y, z))


@jit()
def elec_p_xyx_loop(x0, x=None, y=None, z=None):
    """Electric potential of electrons on a sphere
    do this with a brutal loop that can be numba ified
    """
    if x0 is not None:
        x0 = x0.reshape(3, int(x0.size/3))
        x = x0[0, :]
        y = x0[1, :]
        z = x0[2, :]
    U = 0.

    r = np.sqrt(x**2 + y**2 + z**2)
    x = x/r
    y = y/r
    z = z/r

    npts = x.size
    for i in range(npts-1):
        for j in range(i+1, npts):
            dsq = (x[i]-x[j])**2 + (y[i]-y[j])**2 + (z[i]-z[j])**2
            U += 1./np.sqrt(dsq)
    return U


@jit()
def force_vec(x0):
    """Find the non-radial vector for the force on each electron
    """
    x0 = x0.reshape(3, int(x0.size/3))
    x = x0[0, :]
    y = x0[1, :]
    z = x0[2, :]

    npts = x.size

    forces = np.zeros((3, npts))
    for i in range(npts):
        for j in range(i+1, npts):
            d_x = x[i]-x[j]
            d_y = y[i]-y[j]
            d_z = z[i]-z[j]
            dsq = (d_x)**2 + (d_y)**2 + (d_z)**2

            f_x = d_x/dsq
            f_y = d_y/dsq
            f_z = d_z/dsq

            forces[:, i] += [f_x, f_y, f_z]
            forces[:, j] += -1.*[f_x, f_y, f_z]

    for i in range(npts):
        # magnitude of the force along the radial direction
        f_r = forces[0, i]*x[i] + forces[1, i]*y[i] + forces[2, i]*z[i]
        f_r_sqrt = f_r**0.5
        forces[0, i] = forces[0, i]-f_r_sqrt*x[i]
        forces[1, i] = forces[1, i]-f_r_sqrt*y[i]
        forces[2, i] = forces[2, i]-f_r_sqrt*z[i]

    max_force = np.max(forces[0, :]**2+forces[1, :]**2+forces[2, :]**2)**0.5

    return forces/max_force


def new_pot(a, x0, forces):
    x0 = x0.reshape(3, int(x0.size/3))
    x = x0[0, :]
    y = x0[1, :]
    z = x0[2, :]

    x += a*forces[0, :]
    y += a*forces[1, :]
    z += a*forces[2, :]

    new_u = elec_p_xyx_loop(None, x=x, y=y, z=z)
    return new_u


def shift_to_min(x0, forces):
    """Given positions and forces, figure out how much to scale the forces to move the points
    """
    npts = x0.size/3
    area = 4*np.pi
    ave_dist = np.sqrt(area/npts)

    fit_result = minimize(new_pot, ave_dist/2., (x0, forces))
    return fit_result




