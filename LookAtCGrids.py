import numpy as np
import matplotlib.pyplot as plt
import glob
from pylab import *

models = (glob.glob('CGrid/temp*'))
'''
standard1 = np.loadtxt('AGB_C_kmh.stb')
wave1 = standard1[:,0]
fTot1 = standard1[:,1]
fInp1 = standard1[:,5]
ratio1 = np.divide(fTot1, fInp1)

standard2 = np.loadtxt('AGB_C_single.stb')
wave2 = standard2[:,0]
fTot2 = standard2[:,1]
fInp2 = standard2[:,5]
ratio2 = np.divide(fTot2, fInp2)
'''
for i in range(len(models)):
	data1 = np.loadtxt(models[i])
	wave1 = data1[:,0]
	fTot1 = data1[:,1]
	fInp1 = data1[:,5]
	ratio1 = np.divide(fTot1, fInp1)
	plt.plot(wave1, ratio1)

#		data1, data2 = np.loadtxt(lin_models[i]), np.loadtxt(lin_models[i])
#		wave1 = data1[:,0], data2[:,0]
#		fTot1 = data1[:,1], data2[:,1]
#		fInp1 = data1[:,5], data2[:,5]
#		ratio1, ratio2 = np.divide(fTot1, fInp1), np.divide(fTot2, fInp2)
#		plt.plot(wave1, ratio1, color = 'k', label = ' ')
#		plt.plot(wave2, ratio2, color = 'b', label = ' ')

#plt.plot(wave1, ratio1, linewidth = 3, color = "#58FAAC", label = "Tau = 0.022, KMH distribution")
#plt.plot(wave2, ratio2, linewidth = 3, color = "#FA5882", label = "Tau = 0.022, Single grain size")

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Wavelength')
plt.ylabel('fTot/fInp')
plt.title('0.01 < T < 50.0, Teff < 2400')
#plt.legend()
plt.show()
