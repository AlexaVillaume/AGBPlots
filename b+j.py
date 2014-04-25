'''
Recreate Barmby+Jalilian Figures 6 + 7
'''
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
import FSPSFiles as fsps
import phot_utils

# Read data from Barmby and Jalilian 2012

barmby = Table.read('barmby2012.txt', format='ascii.commented_header')

metallicity = barmby['met']
e_bv = barmby['ebv']
irac1 = barmby['3.6']
irac1_err = barmby['err1']
irac2 = barmby['4.5']
irac2_err = barmby['err2']
irac3 = barmby['5.8']
irac3_err = barmby['err3']
irac4 = barmby['8.0']
irac4_err = barmby['err4']
twomk = barmby['ks']
twomk_err = barmby['err5']
lirac1 = barmby['3.6l']
lirac1_err = barmby['err6']
lirac2 = barmby['4.5l']
lirac2_err = barmby['err7']

# Convert metallicity to total metallicty
totmet = map(lambda value: value + 0.94*0.2, metallicity)

# Compute extinction corrections for each band
aks = map(lambda value: 0.35*value, e_bv)
a36 = map(lambda value: 0.56*value, aks)
amu = map(lambda value: 0.43*value, aks)

# And then correct the photometry by those values
twomk = twomk - aks
irac1 = irac1 - a36
lirac1 = lirac1 - a36
irac2 = irac2 - amu
lirac2 = lirac2 - amu
irac3 = irac3 - amu
irac4 = irac4 - amu

# Read in FSPS models
with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z03_agb', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z03_agb = map(lambda line: fsps.readmags(line), tmp)
with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z13_agb', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z13_agb = map(lambda line: fsps.readmags(line), tmp)
with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z17_agb', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z17_agb = map(lambda line: fsps.readmags(line), tmp)
with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z20_agb', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z20_agb = map(lambda line: fsps.readmags(line), tmp)
with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z22_agb', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z22_agb = map(lambda line: fsps.readmags(line), tmp)

with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z03_nod', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z03_nod = map(lambda line: fsps.readmags(line), tmp)
with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z13_nod', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z13_nod = map(lambda line: fsps.readmags(line), tmp)
with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z17_nod', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z17_nod = map(lambda line: fsps.readmags(line), tmp)
with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z20_nod', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z20_nod = map(lambda line: fsps.readmags(line), tmp)
with open('/Users/alexawork/fsps/OUTPUTS/Barmby+Jalilian/SSP.out.mags_z22_nod', 'r') as model:
    tmp = filter(lambda line: phot_utils.noHead(line), model)
    z22_nod = map(lambda line: fsps.readmags(line), tmp)

# Select by age
agb_models = [z03_agb, z13_agb, z17_agb, z20_agb, z22_agb]
nod_models = [z03_nod, z13_nod, z17_nod, z20_nod, z22_nod]

irac1_agb_2gyr = np.array([])
irac2_agb_2gyr = np.array([])
irac3_agb_2gyr = np.array([])
irac4_agb_2gyr = np.array([])
twomk_agb_2gyr = np.array([])
vmag_agb_2gyr = np.array([])

irac1_agb_8gyr = np.array([])
irac2_agb_8gyr = np.array([])
irac3_agb_8gyr = np.array([])
irac4_agb_8gyr = np.array([])
twomk_agb_8gyr = np.array([])
vmag_agb_8gyr = np.array([])
for model in agb_models:
    for tmp in model:
        if tmp.agegyr > 1.9 and tmp.agegyr < 2.1:
            irac1_agb_2gyr = np.append(irac1_agb_2gyr, tmp.IRAC1)
            irac2_agb_2gyr = np.append(irac2_agb_2gyr, tmp.IRAC2)
            irac3_agb_2gyr = np.append(irac3_agb_2gyr, tmp.IRAC3)
            irac4_agb_2gyr = np.append(irac4_agb_2gyr, tmp.IRAC4)
            twomk_agb_2gyr = np.append(twomk_agb_2gyr, tmp.TWOMASS_K)
            vmag_agb_2gyr = np.append(vmag_agb_2gyr, tmp.V)
        if tmp.agegyr > 7.9 and tmp.agegyr < 8.1:
            irac1_agb_8gyr = np.append(irac1_agb_8gyr, tmp.IRAC1)
            irac2_agb_8gyr = np.append(irac2_agb_8gyr, tmp.IRAC2)
            irac3_agb_8gyr = np.append(irac3_agb_8gyr, tmp.IRAC3)
            irac4_agb_8gyr = np.append(irac4_agb_8gyr, tmp.IRAC4)
            twomk_agb_8gyr = np.append(twomk_agb_8gyr, tmp.TWOMASS_K)
            vmag_agb_8gyr = np.append(vmag_agb_8gyr, tmp.V)

