Looking at my previous attempts to solve Thomson problem and get different tesselation schemes for LSST

Looks like I have things in the sims_featureScheduler repo, and in a Thomson repo.

sims_featureScheduler:  Uses CG minimizer to try and move things around.

Thomson repo:  Experimented with doing my own iteration scheme. Compute the force on each electon, and move it partially towards where it's minimum would be. Note sure if stepsize should increase or decrease with that one honestly

Note, the CG minimizer is the winner, it gets to the lowest energies.