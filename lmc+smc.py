import numpy as np
from itertools import product
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import cm
from matplotlib.ticker import MultipleLocator
import sys

import phot_utils
import FSPSFiles as fsps

fig = plt.figure(figsize=(11, 8))

# Set histogram characteristics
levels = [2, 8, 32, 64, 128, 256, 512]
bins   = 85
cmap   = cm.gray
cmap.set_gamma(0.04)

def plotcmd(x, y, bins, levels, x1, x2, y1, y2, ax):
    # Make 2D histrogram of x and y data
    h, xe, ye = np.histogram2d(x, y, bins=bins)
    # Contour the histogram and add outlines to the contours
    ax.contourf(h.T, extent=[xe[0],xe[-1], ye[0],ye[-1]],
                        levels=levels, zorder=2, cmap=cmap)
    ax.contour(h.T, extent=[xe[0],xe[-1], ye[0],ye[-1]],
                       levels=levels, colors=('black', 'black', 'black','black'))
    ax.set_xlim(x1, x2)
    ax.set_ylim(y1, y2)

# Read in models
path = '/Users/alexawork/fsps/OUTPUTS/COLORMAG/'
with open(path + 'SMC/SSP.out.cmd_agb_z13_newgrid', "r") as f:
    models = map(lambda line: fsps.readcmd(line), f)
smc_agb_79 =[]
smc_agb_89 =[]
smc_agb_99 =[]
for model in models:
    if model.phase != 6.0:
        if model.logage == 7.9:
            smc_agb_79.append(model)
        if model.logage == 8.9:
            smc_agb_89.append(model)
        if model.logage == 9.9:
            smc_agb_99.append(model)

with open(path + 'SMC/SSP.out.cmd_nod_z13_newgrid', "r") as f:
    models = map(lambda line: fsps.readcmd(line), f)
smc_nod_79 =[]
smc_nod_89 =[]
smc_nod_99 =[]
for model in models:
    if model.phase != 6.0:
        if model.logage == 7.9:
            smc_nod_79.append(model)
        if model.logage == 8.9:
            smc_nod_89.append(model)
        if model.logage == 9.9:
            smc_nod_99.append(model)

with open(path + 'LMC/SSP.out.cmd_agb_z16_newgrid', "r") as f:
    models = map(lambda line: fsps.readcmd(line), f)
lmc_agb_79 =[]
lmc_agb_89 =[]
lmc_agb_99 =[]
for model in models:
    if model.phase != 6.0:
        if model.logage == 7.9:
            lmc_agb_79.append(model)
        if model.logage == 8.9:
            lmc_agb_89.append(model)
        if model.logage == 9.9:
            lmc_agb_99.append(model)

with open(path + 'LMC/SSP.out.cmd_nod_z16_newgrid', "r") as f:
    models = map(lambda line: fsps.readcmd(line), f)
lmc_nod_79 =[]
lmc_nod_89 =[]
lmc_nod_99 =[]
for model in models:
    if model.phase != 6.0:
        if model.logage == 7.9:
            lmc_nod_79.append(model)
        if model.logage == 8.9:
            lmc_nod_89.append(model)
        if model.logage == 9.9:
            lmc_nod_99.append(model)

smc_distmod = 19.05
smc_nod_79_twom_j = map(lambda source: source.TWOMASS_J + smc_distmod, smc_nod_79)
smc_nod_79_irac_1 = map(lambda source: source.IRAC1 + smc_distmod, smc_nod_79)
smc_nod_79_irac_4 = map(lambda source: source.IRAC4 + smc_distmod, smc_nod_79)

smc_nod_89_twom_j = map(lambda source: source.TWOMASS_J + smc_distmod, smc_nod_89)
smc_nod_89_irac_1 = map(lambda source: source.IRAC1 + smc_distmod, smc_nod_89)
smc_nod_89_irac_4 = map(lambda source: source.IRAC4 + smc_distmod, smc_nod_89)

