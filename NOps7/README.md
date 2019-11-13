# LRS Slit simulations for Normal Ops 7 testing


### Contents of this folder

This folder contains materials used for LRS slit simulations specifically for the Normal Ops 7 run, to be executed (probably) in December 2019. The osbervation simulated is captured in APT PID 623, Observation number 47. As target we are using the LMC-81 planetary nebula - to keep things simple. The contents of the folder are as follows:

* 623_nops7.pointing: the pointing file exported from APT, only for Observation 47
* lrsslit\_nops7\_pointings.dat: the pointing file, converted into a dither pattern file that MIRISim can use (using the APT2dither script, which I don't include here)
* lrsslit\_nops7\_sim.py: a script that generates the scene, configures and runs the simulation.
* LMC\_81\_Mirisim\_spec.txt: the Spitzer spectrum file used to generate the scene

### Instructions for using the custom dither pattern file

To run the simulation with the custom pattern of pointings (this will simulate an Along Slit Nod pattern for 2 mosaic tiles, with 10% overlap), do the following:

* search your hard drive for the file "lrs\_recommended\_dither.dat"; note the directory. This will be something like: $HOME/anaconda3/envs/mirisim/...../obssim/data/ - depending on your local setup.
* copy file lrsslit\_nops7\_pointings.dat to this directory
* rename the existing file lrs\_recommended\_dither.dat to something else (don't overwrite or delete it!)
* rename the new pointings file lrs\_recommended\_dither.dat

You should then be able to return to the simulation folder, and run the script:
`python lrsslit_nops7_sim.py`


### Dependencies
The following packages are called in these scripts:

numpy
matplotlib
The simulations are designed to be run using MIRISim, the publicly available data simulator developed by the MIRI European Consortium. Instructions for installation and use can be found on this page. Bugs can be reported to mirisim AT roe.ac.uk.

MIRISim is therefore also called extensively in the scripts and notebooks.

### Authors
Sarah Kendrew, sarah.kendrew AT esa.int
