import numpy as np
from itertools import product
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import cm
import sys

fig = plt.figure(figsize=(11, 10))

# Set histogram characteristics
levels = [2, 8, 32, 64, 128, 256, 512]
bins   = 50
cmap   = cm.gray
cmap.set_gamma(0.1)

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

# Read in data
smc_cmd1 = np.loadtxt('smc_irac1irac3.phot')
smc_cmd2 = np.loadtxt('smc_irac1twomj.phot')
#lmc_cmd1 = np.loadtxt('lmc_irac1irac3.phot')
#lmc_cmd2 = np.loadtxt('lmc_irac1twomj.phot')

outer_grid = gridspec.GridSpec(2, 2, wspace=0.05, hspace=0.05)
for i in xrange(4):
    inner_grid = gridspec.GridSpecFromSubplotSpec(1, 3,
                 subplot_spec=outer_grid[i], wspace=0.0, hspace=0.0)
    for j in xrange(3):
        ax = plt.Subplot(fig, inner_grid[j])
        if i == 0:
            plotcmd(smc_cmd1[:,0]-smc_cmd1[:,1], smc_cmd1[:,1], bins, levels,
                    -1, 2, 13, 4, ax)
        if i == 1:
            plotcmd(smc_cmd2[:,0]-smc_cmd2[:,1], smc_cmd2[:,1], bins, levels,
                    -2, 3, 13, 7, ax)
        #if i == 2:
        #    ax.plot(lmc_cmd1[:,0]-lmc_cmd1[:,1], lmc_cmd1[:,1], linestyle='none', marker=',')
        #if i == 3:
        #    ax.plot(lmc_cmd2[:,0]-lmc_cmd2[:,1], lmc_cmd2[:,1], linestyle='none', marker=',')
        ax.set_xticks([])
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