smc_nod_99_twom_j = map(lambda source: source.TWOMASS_J + smc_distmod, smc_nod_99)
smc_nod_99_irac_1 = map(lambda source: source.IRAC1 + smc_distmod, smc_nod_99)
smc_nod_99_irac_4 = map(lambda source: source.IRAC4 + smc_distmod, smc_nod_99)

smc_agb_79_twom_j = map(lambda source: source.TWOMASS_J + smc_distmod, smc_agb_79)
smc_agb_79_irac_1 = map(lambda source: source.IRAC1 + smc_distmod, smc_agb_79)
smc_agb_79_irac_4 = map(lambda source: source.IRAC4 + smc_distmod, smc_agb_79)

smc_agb_89_twom_j = map(lambda source: source.TWOMASS_J + smc_distmod, smc_agb_89)
smc_agb_89_irac_1 = map(lambda source: source.IRAC1 + smc_distmod, smc_agb_89)
smc_agb_89_irac_4 = map(lambda source: source.IRAC4 + smc_distmod, smc_agb_89)

smc_agb_99_twom_j = map(lambda source: source.TWOMASS_J + smc_distmod, smc_agb_99)
smc_agb_99_irac_1 = map(lambda source: source.IRAC1 + smc_distmod, smc_agb_99)
smc_agb_99_irac_4 = map(lambda source: source.IRAC4 + smc_distmod, smc_agb_99)

smc_color1_nod_78 = []
smc_color1_nod_88 = []
smc_color1_nod_98 = []
for i in range(len(smc_nod_79_irac_1)):
    smc_color1_nod_78.append(smc_nod_79_irac_1[i] - smc_nod_79_irac_4[i])
for i in range(len(smc_nod_89_irac_1)):
    smc_color1_nod_88.append(smc_nod_89_irac_1[i] - smc_nod_89_irac_4[i])
for i in range(len(smc_nod_99_irac_1)):
    smc_color1_nod_98.append(smc_nod_99_irac_1[i] - smc_nod_99_irac_4[i])

smc_color2_nod_78 = []
smc_color2_nod_88 = []
smc_color2_nod_98 = []
for i in range(len(smc_nod_79_irac_4)):
    smc_color2_nod_78.append(smc_nod_79_twom_j[i] - smc_nod_79_irac_1[i])
for i in range(len(smc_nod_89_irac_4)):
    smc_color2_nod_88.append(smc_nod_89_twom_j[i] - smc_nod_89_irac_1[i])
for i in range(len(smc_nod_99_irac_4)):
    smc_color2_nod_98.append(smc_nod_99_twom_j[i] - smc_nod_99_irac_1[i])

smc_color1_agb_78 = []
smc_color1_agb_88 = []
smc_color1_agb_98 = []
for i in range(len(smc_agb_79_irac_1)):
    smc_color1_agb_78.append(smc_agb_79_irac_1[i] - smc_agb_79_irac_4[i])
for i in range(len(smc_agb_89_irac_1)):
    smc_color1_agb_88.append(smc_agb_89_irac_1[i] - smc_agb_89_irac_4[i])
for i in range(len(smc_agb_99_irac_1)):
    smc_color1_agb_98.append(smc_agb_99_irac_1[i] - smc_agb_99_irac_4[i])

smc_color2_agb_78 = []
smc_color2_agb_88 = []
smc_color2_agb_98 = []
for i in range(len(smc_agb_79_irac_4)):
    smc_color2_agb_78.append(smc_agb_79_twom_j[i] - smc_agb_79_irac_1[i])
for i in range(len(smc_agb_89_irac_4)):
    smc_color2_agb_88.append(smc_agb_89_twom_j[i] - smc_agb_89_irac_1[i])
for i in range(len(smc_agb_99_irac_4)):
    smc_color2_agb_98.append(smc_agb_99_twom_j[i] - smc_agb_99_irac_1[i])


lmc_distmod = 18.5
lmc_nod_79_twom_j = map(lambda source: source.TWOMASS_J + lmc_distmod, lmc_nod_79)
lmc_nod_79_irac_1 = map(lambda source: source.IRAC1 + lmc_distmod, lmc_nod_79)
lmc_nod_79_irac_4 = map(lambda source: source.IRAC4 + lmc_distmod, lmc_nod_79)

