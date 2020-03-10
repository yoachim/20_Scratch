import argparse
import numpy as np
from thomson import sphere_iterator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--npoints", type=int, default=10)
    parser.add_argument("--maxiter", type=int, default=300)

    args = parser.parse_args()
    npoints = args.npoints
    maxiter = args.maxiter

    result = sphere_iterator(npoints, maxiter=maxiter)
    np.savez('thomson_%i_ni%i.npz' % (npoints, maxiter), result=result)


## timing:  
#  npts    niter    time
#  100      258       42s
#  150      470       3m44s
#  200      328       5m18