# script to generate a mirisim scene from the planetary nebula SMP LMC 81


import numpy as np
import matplotlib.pyplot as plt
import pdb

from mirisim.skysim import Background, sed, Point, Skycube, ExternalSed
from mirisim.skysim import wrap_pysynphot as wS

from mirisim.config_parser import SimConfig, SimulatorConfig, SceneConfig
from mirisim import MiriSimulation


# this script will create a scene file for the LMC planetary nebula SMP LMC 81, which I'll use as a stand-in target for the NOps 7 DMS testing.
# this observation will use the ALONG SLIT DITHER strategy (which is the default for LRS slit), and a 2-tile mosaic with 10 % overlap in the pointings
# I have generated a custom dither file from the APT pointing output (APT PID 623 Obs 47), using the apt2dither tool in miricoord.
# NGROUPS = 100, NINT = 3, NEXP = 1


# initialise the point source:
pn_sed = ExternalSed(sedfile='LMC_81_Mirisim_spec.txt')

pn = Point(Cen=[0,0])
pn.set_SED(pn_sed)

# now write out to a FITS file
fov = np.array([[-5, 5], [-5,5]])
spat_samp = 0.05

# now we can add a background if requested:
bg = Background(level='low', gradient=5., pa=15.)
scene = pn + bg    


# write some output
print(scene)
    
# now we also want to create the ini file
targetlist = [pn]

## export to ini file -- THIS DOESN'T WORK AS DESCRIBED IN THE JUPYTER NOTEBOOK
scene_config = SceneConfig.makeScene(loglevel=0,
                                    background=bg,
                                    targets = targetlist)
scene_config.write('lrsslit_nops7_scene.ini')

# FIRST SIMULATION: NO DITHERING

sim_config = SimConfig.makeSim(
    name = 'lrsslit_nops7',    # name given to simulation
    scene = 'lrsslit_nops7_scene.ini', # name of scene file to input
    rel_obsdate = 0.5,          # relative observation date (0 = launch, 1 = end of 5 yrs)
    POP = 'IMA',                # Component on which to center (Imager or MRS)
    ConfigPath = 'LRS_SLIT',  # Configure the Optical path (MRS sub-band)
    Dither = True,             # Don't Dither
    StartInd = 1,               # start index for dither pattern [NOT USED HERE]
    NDither = 2,                # number of dither positions [NOT USED HERE]
    DitherPat = 'lrs_recommended_dither.dat', # dither pattern to use [NOT USED HERE]
    disperser = 'SHORT',        # [NOT USED HERE]
    detector = 'SW',            # [NOT USED HERE]
    mrs_mode = 'SLOW',          # [NOT USED HERE]
    mrs_exposures = 10,          # [NOT USED HERE]
    mrs_integrations = 3,       # [NOT USED HERE]
    mrs_frames = 5,             # [NOT USED HERE]
    ima_exposures = 1,          # number of exposures
    ima_integrations = 3,       # number of integrations
    ima_frames = 100,             # number of groups (for MIRI, # Groups = # Frames)
    ima_mode = 'FAST',          # Imager read mode (default is FAST ~ 2.3 s)
    filter = 'P750L',          # Imager Filter to use
    readDetect = 'FULL'         # Portion of detector to read out
)


sim_config.write('lrsslit_nops7_sim.ini')
simulator_config = SimulatorConfig.from_default()

sim = MiriSimulation(sim_config, scene_config, simulator_config)
sim.run()