irac1_nod_2gyr = np.array([])
irac2_nod_2gyr = np.array([])
irac3_nod_2gyr = np.array([])
irac4_nod_2gyr = np.array([])
twomk_nod_2gyr = np.array([])
vmag_nod_2gyr = np.array([])

irac1_nod_8gyr = np.array([])
irac2_nod_8gyr = np.array([])
irac3_nod_8gyr = np.array([])
irac4_nod_8gyr = np.array([])
twomk_nod_8gyr = np.array([])
vmag_nod_8gyr = np.array([])
for model in nod_models:
    for tmp in model:
        if tmp.agegyr > 1.9 and tmp.agegyr < 2.1:
            irac1_nod_2gyr = np.append(irac1_nod_2gyr, tmp.IRAC1)
            irac2_nod_2gyr = np.append(irac2_nod_2gyr, tmp.IRAC2)
            irac3_nod_2gyr = np.append(irac3_nod_2gyr, tmp.IRAC3)
            irac4_nod_2gyr = np.append(irac4_nod_2gyr, tmp.IRAC4)
            twomk_nod_2gyr = np.append(twomk_nod_2gyr, tmp.TWOMASS_K)
            vmag_nod_2gyr = np.append(vmag_nod_2gyr, tmp.V)
        if tmp.agegyr > 7.9 and tmp.agegyr < 8.1:
            irac1_nod_8gyr = np.append(irac1_nod_8gyr, tmp.IRAC1)
            irac2_nod_8gyr = np.append(irac2_nod_8gyr, tmp.IRAC2)
            irac3_nod_8gyr = np.append(irac3_nod_8gyr, tmp.IRAC3)
            irac4_nod_8gyr = np.append(irac4_nod_8gyr, tmp.IRAC4)
            twomk_nod_8gyr = np.append(twomk_nod_8gyr, tmp.TWOMASS_K)
            vmag_nod_8gyr = np.append(vmag_nod_8gyr, tmp.V)

metallicity = [-1.68, -0.69, -0.30, +0.00, +0.20]
# The NIR and MIR colors
xlabel = ['', -1.5, -1.0, -0.5, 0.0, '']

ax2 = plt.subplot(2, 3, 2)
ax2.errorbar(totmet, twomk - lirac1, yerr=lirac1_err + twomk_err,
             linestyle='none', marker='o', color='#424242')
ax2.plot(metallicity, twomk_nod_8gyr - irac1_nod_8gyr, linestyle='-',
         linewidth=2, color='#0066ff')
ax2.plot(metallicity, twomk_agb_8gyr - irac1_agb_8gyr, linestyle='-',
         linewidth=2, color='#ff536d')
ax2.plot(metallicity, twomk_nod_2gyr - irac1_nod_2gyr, linestyle='--',
         linewidth=2, color='#0066ff')
ax2.plot(metallicity, twomk_agb_2gyr - irac1_agb_2gyr, linestyle='--',
         linewidth=2, color='#ff536d')
plt.xlim(-2.0, 0.5)
plt.ylim(-0.4, 0.7)
plt.ylabel('Ks - [3.6]', fontsize=16)
ax2.set_xticklabels(xlabel, minor=False)

ax3 = plt.subplot(2, 3, 3)
ax3.errorbar(totmet, irac1 - irac2, yerr=irac1_err + irac4_err,
             linestyle='none', marker='o',  color='#424242')
ax3.plot(metallicity, irac1_nod_8gyr - irac2_nod_8gyr, linestyle='-',
         linewidth=2, color='#0066ff')
ax3.plot(metallicity, irac1_agb_8gyr - irac2_agb_8gyr, linestyle='-',
         linewidth=2, color='#ff536d')
ax3.plot(metallicity, irac1_nod_2gyr - irac2_nod_2gyr, linestyle='--',
         linewidth=2, color='#0066ff')
ax3.plot(metallicity, irac1_agb_2gyr - irac2_agb_2gyr, linestyle='--',
         linewidth=2, color='#ff536d')
plt.xlim(-2.0, 0.5)
plt.ylim(-0.2, 0.3)
plt.ylabel('[3.6] - [4.5]', fontsize=16)
ax3.set_xticklabels(xlabel, minor=False)

ax5 = plt.subplot(2, 3, 5)
ax5.errorbar(totmet, irac2 - irac3, yerr=irac2_err + irac3_err,
             linestyle='none', marker='o', color='#424242')
