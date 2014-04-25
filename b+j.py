'''
Recreate Barmby+Jalilian Figures 6 + 7
'''
import matplotlib.pyplot as plt

from astropy.table import Table

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

# The NIR and MIR colors
ax2 = plt.subplot(2, 3, 2)
ax2.errorbar(totmet, twomk - lirac1, yerr=lirac1_err + twomk_err,
             linestyle='none', marker='o', color='#424242')
plt.xlim(-2.0, 0.5)
plt.ylim(-0.4, 0.7)
plt.ylabel('Ks - [3.6]', fontsize=16)

ax3 = plt.subplot(2, 3, 3)
ax3.errorbar(totmet, irac1 - irac2, yerr=irac1_err + irac4_err,
             linestyle='none', marker='o',  color='#424242')
plt.xlim(-2.0, 0.5)
plt.ylim(-0.2, 0.3)
plt.ylabel('[3.6] - [4.5]', fontsize=16)

ax5 = plt.subplot(2, 3, 5)
ax5.errorbar(totmet, irac2 - irac3, yerr=irac2_err + irac3_err,
             linestyle='none', marker='o', color='#424242')
plt.xlim(-2.0, 0.5)
plt.ylim(-0.1, 0.5)
plt.xlabel('Metallicity [M/H]', fontsize=16)
plt.ylabel('[4.5] - [5.8]', fontsize=16)

ax6 = plt.subplot(2, 3, 6)
ax6.errorbar(totmet, irac3 - irac4, yerr=irac3_err + irac4_err,
             linestyle='none', marker='o', color='#424242')
plt.xlim(-2.0, 0.5)
plt.ylim(-0.2, 0.6)
plt.ylabel('[5.8] - [8.0]', fontsize=16)

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
plt.xlim(-2.0, 0.5)
plt.ylim(1.0,  4.0)
plt.ylabel('V - [3.6]', fontsize=16)

ax4 = plt.subplot(2, 3, 4)
ax4.errorbar(totmet, vmag - irac2, yerr=matched['err3'] + matched['err4'],
             linestyle='none', marker='o', color='#424242')
plt.xlim(-2.0, 0.5)
plt.ylim(1.0,  4.0)
plt.ylabel('V - [4.5]', fontsize=16)

plt.tight_layout()
plt.show()
