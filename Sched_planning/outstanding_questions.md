# Outstanding Questions for LSST Cadence simulations

With the release of [75 new survey simulations in v1.4](https://community.lsst.org/t/january-2020-update-fbs-1-4-runs/4006), we are now ready to start combining strategies to construct the first version of the LSST scheduler.

## Which deep drilling strategy should we employ?

We have several DDF strategies (baseline, DESC, AGN, Euclid). There are also proposals to ephasize a DDF in a single year, and de-emphasize other years.  What DDF observing strategy should be included in our simulations?

Should DDFs be taken preferentially in dark time?

## What's the best dithering strategy for the DDFs (both spatially and rotationally)?

There is tension in that DM generally prefers larger dithers for calibration and co-addition purposes, while science cases prefer smaller dithers to preserve the area that reaches the deepest levels.

Some fields are near bright stars, so need to not dither too close.

Euclid fields will need to be dithered along vector beween them I guess.

## Should we experiment with different tessellations?

We could try packing or expanding the current tessellation, trading area covered per night with area that gets more revisits in a night.


## What is the best camera rotational dithering strategy?

In the baseline, we set the camera rotator to a random position between -80 and 80 degrees (relative to the telescope) each night. We also test constraining the camera to be +/- 45 degrees to make diffraction spikes fall along CCD rows and columns.  

## What should the final survey footprint be?

We have run a large number of potential survey footprints.

Relevant sub-questions:  

* How the total number of visits should be distributed between filters? Presumably there is a strong photo-z preference here?
* Should we use dust extinction maps to define regions? 
* Should we de-emphasize the (dusty) galactic anti-center?
* Should we include some minimal coverage of the entire accesable sky for ToO potential? Maybe in only a few filters?
* How much contingency should we have on the WFD region? The SRD states we should reach 825 visits, how far over this value should our simulations end up?

## Do we need to use a rolling cadence?

Rolling cadence makes it possible to better sample light curves of transient and variable objects in alternating years. 

Should rolling be WFD, or other regions of the sky as well?

## Should we use variable exposure times?

We can vary the exposure times based on the observing conditions to help keep individual exposures to similar depths.

## Should visits be 1x30s or 2x15s?

This probably has to wait until we have on-sky data. But it represent a fairly large loss of the total available time (7%) if we need to take two snaps per visit.

## Should we intentionally take observations at high airmass to measure DCR

For the bluer filters, DCR can make image template construction complicated. There is also potential to do science via measuring the DCR amplitude of certain objects (AGN, etc).

## What is the best strategy for taking observations in pairs?

We typically try to take pairs seperated by 22 minutes, and in different filters. It would be nice to know which colors are most useful.

## Should we use some of twilight time for a NEO survey?

## What should our general twilight strategy be? 

Right now, we are mostly using it to fill out visits to ensure we get to the SRD values in the WFD in redder filters. We're using a greedy algorithm that isn't that impressive.  We could go to shorter exposures, or try to get third observations of things that have already been observed.

## Should we include a short exposure time survey as well as the standard 30s visits?

We tested mixing in observations of 5s and 1s in addition to the usual survey.

## What's the best way to observe the LMC and SMC?

We have simulations where we include them as part of the WFD area, but we could also treat them as DDFs for more specific cadence

## Should we prioritize collecting "good seeing" images across the entire sky? In which filters?

We do not take much account of the atmospheric seeing. 
Other surveys have often preferentially observed certain filters in "good seeing" conditions.  

## Should we adjust the survey footprint slightly to account for over/under subscription?

Right now, we tend to use straight cuts in declination to define the survey area (easy to code and calculate areas covered). However, because of variable night length, weather downtime, and the placement of DDFs we have some regions of the sky that are oversubscribed and some (like the galactic plane) are undersubscribed. We could alter the limits of the WFD area to constrict in parts of the sky that are over-subscribed and flare where it is undersubscribed. This should result in a slightly more uniform WFD depth. 

## Do periodic sources suffer from aliasing?

The Bell et al white paper discussed scheduling to prevent aliasing of periodic sources. This is potentially a memory intensive problem to simulate. It would be good to see if there is a population of periodic sources that are currently suffering from aliasing and would drive a need to shift the timing of our observations?  Is there new science enabled by trying to avoid the current level of aliasing in LSST?

Related to this question, is what is the minimum timescale of variation should LSST strive to measure? The Bell et al white paper looks at aliasing at the 2-hour level. Should we strive to eliminate aliasing at that level, or should we say LSST will discover variables, and other telecopes are better suited to studying short time variability?

## Do we need to do anything more for image differencing templates?

Either for making sure we have enough templates early enough, or for DCR coverage.

## When/how should we optimize the basis function weights?

We can refine the behavior of the scheduler by varying the weights on the basis functions, namely the 5$\sigma$ depth, footprint, slewtime, filter, and template weights. Can we put together a combination of science metrics to judge the best combination in this 5D parameter space?


## Should we switch u-band to 60s visits?

u-band can be read noise dominated, so we should probably switch to 60s (or 2x30s) visits.  Does a 60s u-band observation count as 2 visits for SRD requirement purposes?

## How long do we leave the u filter loaded?

We currently swap the u and z filters, leaving the u only loaded around new moon. 

## What should the plan be for ToO LIGO events?

Should we extend all the way to the north so that we have image templates for events that happen outside our usual footprint?

Should we only follow up ToO events that fall in the WFD area?

What should the search strategy be for ToOs? What filters, what dithering strategy to fill chip/raft gaps? 

Is the strategy that Rubin makes a detection, then leaves further followup to other telescopes? Some ToO white papers seem to advocate ToO followup over multiple days.

