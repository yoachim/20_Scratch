Run the profiler on the old and new kinematic model to see where the slowdown is coming from


profile command:
python -m cProfile -o profiler_out -s time baseline.py


new code:
Skipped 0 observations
Flushed 0 observations from queue for being stale
Completed 12253 observations
ran in 5 min = 0.1 hours

old code:
Flushed 0 observations from queue for being stale
Completed 12397 observations
ran in 3 min = 0.1 hours
Writing results to  baseline_nexp1_v1.6_0yrs.db