ax5.plot(metallicity, irac2_nod_8gyr - irac3_nod_8gyr, linestyle='-',
         linewidth=2, color='#0066ff')
ax5.plot(metallicity, irac2_agb_8gyr - irac3_agb_8gyr, linestyle='-',
         linewidth=2, color='#ff536d')
ax5.plot(metallicity, irac2_nod_2gyr - irac3_nod_2gyr, linestyle='--',
         linewidth=2, color='#0066ff')
ax5.plot(metallicity, irac2_agb_2gyr - irac3_agb_2gyr, linestyle='--',
         linewidth=2, color='#ff536d')
plt.xlim(-2.0, 0.5)
plt.ylim(-0.1, 0.5)
plt.xlabel('Metallicity [M/H]', fontsize=16)
plt.ylabel('[4.5] - [5.8]', fontsize=16)
ax5.set_xticklabels(xlabel, minor=False)

ax6 = plt.subplot(2, 3, 6)
ax6.errorbar(totmet, irac3 - irac4, yerr=irac3_err + irac4_err,
             linestyle='none', marker='o', color='#424242')
ax6.plot(metallicity, irac3_nod_8gyr - irac4_nod_8gyr, linestyle='-',
         linewidth=2, color='#0066ff')
ax6.plot(metallicity, irac3_agb_8gyr - irac4_agb_8gyr, linestyle='-',
         linewidth=2, color='#ff536d')
ax6.plot(metallicity, irac3_nod_2gyr - irac4_nod_2gyr, linestyle='--',
         linewidth=2, color='#0066ff')
ax6.plot(metallicity, irac3_agb_2gyr - irac4_agb_2gyr, linestyle='--',
         linewidth=2, color='#ff536d')
plt.xlim(-2.0, 0.5)
plt.ylim(-0.2, 0.6)
plt.ylabel('[5.8] - [8.0]', fontsize=16)
ax6.set_xticklabels(xlabel, minor=False)

# The optical and NIR colors
matched = Table.read('matched_catalog.txt', format='ascii.commented_header')
totmet = map(lambda value: value + 0.94*0.2, matched['met'])

aks = map(lambda value: 0.35*value, matched['eb_v'])
a36 = map(lambda value: 0.56*value, aks)
amu = map(lambda value: 0.43*value, aks)
av  = map(lambda value: 3.10*value, matched['eb_v'])

vmag = matched['vmag'] - av
irac1 = matched['irac1'] - a36
irac2 = matched['irac2'] - amu

ax1 = plt.subplot(2, 3, 1)
ax1.errorbar(totmet, vmag - irac1, yerr=matched['err2'] + matched['err4'],
             linestyle='none', marker='o', color='#424242')
ax1.plot(metallicity, vmag_nod_8gyr - irac1_nod_8gyr, linestyle='-',
         linewidth=2, color='#0066ff')
ax1.plot(metallicity, vmag_agb_8gyr - irac1_agb_8gyr, linestyle='-',
         linewidth=2, color='#ff536d')
ax1.plot(metallicity, vmag_nod_2gyr - irac1_nod_2gyr, linestyle='--',
         linewidth=2, color='#0066ff')
ax1.plot(metallicity, vmag_agb_2gyr - irac1_agb_2gyr, linestyle='--',
         linewidth=2, color='#ff536d')
plt.xlim(-2.0, 0.5)
plt.ylim(1.0,  4.0)
plt.ylabel('V - [3.6]', fontsize=16)
ax1.set_xticklabels(xlabel, minor=False)

ax4 = plt.subplot(2, 3, 4)
ax4.errorbar(totmet, vmag - irac2, yerr=matched['err3'] + matched['err4'],
             linestyle='none', marker='o', color='#424242')
ax4.plot(metallicity, vmag_nod_8gyr - irac2_nod_8gyr, linestyle='-',
         linewidth=2, color='#0066ff')
ax4.plot(metallicity, vmag_agb_8gyr - irac2_agb_8gyr, linestyle='-',
         linewidth=2, color='#ff536d')
ax4.plot(metallicity, vmag_nod_2gyr - irac2_nod_2gyr, linestyle='--',
         linewidth=2, color='#0066ff')
ax4.plot(metallicity, vmag_agb_2gyr - irac2_agb_2gyr, linestyle='--',
         linewidth=2, color='#ff536d')
plt.xlim(-2.0, 0.5)
plt.ylim(1.0,  4.0)
plt.ylabel('V - [4.5]', fontsize=16)
ax4.set_xticklabels(xlabel, minor=False)

plt.tight_layout()
plt.show()
