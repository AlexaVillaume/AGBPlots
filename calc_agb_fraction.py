'''
Attempting to estimate how many dust enshrouded AGB stars we should expect in galaxy
'''
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import FSPSFiles as fsps
import phot_utils

# Take definite integral of  km^-2.35
def salpeter(m_min, m_max):
    # In the IMF k is local stellar density but because
    # taking the fraction this can be arbitray and can
    # also be for age, metallcity, etc...
    k = 0.004
    low = (m_min**-1.35)
    high = (m_max**-1.35)
    return (k/1.35)*(low - high)

path = '/Users/alexawork/fsps/OUTPUTS/'
models = fsps.readmags(path + 'SMC_SSP.out.cmd')
models = map(lambda model: model, models)

# Get mass_min and mass_max for all the stars for a given age
all_stars = []
for model in models:
    if model['age'] == 8.9:
        all_stars.append(model)
mass = map(lambda star: star['mass'], all_stars)
mass_min_all = min(mass)
mass_max_all = max(mass)
print 'Max Mass (all): ', mass_max_all, 'Min Mass (all): ', mass_min_all

# Get stars of AGB['phase'] and appropriate age
smc1 = []
for model in models:
    if model['age'] == 8.9:
        if model['phase'] == 5.0:
            smc1.append(model)

# Make color-magnitude cut
smc2 = []
for star in smc1:
    # Stars in the redward spur
    if star['irac1'] - star['irac4'] > -1.5 and star['irac4'] < -4:
        smc2.append(star)

" Make luminosity function "
imf = map(lambda star: 10**star['log(weight)'], smc1)
logl = map(lambda star: 10**star['logl'], smc1)
cul_lum = []
# Make it cumulative
for value in logl:
    tmp = []
    for j, val in enumerate(logl):
        if val >= value:
        # Select imf values that correspond to app. logl values
            tmp.append(imf[j])
    cul_lum.append(sum(tmp))

cul_lum = map(lambda star: math.log10(star), cul_lum)
logl = map(lambda star: math.log10(star), logl)

plt.plot(logl, cul_lum, linestyle='-', color='#424242', linewidth=3,
         label = 'Z = 0.004, log(age) = 8.9')
plt.title('phase = 5')
plt.ylabel('log $N(>L)/N_{tot}$', fontsize=16)
plt.xlabel(r'log $L_{bol}$', fontsize=20, labelpad=20)

plt.legend(frameon=False)
plt.show()

# Make tau cut
tau = map(lambda star: star['tau'], smc2)
med_tau = phot_utils.calc_median(tau)
print "Tau before tau-cut: ", med_tau
smc3 = filter(lambda star: star['tau'] > med_tau*5, smc2)
tau = map(lambda star: star['tau'], smc3)
print "Tau after tau-cut: ", phot_utils.calc_median(tau)


mass = map(lambda star: star['mass'], smc3)
mass_min_agb = min(mass)
mass_max_agb = max(mass)
print 'Max Mass (agb): ', mass_max_agb, 'Min Mass (agb): ', mass_min_agb

print salpeter(mass_min_agb, mass_max_agb), salpeter(mass_min_all, mass_max_all)
print salpeter(mass_min_agb, mass_max_agb)/salpeter(mass_min_all, mass_max_all)
