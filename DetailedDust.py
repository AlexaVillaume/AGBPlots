import glob
import math
import matplotlib.pyplot as plt
import phot_utils as pu
import FSPSFiles as fsps

dust2 = [0.0, 0.001, 0.003, 0.01, 0.031, 0.097, 0.304, 0.954, 3.0]

# Open data files and read in models to the FSPS class
nod = (glob.glob('/Users/alexawork/fsps/OUTPUTS/CSP*nod*'))
agb = (glob.glob('/Users/alexawork/fsps/OUTPUTS/CSP*agb*'))

nod_data = []
for data in nod:
    catalog = open(data, 'r')
    tmp = filter(lambda line: pu.noHead(line), catalog)
    nod_data.append(map(lambda line: fsps.readmags(line), tmp))

agb_data = []
for data in agb:
    catalog = open(data, 'r')
    tmp = filter(lambda line: pu.noHead(line), catalog)
    agb_data.append(map(lambda line: fsps.readmags(line), tmp))

# Grab age values and convert to Gyr
age = map(lambda d: 10**d.agegyr /1e9, nod_data[0])

# Grab the 24 micron flux at various ages
fnod_0_10 = []
fnod_1_ = []
fnod_2_ = []
fnod_5_ = []
fnod_7_ = []
fnod_10 = []
fnod_14 = []
for model in nod_data:
    age_tmp = filter(lambda d: d.agegyr  == 0.1, model)
    fnod_0_10.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr  == 1.0, model)
    fnod_1_.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr  > 2.0 and d.agegyr  < 2.3, model)
    fnod_2_.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr  > 5.0 and d.agegyr  < 5.6, model)
    fnod_5_.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr  > 7.0 and d.agegyr  < 7.1, model)
    fnod_7_.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr == 10, model)
    fnod_10.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr  > 14.5, model)
    fnod_14.append(map(lambda d: d.MIPS_24, age_tmp))


fagb_0_10 = []
fagb_1_ = []
fagb_2_ = []
fagb_5_ = []
fagb_7_ = []
fagb_10 = []
fagb_14 = []
for model in agb_data:
    age_tmp = filter(lambda d: d.agegyr  == 0.1, model)
    fagb_0_10.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr  == 1.0, model)
    fagb_1_.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr  > 2.0 and d.agegyr < 2.3, model)
    fagb_2_.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr  > 5.0 and d.agegyr < 5.6, model)
    fagb_5_.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr > 7.0 and d.agegyr < 7.1, model)
    fagb_7_.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr == 10, model)
    fagb_10.append(map(lambda d: d.MIPS_24, age_tmp))
    age_tmp = filter(lambda d: d.agegyr > 14, model)
    fagb_14.append(map(lambda d: d.MIPS_24, age_tmp))

ratio1 = []
ratio2 = []
ratio3 = []
ratio4 = []
ratio5 = []
ratio6 = []
for i in range(len(dust2)):
    ratio1.append(math.pow(10, (fnod_0_10[i][0] - fagb_0_10[i][0])/2.5))
    ratio2.append(math.pow(10, (fnod_1_[i][0] - fagb_1_[i][0])/2.5))
    ratio6.append(math.pow(10, (fnod_7_[i][0] - fagb_7_[i][0])/2.5))
    ratio3.append(math.pow(10, (fnod_5_[i][0] - fagb_5_[i][0])/2.5))
    ratio4.append(math.pow(10, (fnod_10[i][0] - fagb_10[i][0])/2.5))
    ratio5.append(math.pow(10, (fnod_14[i][0] - fagb_14[i][0])/2.5))

plt.plot(dust2, ratio1, linewidth=2, color='#424242', label = 'Age (Gyr) = 0.1')
plt.plot(dust2, ratio2, linewidth=2, color='#0066ff', label = 'Age (Gyr) = 1.0')
plt.plot(dust2, ratio3, linewidth=2, color='#ff536d', label = 'Age (Gyr) ~ 5.0')
plt.plot(dust2, ratio6, linewidth=2, color='#f88534', label = 'Age (Gyr) ~ 7.0')
plt.plot(dust2, ratio4, linewidth=2, color='#83c460', label = 'Age (Gyr) = 10.0')
plt.plot(dust2, ratio5, linewidth=2, color='#CC0099', label = 'Age (Gyr) ~ 14.0')

plt.xscale('log')
plt.ylim(0.9,2)
plt.xlabel(r"$\tau_{diff}$", fontsize=24)
plt.ylabel(r"$\Delta_{24_{\mu m}}$", fontsize=24)
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
