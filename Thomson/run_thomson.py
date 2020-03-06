import argparse
import numpy as np
from lsst.sims.featureScheduler.thomson import even_points_xyz

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--npoints", type=int, default=10)
    parser.add_argument("--maxiter", type=int, default=300)

    args = parser.parse_args()
    npoints = args.npoints
    maxiter = args.maxiter

    result = even_points_xyz(npoints, maxiter=maxiter)
    np.savez('thomson_%i.npz' % npoints, result=result)
