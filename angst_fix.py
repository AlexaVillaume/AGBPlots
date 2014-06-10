'''
Working with Ben's models...
'''
import math
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
import phot_utils

fig = plt.figure(figsize=(10, 8))

# Taken from Berg et al. 2012
def calc_met(mag):
    return 6.10  -.1*mag - 12

def rm_nan(data):
    index = []
    for i, value in enumerate(data):
        if math.isnan(value):
            index.append(i)
    return index

def calc_ratio(data1, data2):
    ratio = []
    for i in range(len(data1)):
        ratio.append(data1[i]-data2[i])
    return ratio

angst = Table.read('johnson_all.txt', format='ascii.commented_header')

m1_nans = rm_nan(angst['mag_obs_m1'])
i4_nans = rm_nan(angst['mag_obs_i4'])

angst_m1 = np.delete(angst, m1_nans)
angst_i4 = np.delete(angst, i4_nans)

ratio_nod_m1 = calc_ratio(angst_m1['mag_obs_m1'], angst_m1['mag_mod_m1'])
ratio_agb_m1 = calc_ratio(angst_m1['mag_obs_m1'], angst_m1['mag_amod_m1'])
ratio_nod_i4 = calc_ratio(angst_i4['mag_obs_i4'], angst_i4['mag_mod_i4'])
ratio_agb_i4 = calc_ratio(angst_i4['mag_obs_i4'], angst_i4['mag_amod_i4'])

logmet_m1 = map(lambda galaxy: calc_met(galaxy), angst_m1['mag_obs_i2'])
logmet_i4 = map(lambda galaxy: calc_met(galaxy), angst_i4['mag_obs_i2'])

i4_agb_med = phot_utils.calc_median(ratio_agb_i4)
i4_nod_med = phot_utils.calc_median(ratio_nod_i4)
m1_agb_med = phot_utils.calc_median(ratio_agb_m1)
m1_nod_med = phot_utils.calc_median(ratio_nod_m1)

x = 0.75
y = 0.95
ax1 = plt.subplot(2, 2, 1)
ax1.axhline(m1_agb_med, color='#ff536d',linewidth=3)
ax1.axhline(m1_nod_med, color='#0066ff',linewidth=3)
ax1.plot(logmet_m1, ratio_nod_m1, linestyle='none',
        marker='o', color='#0066ff')
ax1.plot(logmet_m1, ratio_agb_m1, linestyle='none',
        marker='o', color='#ff536d')
plt.xlabel('log[O/H]', fontsize=16)
plt.ylabel('M$_\mathrm{obs}$ - M$_\mathrm{mod}$', fontsize=20)
ax1.text(x, y, '24$\mu m$', transform=ax1.transAxes, verticalalignment='top',
        fontsize=14)
plt.ylim(-8, 2)

ax2 = plt.subplot(2, 2, 2)
ax2.axhline(i4_agb_med, color='#ff536d',linewidth=3, label="With AGB Dust")
ax2.axhline(i4_nod_med, color='#0066ff',linewidth=3, label="No AGB Dust")
ax2.plot(logmet_i4, ratio_nod_i4, linestyle='none',
        marker='o', color='#0066ff', alpha=1.0)
ax2.plot(logmet_i4, ratio_agb_i4, linestyle='none',
        marker='o', color='#ff536d', alpha=1.0)
plt.legend(loc='lower right', frameon=False, fontsize=10)
plt.xlabel('log[O/H]', fontsize=16)
ax2.text(x, y, '8$\mu m$', transform=ax2.transAxes, verticalalignment='top',
        fontsize=14)
plt.ylim(-4, 3)

ax3 = plt.subplot(2, 2, 3)
ax3.axhline(m1_agb_med, color='#ff536d',linewidth=3)
ax3.axhline(m1_nod_med, color='#0066ff',linewidth=3)
ax3.plot(angst_m1['LogSFR'] - angst_m1['logM'], ratio_nod_m1, linestyle='none', marker='o',
        color='#0066ff')
ax3.plot(angst_m1['LogSFR'] - angst_m1['logM'], ratio_agb_m1, linestyle='none', marker='o',
        color='#ff536d')
plt.xlabel('Log(SFR)/Log(M)', fontsize=16)
plt.ylabel('M$_\mathrm{obs}$ - M$_\mathrm{mod}$', fontsize=20)
ax3.text(x, y, '24$\mu m$', transform=ax3.transAxes, verticalalignment='top',
        fontsize=14)
plt.ylim(-8, 2)

ax4 = plt.subplot(2, 2, 4)
ax4.axhline(i4_agb_med, color='#ff536d',linewidth=3, label="With AGB Dust")
ax4.axhline(i4_nod_med, color='#0066ff',linewidth=3, label="No AGB Dust")
ax4.plot(angst_i4['LogSFR'] - angst_i4['logM'], ratio_nod_i4, linestyle='none', marker='o',
        color='#0066ff')
ax4.plot(angst_i4['LogSFR'] - angst_i4['logM'], ratio_agb_i4, linestyle='none', marker='o',
        color='#ff536d')
plt.legend(loc='lower right', frameon=False, fontsize=10)
plt.xlabel('Log(SFR)/Log(M)', fontsize=16)
ax4.text(x, y, '8$\mu m$', transform=ax4.transAxes, verticalalignment='top',
        fontsize=14)
plt.ylim(-4, 2)

plt.tight_layout()
plt.show()
