'''
Fit NGC 1404 data from athey et al. 2002
Used solar metallicity for both FSPS models
http://iopscience.iop.org/0004-637X/571/1/272/fulltext/
'''
import matplotlib.pyplot as plt

import FSPSFiles as fsps

# Microns
wave = [6.044, 6.221, 6.396, 6.569, 6.741, 6.911, 7.080, 7.248, 7.414, 7.578,
        7.741, 7.903, 8.063, 8.222, 8.379, 8.535, 8.689, 8.842, 8.993, 9.291,
        9.660, 9.986, 10.31, 10.63, 10.05, 11.27, 11.58, 11.89, 12.21, 12.51,
        12.82, 13.12, 13.42, 13.73, 14.02]

# mJy
flux = [84.98, 80.57, 85.49, 80.29, 72.94, 70.24, 66.57, 69.21, 63.61, 62.84,
        55.83, 54.72, 62.78, 56.73, 50.94, 52.31, 46.61, 46.93, 52.09, 49.26,
        50.64, 50.78, 47.27, 42.06, 36.08, 37.41, 30.16, 27.54, 21.11, 20.76,
        31.47, 32.15, 26.96, 26.07, 29.46]

erro = [2.90, 2.94, 2.78, 2.96, 2.85, 3.14, 3.74, 2.59, 3.80, 3.35, 2.88, 2.91,
        3.25, 3.13, 2.45, 2.97, 2.84, 3.22, 3.38, 3.77, 4.44, 3.10, 3.56, 3.96,
        4.83, 4.39, 4.30, 4.24, 4.61, 3.88, 4.49, 4.32, 5.04, 4.97, 4.50]

nod = fsps.readspec("/Users/alexawork/fsps/OUTPUTS/athey_nod_SSP.spec")
for model in nod:
    if model.agegyr > 8.8 and model.agegyr < 9.1:
        nod_age9 = map(lambda value: value*0.6*1e18, model.flux)
        swave = model.wave

agb = fsps.readspec("/Users/alexawork/fsps/OUTPUTS/athey_agb_SSP.spec")
for model in agb:
    if model.agegyr > 8.8 and model.agegyr < 9.1:
        agb_age9 = map(lambda value: value*0.6*1e18, model.flux)

plt.errorbar(wave, flux, yerr=erro, linestyle='none', marker='o', color='#424242')
plt.plot(swave, nod_age9, linestyle='-', linewidth=2, color='#0066ff',
         label='No AGB Dust')
plt.plot(swave, agb_age9, linestyle='-', linewidth=2, color='#ff536d',
         label='With AGB Dust')
plt.xlim(5,14)
plt.ylim(15,100)
plt.xlabel('Wavelength ($\mu m$)', fontsize=16)
plt.ylabel('Flux (mJy)', fontsize=16)
plt.legend(frameon=False)

plt.show()
