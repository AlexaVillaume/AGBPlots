'''
Recreating Cassara et al. fig 10 with our own models
'''
import matplotlib.pyplot as plt
import FSPSFiles as fsps

z13_nod = fsps.readspec("/Users/alexawork/fsps/OUTPUTS/z13_nod_SSP.out.spec")
for model in z13_nod:
    if model.agegyr == 0.2:
        z13_nod_020 = model.flux
        wave = model.wave
    if model.agegyr > 1.9 and model.agegyr < 2.1:
         z13_nod_200 = model.flux

z13_agb = fsps.readspec("/Users/alexawork/fsps/OUTPUTS/z13_agb_SSP.out.spec")
for model in z13_agb:
    if model.agegyr == 0.2:
        z13_agb_020 = model.flux
    if model.agegyr > 1.9 and model.agegyr < 2.1:
         z13_agb_200 = model.flux

z20_nod = fsps.readspec("/Users/alexawork/fsps/OUTPUTS/z20_nod_SSP.out.spec")
for model in z20_nod:
    if model.agegyr == 0.2:
        z20_nod_020 = model.flux
    if model.agegyr > 1.9 and model.agegyr < 2.1:
         z20_nod_200 = model.flux

plt.plot(wave, z13_nod_020, linestyle='--')
z20_agb = fsps.readspec("/Users/alexawork/fsps/OUTPUTS/z20_agb_SSP.out.spec")
for model in z20_agb:
    if model.agegyr == 0.2:
        z20_agb_020 = model.flux
    if model.agegyr > 1.9 and model.agegyr < 2.1:
         z20_agb_200 = model.flux

x = 0.62
y = 0.88

ax1 = plt.subplot(1,2,1)
ax1.plot(wave, z13_agb_020, linestyle='-', linewidth=2, color='#83c460', label = "Age (Gyr) = 0.2")
ax1.plot(wave, z13_nod_020, linestyle='--', linewidth=2, color='#424242')
ax1.plot(wave, z13_agb_200, linestyle='-', linewidth=2, color='#f88534', label = "Age (Gyr) = 2.0")
ax1.plot(wave, z13_nod_200, linestyle='--', linewidth=2, color='#424242')
ax1.text(x, y, 'Z = 0.039', transform=ax1.transAxes, verticalalignment = 'top', fontsize=10)
plt.ylim(10e-18, 10e-15)
plt.xlim(10e-3, 10e2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Wavelength ($\mu m$)', fontsize=16)
plt.ylabel('Flux (Jy)', fontsize=16)
plt.legend(frameon=False, fontsize=10)

ax2 = plt.subplot(1,2,2)
ax2.plot(wave, z20_agb_020, linestyle='-', linewidth=2, color='#83c460', label = "Age (Gyr) = 0.2")
ax2.plot(wave, z20_nod_020, linestyle='--', linewidth=2, color='#424242')
ax2.plot(wave, z20_agb_200, linestyle='-', linewidth=2, color='#f88534', label = "Age (Gyr) = 2.0")
ax2.plot(wave, z20_nod_200, linestyle='--', linewidth=2, color='#424242')
ax2.text(x, y, 'Z = 0.019', transform=ax2.transAxes, verticalalignment = 'top', fontsize=10)
plt.ylim(10e-18, 10e-15)
plt.xlim(10e-3, 10e2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Wavelength ($\mu m$)', fontsize=16)
plt.ylabel('Flux (Jy)', fontsize=16)
plt.legend(frameon=False, fontsize=10)

plt.tight_layout()
plt.show()