lmc_nod_89_twom_j = map(lambda source: source.TWOMASS_J + lmc_distmod, lmc_nod_89)
lmc_nod_89_irac_1 = map(lambda source: source.IRAC1 + lmc_distmod, lmc_nod_89)
lmc_nod_89_irac_4 = map(lambda source: source.IRAC4 + lmc_distmod, lmc_nod_89)

lmc_nod_99_twom_j = map(lambda source: source.TWOMASS_J + lmc_distmod, lmc_nod_99)
lmc_nod_99_irac_1 = map(lambda source: source.IRAC1 + lmc_distmod, lmc_nod_99)
lmc_nod_99_irac_4 = map(lambda source: source.IRAC4 + lmc_distmod, lmc_nod_99)

lmc_agb_79_twom_j = map(lambda source: source.TWOMASS_J + lmc_distmod, lmc_agb_79)
lmc_agb_79_irac_1 = map(lambda source: source.IRAC1 + lmc_distmod, lmc_agb_79)
lmc_agb_79_irac_4 = map(lambda source: source.IRAC4 + lmc_distmod, lmc_agb_79)

lmc_agb_89_twom_j = map(lambda source: source.TWOMASS_J + lmc_distmod, lmc_agb_89)
lmc_agb_89_irac_1 = map(lambda source: source.IRAC1 + lmc_distmod, lmc_agb_89)
lmc_agb_89_irac_4 = map(lambda source: source.IRAC4 + lmc_distmod, lmc_agb_89)

lmc_agb_99_twom_j = map(lambda source: source.TWOMASS_J + lmc_distmod, lmc_agb_99)
lmc_agb_99_irac_1 = map(lambda source: source.IRAC1 + lmc_distmod, lmc_agb_99)
lmc_agb_99_irac_4 = map(lambda source: source.IRAC4 + lmc_distmod, lmc_agb_99)

lmc_color1_nod_78 = []
lmc_color1_nod_88 = []
lmc_color1_nod_98 = []
for i in range(len(lmc_nod_79_irac_1)):
    lmc_color1_nod_78.append(lmc_nod_79_irac_1[i] - lmc_nod_79_irac_4[i])
for i in range(len(lmc_nod_89_irac_1)):
    lmc_color1_nod_88.append(lmc_nod_89_irac_1[i] - lmc_nod_89_irac_4[i])
for i in range(len(lmc_nod_99_irac_1)):
    lmc_color1_nod_98.append(lmc_nod_99_irac_1[i] - lmc_nod_99_irac_4[i])

lmc_color2_nod_78 = []
lmc_color2_nod_88 = []
lmc_color2_nod_98 = []
for i in range(len(lmc_nod_79_irac_4)):
    lmc_color2_nod_78.append(lmc_nod_79_twom_j[i] - lmc_nod_79_irac_1[i])
for i in range(len(lmc_nod_89_irac_4)):
    lmc_color2_nod_88.append(lmc_nod_89_twom_j[i] - lmc_nod_89_irac_1[i])
for i in range(len(lmc_nod_99_irac_4)):
    lmc_color2_nod_98.append(lmc_nod_99_twom_j[i] - lmc_nod_99_irac_1[i])

lmc_color1_agb_78 = []
lmc_color1_agb_88 = []
lmc_color1_agb_98 = []
for i in range(len(lmc_agb_79_irac_1)):
    lmc_color1_agb_78.append(lmc_agb_79_irac_1[i] - lmc_agb_79_irac_4[i])
for i in range(len(lmc_agb_89_irac_1)):
    lmc_color1_agb_88.append(lmc_agb_89_irac_1[i] - lmc_agb_89_irac_4[i])
for i in range(len(lmc_agb_99_irac_1)):
    lmc_color1_agb_98.append(lmc_agb_99_irac_1[i] - lmc_agb_99_irac_4[i])

