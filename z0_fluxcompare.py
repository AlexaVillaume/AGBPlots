'''
PURPOSE
    Compare the the flux at different wavelengths of different models as a function of age
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

sfh_agb = ["/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh001_dust00_agb_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust00_agb_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh10_dust00_agb_CSP.mags"]

sfh_nod = ["/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh001_dust00_nod_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust00_nod_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh10_dust00_nod_CSP.mags"]

met_agb = ["/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z13_Z00_sfh01_dust00_agb_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust00_agb_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z19_Z00_sfh01_dust00_agb_CSP.mags"]

met_nod = ["/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z13_Z00_sfh01_dust00_nod_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust00_nod_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z19_Z00_sfh01_dust00_nod_CSP.mags"]

dust_agb = ["/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust00_agb_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust0103_agb_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust1505_agb_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust31_agb_CSP.mags"]

dust_nod = ["/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust00_nod_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust0103_nod_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust1505_nod_CSP.mags",
            "/Users/alexawork/fsps/OUTPUTS/SEDFitting/z0/z16_Z00_sfh01_dust31_nod_CSP.mags"]

sfh_models_agb = []
sfh_models_nod = []
for i in range(len(sfh_agb)):
    blah_agb = open(sfh_agb[i])
    blah_nod = open(sfh_nod[i])
    tmp1 = filter(lambda line: phot_utils.noHead(line), blah_agb)
    tmp2 = filter(lambda line: phot_utils.noHead(line), blah_nod)
    sfh_models_agb.append(map(lambda line: f.readmags(line), tmp1))
    sfh_models_nod.append(map(lambda line: f.readmags(line), tmp2))
    blah_agb.close()
    blah_nod.close()

met_models_agb = []
met_models_nod = []
for i in range(len(met_agb)):
    blah_agb = open(met_agb[i])
    blah_nod = open(met_nod[i])
    tmp1 = filter(lambda line: phot_utils.noHead(line), blah_agb)
    tmp2 = filter(lambda line: phot_utils.noHead(line), blah_nod)
    met_models_agb.append(map(lambda line: f.readmags(line), tmp1))
    met_models_nod.append(map(lambda line: f.readmags(line), tmp2))
    blah_agb.close()
    blah_nod.close()

dust_models_agb = []
dust_models_nod = []
for i in range(len(dust_agb)):
    blah_agb = open(dust_agb[i])
    blah_nod = open(dust_nod[i])
    tmp1 = filter(lambda line: phot_utils.noHead(line), blah_agb)
    tmp2 = filter(lambda line: phot_utils.noHead(line), blah_nod)
    dust_models_agb.append(map(lambda line: f.readmags(line), tmp1))
    dust_models_nod.append(map(lambda line: f.readmags(line), tmp2))
    blah_agb.close()
    blah_nod.close()

sfh_agb_24 = []
sfh_nod_24 = []
sfh_agb_12 = []
sfh_nod_12 = []
sfh_agb_08 = []
sfh_nod_08 = []
for i in range(len(sfh_models_agb)):
    age = map(lambda d: d.agegyr, sfh_models_agb[0])
    sfh_agb_24.append(map(lambda d: d.MIPS_24, sfh_models_agb[i]))
    sfh_nod_24.append(map(lambda d: d.MIPS_24, sfh_models_nod[i]))
    sfh_agb_12.append(map(lambda d: d.WISE_W3, sfh_models_agb[i]))
    sfh_nod_12.append(map(lambda d: d.WISE_W3, sfh_models_nod[i]))
    sfh_agb_08.append(map(lambda d: d.IRAC4, sfh_models_agb[i]))
    sfh_nod_08.append(map(lambda d: d.IRAC4, sfh_models_nod[i]))

met_agb_24 = []
met_nod_24 = []
met_agb_12 = []
met_nod_12 = []
met_agb_08 = []
met_nod_08 = []
for i in range(len(met_models_agb)):
    met_agb_24.append(map(lambda d: d.MIPS_24, met_models_agb[i]))
    met_nod_24.append(map(lambda d: d.MIPS_24, met_models_nod[i]))
    met_agb_12.append(map(lambda d: d.WISE_W3, met_models_agb[i]))
    met_nod_12.append(map(lambda d: d.WISE_W3, met_models_nod[i]))
    met_agb_08.append(map(lambda d: d.IRAC4, met_models_agb[i]))
    met_nod_08.append(map(lambda d: d.IRAC4, met_models_nod[i]))

dust_agb_24 = []
dust_nod_24 = []
dust_agb_12 = []
dust_nod_12 = []
dust_agb_08 = []
dust_nod_08 = []
for i in range(len(dust_models_agb)):
    dust_agb_24.append(map(lambda d: d.MIPS_24, dust_models_agb[i]))
    dust_nod_24.append(map(lambda d: d.MIPS_24, dust_models_nod[i]))
    dust_agb_12.append(map(lambda d: d.WISE_W3, dust_models_agb[i]))
    dust_nod_12.append(map(lambda d: d.WISE_W3, dust_models_nod[i]))
    dust_agb_08.append(map(lambda d: d.IRAC4, dust_models_agb[i]))
    dust_nod_08.append(map(lambda d: d.IRAC4, dust_models_nod[i]))

sfh_ratio_24 = []
sfh_ratio_24 = []
sfh_ratio_12 = []
sfh_ratio_08 = []
for i in range(len(sfh_agb_24)):
    sfh_ratio_24.append(calcRatio(sfh_agb_24[i], sfh_nod_24[i]))
    sfh_ratio_12.append(calcRatio(sfh_agb_12[i], sfh_nod_12[i]))
    sfh_ratio_08.append(calcRatio(sfh_agb_08[i], sfh_nod_08[i]))

met_ratio_24 = []
met_ratio_12 = []
met_ratio_08 = []
for i in range(len(met_agb_24)):
    met_ratio_24.append(calcRatio(met_agb_24[i], met_nod_24[i]))
    met_ratio_12.append(calcRatio(met_agb_12[i], met_nod_12[i]))
    met_ratio_08.append(calcRatio(met_agb_08[i], met_nod_08[i]))

dust_ratio_24 = []
dust_ratio_12 = []
dust_ratio_08 = []
for i in range(len(dust_agb_24)):
    dust_ratio_24.append(calcRatio(dust_agb_24[i], dust_nod_24[i]))
    dust_ratio_12.append(calcRatio(dust_agb_12[i], dust_nod_12[i]))
    dust_ratio_08.append(calcRatio(dust_agb_08[i], dust_nod_08[i]))

# ========================================================= #
# ========================================================= #
# Plotting the changes in SFH #
# ========================================================= #
ax1 = plt.subplot(3,3,2)
for model in sfh_ratio_24:
    ax1.plot(age, model, linestyle='-', linewidth=3)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-1, 10e2)

ax2 = plt.subplot(3,3,5)
for model in sfh_ratio_12:
    ax2.plot(age, model, linestyle='-', linewidth=3)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-1, 10e2)

ax3 = plt.subplot(3,3,8)
for model in sfh_ratio_08:
    ax3.plot(age, model, linestyle='-', linewidth=3)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-1, 10e2)
plt.xlabel('Age (Gyr)', fontsize=16)

# ========================================================= #
# Plotting the changes in metallicity #
# ========================================================= #
ax4 = plt.subplot(3,3,1)
for model in met_ratio_24:
    ax4.plot(age, model, linestyle='-', linewidth=3)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-1, 10e2)
plt.ylabel(r"$\Delta_{24_{\mu m}}$", fontsize=24)

ax5 = plt.subplot(3,3,4)
for model in sfh_ratio_12:
    ax5.plot(age, model, linestyle='-', linewidth=3)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-1, 10e2)
plt.ylabel(r"$\Delta_{12_{\mu m}}$", fontsize=24)

ax6 = plt.subplot(3,3,7)
for model in sfh_ratio_08:
    ax6.plot(age, model, linestyle='-', linewidth=3)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-1, 10e2)
plt.ylabel(r"$\Delta_{8_{\mu m}}$", fontsize=24)

# ========================================================= #
# Plotting the changes in dust #
# ========================================================= #

ax7 = plt.subplot(3,3,3)
for model in dust_ratio_24:
    ax7.plot(age, model, linestyle='-', linewidth=3)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-1, 10e2)

ax8 = plt.subplot(3,3,6)
for model in dust_ratio_12:
    ax8.plot(age, model, linestyle='-', linewidth=3)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-1, 10e2)

ax9 = plt.subplot(3,3,9)
for model in dust_ratio_08:
    ax9.plot(age, model, linestyle='-', linewidth=3)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10e-2, 10e0)
plt.ylim(10e-1, 10e2)


plt.tight_layout()
plt.show()
