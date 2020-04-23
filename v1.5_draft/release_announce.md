FBS runs 1.5

This release includes 86 simulation databases. Most of the experiments from v1.4 have been replicated. Let us know if there is anything missing you would like updated.

The major change in this release is that we use a new algorithm when selecting large areas to observe. Before, we simply sorted pointings by reward function. In v1.5, we demand the area be contiguous. This helps keep the slewtime down, increases the amount of sky that has rapid revisits, and does not seem to impact the overall survey uniformity.

Here are images of the Alt-Az distribution on a single night from version 1.4 and 1.5. The 1.5 pointings do a better job of staying contiguous, resulting in 1.5 having 947 visits in the night while 1.4 only had 909 visits.

![](thumb.baseline_v1_4_N_visits_alt_az_night2007_HEAL_SkyMap.png) 
![](thumb.baseline_v1_5_N_visits_alt_az_night2007_HEAL_SkyMap.png)


Additional changes include:

* Eliminating excess filter changes in DDF sequences
* The u filter remains mounted (and z unmounted) for longer, until the moon is 40% illuminated
* u-band observations are paired with either g or r observations
* We have removed the DDF 290 and replaced it with a pair of Euclid DDF pointings
* Improved 5-sigma depth calculations for when visits have 2 snaps

The default deep drilling fields now execute visit sequences of ux8, gx20, rx10, ix20, zx26, and yx20 with whatever filters are mounted (so sequences will not include u or z depending on the moon phase).  The DDFs comprise \~5% of the total visits. We are still actively exploring the best way to optimize the DDF sequences, and welcome any additional DDF sequence ideas or metrics for measuring the effectiveness of the DDFs. 


Git repo with more notes on the individual runs: https://github.com/lsst-sims/sims_featureScheduler_runs1.5

The databases are available from NCSA at: https://lsst-web.ncsa.illinois.edu/sim-data/sims_featureScheduler_runs1.5/

MAF output will be available at:  http://astro-lsst-01.astro.washington.edu:8083

New experiments in this release:

## dcr

These runs intentionally take some observations at high airmass every year so DCR can be measured and corrected for in difference imaging. In theory, one can also measure the astrometric shift caused by DCR for objects with sharp breaks in their SEDs (e.g., AGN with large emission lines).

## filter_dist

These runs vary the filter distribution in the WFD area. Our baseline filter distribution is nominally set to optimize photo-z measurements, but it would be nice to quantify how well photo-z and other transients perform with different filter distributions.

## greedy_footprint

Here we avoid observing the ecliptic in twilight time, thereby ensuring nearly all ecliptic observations are taken in pairs. 


