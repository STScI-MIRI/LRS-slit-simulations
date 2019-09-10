# LRS-slit-simulations
Simulated data for LRS slit

### Contents of this repository
This repository will be used to collect scripts to generate simulated data with MIRISim for LRS slit observations with MIRI. These data can be used for DMS or pipeline testing purposes. The following cases will be covered:

* LRS slit observations, point source, using the 2-point along-slit dither
* LRS slit observations, point source, no dithering (target at the slit centre)

Simulations will be grouped in dedicated folders:

* LRS-slit-dither
* LRS-slit-nodither

The scope of each of these simulations is described further in the README in each folder. The output format of MIRISim data is compatible with the JWST calibration pipeline.

### Dependencies
The following packages are called in these scripts:

numpy
os
glob
importlib
The simulations are designed to be run using MIRISim, the publicly available data simulator developed by the MIRI European Consortium. Instructions for installation and use can be found on this page. Bugs can be reported to mirisim AT roe.ac.uk.

MIRISim is therefore also called extensively in the scripts and notebooks.

### Authors
Sarah Kendrew, sarah.kendrew AT esa.int
