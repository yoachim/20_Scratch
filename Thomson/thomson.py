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


@jit()
def xyz2sphere(x, y, z):

    r = np.sqrt(x**2 + y**2 + z**2)
    x = x/r
    y = y/r
    z = z/r

    return x, y, z


@jit()
def elec_p_xyx_loop(x, y, z):
    """Electric potential of electrons on a sphere
    do this with a brutal loop that can be numba ified
    """
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
def force_vec(x, y, z):
    """Find the non-radial vector for the force on each electron
    """
    npts = x.size

    forces_x = x*0
    forces_y = x*0
    forces_z = x*0
    for i in range(npts):
        for j in range(i+1, npts):
            d_x = x[i]-x[j]
            d_y = y[i]-y[j]
            d_z = z[i]-z[j]
            dsq = (d_x)**2 + (d_y)**2 + (d_z)**2

            f_x = d_x/dsq
            f_y = d_y/dsq
            f_z = d_z/dsq

            forces_x[i] += f_x
            forces_y[i] += f_y
            forces_z[i] += f_z

            forces_x[j] -= f_x
            forces_y[j] -= f_y
            forces_z[j] -= f_z

    for i in range(npts):
        # magnitude of the force along the radial direction
        f_r = forces_x[i]*x[i] + forces_y[i]*y[i] + forces_z[i]*z[i]
        f_r_sqrt = f_r**0.5
        forces_x[i] = forces_x[i]-f_r_sqrt*x[i]
        forces_y[i] = forces_y[i]-f_r_sqrt*y[i]
        forces_z[i] = forces_z[i]-f_r_sqrt*z[i]

    max_force = np.max(forces_x**2+forces_y**2+forces_z**2)**0.5

    return forces_x/max_force, forces_y/max_force, forces_z/max_force


def new_pot(a, x, y, z, fx, fy, fz):

    x += a*fx
    y += a*fy
    z += a*fz

    new_u = elec_p_xyx_loop(x, y, z)
    return new_u


def find_shift_mag(x, y, z, fx, fy, fz):
    """Given positions and forces, figure out how much to scale the forces to move the points
    """
    npts = x.size
    area = 4*np.pi
    ave_dist = np.sqrt(area/npts)

    fit_result = minimize(new_pot, ave_dist/2., (x, y, z, fx, fy, fz), method='CG',
                          options={'maxiter': 20})
    return fit_result

@jit()
def do_shift(a, x, y, z, fx, fy, fz):
    x += a*fx
    y += a*fy
    z += a*fz

    x, y, z = xyz2sphere(x, y, z)
    return x, y, z

