import numpy as np
import matplotlib.pyplot as plt
import astropy.io.ascii as ascii
import astropy.io.fits as fits
import astropy.units as u
from astropy.modeling import models, fitting
from astropy.table import Table, Column

plt.close('all')

data_dir = '/Users/kendrew/miri/commissioning/CARs/MIRI-076/PNe_magellanic_clouds_data/'

# spectrum file for SMP LMC 81
f = 'SMP_LMC_81_SPITZER_S5_14704896_01_merge.tbl'
T_dust = 130. * u.Kelvin
F_ir = 10**(-10.6) * (u.erg / u.cm / u.cm / u.s)

# read in the spectrum
sp = ascii.read(data_dir + f)
#change the unit on the wavelength axis to work with astropy
sp['wavelength'].unit = u.micron

# plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=[12,6])
ax1.plot(sp['wavelength'], sp['flux_density'], label='Spitzer merged spectrum')
ax1.set_xlabel('wavelength (micron)')
ax1.set_ylabel('flux (Jy)')


# now fit the continuum
bb = models.BlackBody1D(temperature=T_dust, bolometric_flux=F_ir)
ax1.plot(sp['wavelength'], bb(sp['wavelength']).to(u.Jy), 'r-', label='best fit BB (T = 130 K)')
ax1.set_title('SMP LMC 81')
ax1.legend(loc=2)


# subtract best-fit BB from spectrum
sp_sub = sp['flux_density'] - bb(sp['wavelength']).to(u.Jy)
ax2.plot(sp['wavelength'], sp_sub, label='spectrum, continuum subtracted')
ax2.set_xlabel('wavelength (micron)')
ax2.set_ylabel('flux (Jy)')
#ax2.set_xlim((5., 15.))
ax2.legend(loc=2)
fig.show()


# OK this all looks good. I just need to reformat the file so Mirisim can read it: 2 columns, wavelength in microns and flux density in microJy
wavepick = sp['wavelength'] <= 14.
wave = sp['wavelength'][wavepick].data
wavecol = Column(wave)

spec = sp['flux_density'][wavepick].data * 1e6
speccol = Column(spec)

spectab = Table([wave, spec])
#ascii.write(spectab, 'LMC_81_Mirisim_spec.txt')

spec_etc = sp['flux_density'].data * 1e3
wave_etc = sp['wavelength'].data
speccol = Column(spec_etc)

spectab_etc = Table([wave_etc, spec_etc])
ascii.write(spectab_etc, 'LMC_81_ETC_spec.txt')



