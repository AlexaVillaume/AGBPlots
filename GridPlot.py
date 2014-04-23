'''
Make plot of subset of the c and o grids for paper
'''
import numpy as np
import matplotlib.pyplot as plt

cmodel1 = np.loadtxt("CGrid/temp_teff2400_tau0.001")
cmodel2 = np.loadtxt("CGrid/temp_teff2400_tau0.10324")
cmodel3 = np.loadtxt("CGrid/temp_teff2400_tau0.93933")
cmodel4 = np.loadtxt("CGrid/temp_teff2400_tau50.0")

omodel1 = np.loadtxt("OGrid/temp_teff2000_tau0.001")
omodel2 = np.loadtxt("OGrid/temp_teff2000_tau0.10324")
omodel3 = np.loadtxt("OGrid/temp_teff2000_tau0.93933")
omodel4 = np.loadtxt("OGrid/temp_teff2000_tau50.0")

x=0.7
y=0.95

ax2 = plt.subplot(1,2,2)
ax2.plot(cmodel1[:,0], cmodel1[:,1]/cmodel1[:,5], linestyle='-', linewidth=3, color='#0066ff')
ax2.plot(cmodel2[:,0], cmodel2[:,1]/cmodel2[:,5], linestyle='-', linewidth=3, color='#f88534')
ax2.plot(cmodel3[:,0], cmodel3[:,1]/cmodel3[:,5], linestyle='-', linewidth=3, color='#83c460')
ax2.plot(cmodel4[:,0], cmodel4[:,1]/cmodel4[:,5], linestyle='-', linewidth=3, color='#ff536d')
ax2.text(x, y, 'C-Rich Dust', transform=ax2.transAxes, verticalalignment='top', fontsize=10)
plt.xlim(10e-1, 10e3)
plt.ylim(10e-2, 10e3)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Wavelength ($\mu m$)', fontsize=16)
plt.ylabel("$F_{AGB}/F$", fontsize=16)

ax1 = plt.subplot(1,2,1)
ax1.plot(omodel1[:,0], omodel1[:,1]/omodel1[:,5], linestyle='-',
        linewidth=3, color='#0066ff', label=r"$\tau_{agb}$ = 0.01")
ax1.plot(omodel2[:,0], omodel2[:,1]/omodel2[:,5], linestyle='-',
        linewidth=3, color='#f88534', label=r"$\tau_{agb}$ = 0.1")
ax1.plot(omodel3[:,0], omodel3[:,1]/omodel3[:,5], linestyle='-',
        linewidth=3, color='#83c460', label=r"$\tau_{agb}$ = 1.0")
ax1.plot(omodel4[:,0], omodel4[:,1]/omodel4[:,5], linestyle='-',
        linewidth=3, color='#ff536d', label=r"$\tau_{agb}$ = 50.0")
ax1.text(x, y, 'O-Rich Dust', transform=ax1.transAxes, verticalalignment='top', fontsize=10)
plt.xlim(10e-1, 10e3)
plt.ylim(10e-2, 10e3)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Wavelength ($\mu m$)', fontsize=16)
plt.ylabel("$F_{AGB}/F$", fontsize=16)
plt.legend(loc="upper left", frameon=False, fontsize=10)

plt.tight_layout()
plt.show()