lmc_color2_agb_78 = []
lmc_color2_agb_88 = []
lmc_color2_agb_98 = []
for i in range(len(lmc_agb_79_irac_4)):
    lmc_color2_agb_78.append(lmc_agb_79_twom_j[i] - lmc_agb_79_irac_1[i])
for i in range(len(lmc_agb_89_irac_4)):
    lmc_color2_agb_88.append(lmc_agb_89_twom_j[i] - lmc_agb_89_irac_1[i])
for i in range(len(lmc_agb_99_irac_4)):
    lmc_color2_agb_98.append(lmc_agb_99_twom_j[i] - lmc_agb_99_irac_1[i])

# Read in data
smc_cmd1 = np.loadtxt('smc_irac1irac4.phot')
smc_cmd2 = np.loadtxt('smc_irac1twomj.phot')
lmc_cmd1 = np.loadtxt('lmc_irac1irac4.phot')
lmc_cmd2 = np.loadtxt('lmc_irac1twomj.phot')

x = 0.1
y = 0.95
outer_grid = gridspec.GridSpec(2, 2, wspace=0.2, hspace=0.2)
for i in xrange(4):
    inner_grid = gridspec.GridSpecFromSubplotSpec(1, 3,
                 subplot_spec=outer_grid[i], wspace=0.0, hspace=0.0)
    for j in xrange(3):
        ax = plt.Subplot(fig, inner_grid[j])
        if i == 0:
            plotcmd(smc_cmd1[:,0]-smc_cmd1[:,1], smc_cmd1[:,1], bins, levels,
                    -1, 2, 13, 4, ax)
            majorLocator   = MultipleLocator(1.5)
            ax.xaxis.set_major_locator(majorLocator)
            if j == 0:
                ax.plot(smc_color1_agb_78, smc_agb_79_irac_4, linewidth=2,
                        color='#ff536d')
                ax.plot(smc_color1_nod_78, smc_nod_79_irac_4, linewidth=2,
                        color='#0066ff')
                ax.set_ylabel("[8.0]", fontsize=16)
                ax.text(x, y, "log(age) = 7.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
            if j == 1:
                ax.plot(smc_color1_agb_88, smc_agb_89_irac_4, linewidth=2,
                        color='#ff536d')
                ax.plot(smc_color1_nod_88, smc_nod_89_irac_4, linewidth=2,
                        color='#0066ff')
                ax.set_xlabel("[3.6] - [8.0]", fontsize=16)
                ax.text(x, y, "log(age) = 8.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
                ax.set_yticks([])
            if j == 2:
                ax.plot(smc_color1_agb_98, smc_agb_99_irac_4, linewidth=2,
                        color='#ff536d')
                ax.plot(smc_color1_nod_98, smc_nod_99_irac_4, linewidth=2,
                        color='#0066ff')
                ax.text(x, y, "log(age) = 9.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
                ax.set_yticks([])

        if i == 1:
            plotcmd(smc_cmd2[:,1]-smc_cmd2[:,0], smc_cmd2[:,0], bins, levels,
                    -1, 6, 13, 5, ax)
            majorLocator   = MultipleLocator(2.5)
            ax.xaxis.set_major_locator(majorLocator)
            if j == 0:
                ax.plot(smc_color2_agb_78, smc_agb_79_irac_1, linewidth=2,
                        color='#ff536d')
                ax.plot(smc_color2_nod_78, smc_nod_79_irac_1, linewidth=2,
                        color='#0066ff')
                ax.set_ylabel("[3.6]", fontsize=16)
                ax.text(x, y, "log(age) = 7.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
            if j == 1:
                ax.plot(smc_color2_agb_88, smc_agb_89_irac_1, linewidth=2,
                        color='#ff536d')
                ax.plot(smc_color2_nod_88, smc_nod_89_irac_1, linewidth=2,
                        color='#0066ff')
                ax.set_xlabel("j - [3.6]", fontsize=16)
                ax.text(x, y, "log(age) = 8.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
                ax.set_yticks([])
            if j == 2:
                ax.plot(smc_color2_agb_98, smc_agb_99_irac_1, linewidth=2,
                        color='#ff536d')
                ax.plot(smc_color2_nod_98, smc_nod_99_irac_1, linewidth=2,
                        color='#0066ff')
                ax.text(x, y, "log(age) = 9.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
                ax.set_yticks([])
        if i == 2:
            plotcmd(lmc_cmd1[:,0]-lmc_cmd1[:,1], lmc_cmd1[:,1], bins, levels,
                    -1, 5, 13, 2, ax)
            majorLocator   = MultipleLocator(3)
            ax.xaxis.set_major_locator(majorLocator)
            if j == 0:
                ax.plot(lmc_color1_agb_78, lmc_agb_79_irac_4, linewidth=2,
                        color='#ff536d')
                ax.plot(lmc_color1_nod_78, lmc_nod_79_irac_4, linewidth=2,
                        color='#0066ff')
                ax.set_ylabel("[8.0]", fontsize=16)
                ax.text(x, y, "log(age) = 7.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
            if j == 1:
                ax.plot(lmc_color1_agb_88, lmc_agb_89_irac_4, linewidth=2,
                        color='#ff536d')
                ax.plot(lmc_color1_nod_88, lmc_nod_89_irac_4, linewidth=2,
                        color='#0066ff')
                ax.set_xlabel("[3.6] - [8.0]", fontsize=16)
                ax.text(x, y, "log(age) = 8.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
                ax.set_yticks([])
            if j == 2:
                ax.plot(lmc_color1_agb_98, lmc_agb_99_irac_4, linewidth=2,
                        color='#ff536d')
                ax.plot(lmc_color1_nod_98, lmc_nod_99_irac_4, linewidth=2,
                        color='#0066ff')
                ax.text(x, y, "log(age) = 9.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
                ax.set_yticks([])
        if i == 3:
            plotcmd(lmc_cmd2[:,0]-lmc_cmd2[:,1], lmc_cmd2[:,1], bins, levels,
                    -1, 7, 13, 5, ax)
            majorLocator   = MultipleLocator(2.5)
            ax.xaxis.set_major_locator(majorLocator)
            if j == 0:
                ax.plot(lmc_color2_agb_78, lmc_agb_79_irac_1, linewidth=2,
                        color='#ff536d')
                ax.plot(lmc_color2_nod_78, lmc_nod_79_irac_1, linewidth=2,
                        color='#0066ff')
                ax.set_ylabel("[8.0]", fontsize=16)
                ax.text(x, y, "log(age) = 7.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
            if j == 1:
                ax.plot(lmc_color2_agb_88, lmc_agb_89_irac_1, linewidth=2,
                        color='#ff536d')
                ax.plot(lmc_color2_nod_88, lmc_nod_89_irac_1, linewidth=2,
                        color='#0066ff')
                ax.set_xlabel("[3.6] - [8.0]", fontsize=16)
                ax.text(x, y, "log(age) = 8.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
                ax.set_yticks([])
            if j == 2:
                ax.plot(lmc_color2_agb_98, lmc_agb_99_irac_1, linewidth=2,
                        color='#ff536d')
                ax.plot(lmc_color2_nod_98, lmc_nod_99_irac_1, linewidth=2,
                        color='#0066ff')
                ax.text(x, y, "log(age) = 9.9", transform=ax.transAxes,
                        verticalalignment='top', fontsize=10)
                ax.set_yticks([])
        fig.add_subplot(ax)

all_axes = fig.get_axes()

# Show only the outside spines
for ax in all_axes:
    for sp in ax.spines.values():
        sp.set_visible(False)
        if ax.is_first_row():
            ax.spines['top'].set_visible(True)
        if ax.is_last_row():
            ax.spines['bottom'].set_visible(True)
        if ax.is_first_col():
            ax.spines['left'].set_visible(True)
        if ax.is_last_col():
            ax.spines['right'].set_visible(True)


plt.show()



