'''
PURPOSE
    To test how the dust scaling affects the models and how the c-rich and o-rich stars influence     things

'''

import glob
import matplotlib.pyplot as plt
import math
import FSPSFiles as f
import phot_utils

def calcRatio(agb, nod):
    ratio = []
    for i in range(len(agb)):
        ratio.append(math.pow(10, (nod[i] - agb[i])/2.5))
    return ratio

datapath = '/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/scaling/'

# The zsol models
with open(datapath + "z20_Z00_sfh01_dust00_agb_SSP_o.mags", "r") as tmp:
    o_agb_z20 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), o_agb_z20)
    age = map(lambda line: line.agegyr, model)
    o_agb_z20_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z20_Z00_sfh01_dust00_nod_SSP_o.mags", "r") as tmp:
    o_nod_z20 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), o_nod_z20)
    o_nod_z20_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z20_Z00_sfh01_dust00_agb_SSP_c.mags", "r") as tmp:
    c_agb_z20 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), c_agb_z20)
    c_agb_z20_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z20_Z00_sfh01_dust00_nod_SSP_c.mags", "r") as tmp:
    c_nod_z20 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), c_nod_z20)
    c_nod_z20_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z20_Z00_sfh01_dust00_agb_SSP_scale.mags", "r") as tmp:
    scale_agb_z20 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), scale_agb_z20)
    scale_agb_z20_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z20_Z00_sfh01_dust00_nod_SSP_scale.mags", "r") as tmp:
    scale_nod_z20 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), scale_nod_z20)
    scale_nod_z20_24 = map(lambda line: line.MIPS_24, model)

# The 0.1zsol models
with open(datapath + "z10_Z00_sfh01_dust00_agb_SSP_o.mags", "r") as tmp:
    o_agb_z10 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), o_agb_z10)
    o_agb_z10_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z10_Z00_sfh01_dust00_nod_SSP_o.mags", "r") as tmp:
    o_nod_z10 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), o_nod_z10)
    o_nod_z10_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z10_Z00_sfh01_dust00_agb_SSP_c.mags", "r") as tmp:
    c_agb_z10 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), c_agb_z10)
    c_agb_z10_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z10_Z00_sfh01_dust00_nod_SSP_c.mags", "r") as tmp:
    c_nod_z10 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), c_nod_z10)
    c_nod_z10_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z10_Z00_sfh01_dust00_agb_SSP_scale.mags", "r") as tmp:
    scale_agb_z10 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), scale_agb_z10)
    scale_agb_z10_24 = map(lambda line: line.MIPS_24, model)

with open(datapath + "z10_Z00_sfh01_dust00_nod_SSP_scale.mags", "r") as tmp:
    scale_nod_z10 = filter(lambda line: phot_utils.noHead(line), tmp)
    model = map(lambda line: f.readmags(line), scale_nod_z10)
    scale_nod_z10_24 = map(lambda line: line.MIPS_24, model)

z20_both = calcRatio(scale_agb_z20_24, scale_nod_z20_24)
z20_cstar = calcRatio(c_agb_z20_24, c_nod_z20_24)
z20_ostar = calcRatio(o_agb_z20_24, o_nod_z20_24)

z10_both = calcRatio(scale_agb_z10_24, scale_nod_z10_24)
z10_cstar = calcRatio(c_agb_z10_24, c_nod_z10_24)
z10_ostar = calcRatio(o_agb_z10_24, o_nod_z10_24)

ax1 = plt.subplot(1,3,1)
ax1.plot(age, z20_both, label="Both", linewidth=6, color='#83c460')
ax1.plot(age, z20_cstar, label="Only Carbon rich", linewidth=3, color='#f88534')
ax1.plot(age, z20_ostar, label="Only Oxygen rich", linewidth=3, color='#0066ff')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-2, 10e3)
plt.xscale('log')
plt.yscale('log')
plt.legend(frameon=False, fontsize=10)

ax2 = plt.subplot(1,3,3)
ax2.plot(age, z10_both, label="Both", linewidth=6, color='#83c460')
ax2.plot(age, z10_cstar, label="Only Carbon rich", linewidth=3, color='#f88534')
ax2.plot(age, z10_ostar, label="Only Oxygen rich", linewidth=3, color='#0066ff')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-2, 10e3)
plt.xscale('log')
plt.yscale('log')
plt.legend(frameon=False, fontsize=10)


plt.tight_layout()
plt.show()


