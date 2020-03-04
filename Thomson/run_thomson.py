import argparse
import numpy as np
from lsst.sims.featureScheduler.thomson import even_points

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--npoints", type=int, default=10)

    args = parser.parse_args()
    npoints = args.npoints

    result = even_points(npoints)
    np.savez('thomson_%i.npz' % npoints)
