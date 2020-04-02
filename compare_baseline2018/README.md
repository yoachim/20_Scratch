Making plots to compare the baseline2018 and new v1.5 2-snap baseline

* Spatial dithering
* camera rotational dithering
* u-band DDF no longer at high airmass
* galactic plane no longer at high airmass
* no more u and g in twilight
* Using a TSP solver and avoiding zenith, we reduce the median slewtime
* DDFs are dithered
* we drop DD:290 and add the Eucid deep fields

* Weather downtime that better matches downtime of Gemini and SOAR
* Pairs in different filters, so transients have color information

* taking pairs in the GP and SCP. This is mostly for scheduling convienence (makes it easy to seamlessly move from WFD to other areas)

the u-band 5-sigma depths seem to be very strange, like 0.5 mag different than current calculations. There are some observations with sunAlt listed as > 0 (that might be my old bug).

wow, there is some wacky stuff going on with the filter distribution

