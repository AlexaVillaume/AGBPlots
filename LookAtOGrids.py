import numpy as np
import matplotlib.pyplot as plt
import glob
from pylab import *

models = (glob.glob('OGrid/temp*'))


'''
standard1 = np.loadtxt('AGB_O_kmh.stb')
wave1 = standard1[:,0]
fTot1 = standard1[:,1]
fInp1 = standard1[:,5]
ratio1 = np.divide(fTot1, fInp1)

standard2 = np.loadtxt('AGB_O_single.stb')
wave2 = standard2[:,0]
fTot2 = standard2[:,1]
fInp2 = standard2[:,5]
ratio2 = np.divide(fTot2, fInp2)
'''

for i in range(len(models)):
	if i % 3 == 0:
		data = np.loadtxt(models[i])
		wave = data[:,0]
		fTot = data[:,1]
		fInp = data[:,5]
		ratio = np.divide(fTot, fInp)
		plt.plot(wave, ratio)


#plt.plot(wave1, ratio1, linewidth = 4, color = "#58FAAC", label = "Tau = 0.46, KMH distribution")
#plt.plot(wave2, ratio2, linewidth = 4, color = "#FA5882", label = "Tau = 0.46, Single grain size")

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Wavelength')
plt.ylabel('fTot/fInp')
plt.title('0.0001 < T < 50, 2000 < Teff < 4000')
plt.legend()
plt.show()
