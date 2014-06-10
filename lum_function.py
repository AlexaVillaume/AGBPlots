'''
Attempting to estimate how many dust enshrouded AGB stars we should expect in galaxy
'''
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from FSPSFiles import readcmd
import phot_utils

fig = plt.figure(figsize=(11, 4))

path = '/Users/alexawork/fsps/OUTPUTS/'
with open(path + 'SOL_SSP.out.cmd', 'r') as f:
    sol_models = map(lambda line: readcmd(line), f)
with open(path + 'SMC_SSP.out.cmd', 'r') as f:
    smc_models = map(lambda line: readcmd(line), f)
with open(path + 'z10_SSP.out.cmd', 'r') as f:
    z10_models = map(lambda line: readcmd(line), f)

# Get stars of AGB phase and appropriate age
sol_87 = []
sol_89 = []
sol_91 = []
for model in sol_models:
    if model.phase == 5:
        if model.logage == 8.7:
            sol_87.append(model)
        if model.logage == 8.9:
            sol_89.append(model)
        if model.logage == 9.1:
            sol_91.append(model)

smc_87 = []
smc_89 = []
smc_91 = []
for model in smc_models:
    if model.phase == 5:
        if model.logage == 8.7:
            smc_87.append(model)
        if model.logage == 8.9:
            smc_89.append(model)
        if model.logage == 9.1:
            smc_91.append(model)

z10_87 = []
z10_89 = []
z10_91 = []
for model in z10_models:
    if model.phase == 5:
        if model.logage == 8.7:
            z10_87.append(model)
        if model.logage == 8.9:
            z10_89.append(model)
        if model.logage == 9.1:
            z10_91.append(model)

" Make luminosity function "
sol_imf_87 = map(lambda star: 10**star.logimfweight, sol_87)
sol_lbol_87 = map(lambda star: 10**star.loglbol, sol_87)
sol_agb_87 = map(lambda star: star.tau, sol_87)
sol_cul_lum_87 = []
# Make it cumulative
for value in sol_lbol_87:
    tmp = []
    for j, val in enumerate(sol_lbol_87):
        if val >= value:
        # Select imf values that correspond to app. lbol values
            tmp.append(sol_imf_87[j])
    sol_cul_lum_87.append(sum(tmp))
sol_cul_lum_87 = map(lambda star: math.log10(star), sol_cul_lum_87)
sol_lbol_87 = map(lambda star: math.log10(star), sol_lbol_87)
sol_agb_87 = map(lambda star: math.log10(star), sol_agb_87)

sol_imf_89 = map(lambda star: 10**star.logimfweight, sol_89)
sol_lbol_89 = map(lambda star: 10**star.loglbol, sol_89)
sol_cul_lum_89 = []
# Make it cumulative
for value in sol_lbol_89:
    tmp = []
    for j, val in enumerate(sol_lbol_89):
        if val >= value:
        # Select imf values that correspond to app. lbol values
            tmp.append(sol_imf_89[j])
    sol_cul_lum_89.append(sum(tmp))
sol_cul_lum_89 = map(lambda star: math.log10(star), sol_cul_lum_89)
sol_lbol_89 = map(lambda star: math.log10(star), sol_lbol_89)

sol_imf_91 = map(lambda star: 10**star.logimfweight, sol_91)
sol_lbol_91 = map(lambda star: 10**star.loglbol, sol_91)
sol_cul_lum_91 = []
# Make it cumulative
for value in sol_lbol_91:
    tmp = []
    for j, val in enumerate(sol_lbol_91):
        if val >= value:
        # Select imf values that correspond to app. lbol values
            tmp.append(sol_imf_91[j])
    sol_cul_lum_91.append(sum(tmp))
sol_cul_lum_91 = map(lambda star: math.log10(star), sol_cul_lum_91)
sol_lbol_91 = map(lambda star: math.log10(star), sol_lbol_91)

smc_imf_87 = map(lambda star: 10**star.logimfweight, smc_87)
smc_lbol_87 = map(lambda star: 10**star.loglbol, smc_87)
smc_cul_lum_87 = []
# Make it cumulative
for value in smc_lbol_87:
    tmp = []
    for j, val in enumerate(smc_lbol_87):
        if val >= value:
        # Select imf values that correspond to app. lbol values
            tmp.append(smc_imf_87[j])
    smc_cul_lum_87.append(sum(tmp))
smc_cul_lum_87 = map(lambda star: math.log10(star), smc_cul_lum_87)
smc_lbol_87 = map(lambda star: math.log10(star), smc_lbol_87)

smc_imf_89 = map(lambda star: 10**star.logimfweight, smc_89)
smc_lbol_89 = map(lambda star: 10**star.loglbol, smc_89)
smc_cul_lum_89 = []
# Make it cumulative
for value in smc_lbol_89:
    tmp = []
    for j, val in enumerate(smc_lbol_89):
        if val >= value:
        # Select imf values that correspond to app. lbol values
            tmp.append(smc_imf_89[j])
    smc_cul_lum_89.append(sum(tmp))
smc_cul_lum_89 = map(lambda star: math.log10(star), smc_cul_lum_89)
smc_lbol_89 = map(lambda star: math.log10(star), smc_lbol_89)

smc_imf_91 = map(lambda star: 10**star.logimfweight, smc_91)
smc_lbol_91 = map(lambda star: 10**star.loglbol, smc_91)
smc_cul_lum_91 = []
# Make it cumulative
for value in smc_lbol_91:
    tmp = []
    for j, val in enumerate(smc_lbol_91):
        if val >= value:
        # Select imf values that correspond to app. lbol values
            tmp.append(smc_imf_91[j])
    smc_cul_lum_91.append(sum(tmp))
smc_cul_lum_91 = map(lambda star: math.log10(star), smc_cul_lum_91)
smc_lbol_91 = map(lambda star: math.log10(star), smc_lbol_91)

z10_imf_87 = map(lambda star: 10**star.logimfweight, z10_87)
z10_lbol_87 = map(lambda star: 10**star.loglbol, z10_87)
z10_cul_lum_87 = []
# Make it cumulative
for value in z10_lbol_87:
    tmp = []
    for j, val in enumerate(z10_lbol_87):
        if val >= value:
        # Select imf values that correspond to app. lbol values
            tmp.append(z10_imf_87[j])
    z10_cul_lum_87.append(sum(tmp))
z10_cul_lum_87 = map(lambda star: math.log10(star), z10_cul_lum_87)
z10_lbol_87 = map(lambda star: math.log10(star), z10_lbol_87)

z10_imf_89 = map(lambda star: 10**star.logimfweight, z10_89)
z10_lbol_89 = map(lambda star: 10**star.loglbol, z10_89)
z10_cul_lum_89 = []
# Make it cumulative
for value in z10_lbol_89:
    tmp = []
    for j, val in enumerate(z10_lbol_89):
        if val >= value:
        # Select imf values that correspond to app. lbol values
            tmp.append(z10_imf_89[j])
    z10_cul_lum_89.append(sum(tmp))
z10_cul_lum_89 = map(lambda star: math.log10(star), z10_cul_lum_89)
z10_lbol_89 = map(lambda star: math.log10(star), z10_lbol_89)

z10_imf_91 = map(lambda star: 10**star.logimfweight, z10_91)
z10_lbol_91 = map(lambda star: 10**star.loglbol, z10_91)
z10_cul_lum_91 = []
# Make it cumulative
for value in z10_lbol_91:
    tmp = []
    for j, val in enumerate(z10_lbol_91):
        if val >= value:
        # Select imf values that correspond to app. lbol values
            tmp.append(z10_imf_91[j])
    z10_cul_lum_91.append(sum(tmp))
z10_cul_lum_91 = map(lambda star: math.log10(star), z10_cul_lum_91)
z10_lbol_91 = map(lambda star: math.log10(star), z10_lbol_91)

x = 0.07
y = 0.95

ax1 = plt.subplot(1, 3, 1)
ax1.plot(z10_lbol_87, z10_cul_lum_87, linestyle='-', color='#83c460', linewidth=3,
         label = 'log(age) = 8.7')
ax1.plot(z10_lbol_89, z10_cul_lum_89, linestyle='-', color='#424242', linewidth=3,
         label = 'log(age) = 8.9')
ax1.plot(z10_lbol_91, z10_cul_lum_91, linestyle='-', color='#ff536d', linewidth=3,
         label = 'log(age) = 9.1')
ax1.text(x, y, r'$0.1Z_{sol}$', transform=ax1.transAxes, verticalalignment='top', fontsize=14)
plt.ylim(-6.0, -3.4)
plt.xlim(3.2, 4.2)
plt.ylabel('log $N(>L)/N_{tot}$', fontsize=16)
plt.xlabel(r'log $L_{bol}$', fontsize=20, labelpad=20)

ax2 = plt.subplot(1, 3, 2)
ax2.plot(smc_lbol_87, smc_cul_lum_87, linestyle='-', color='#83c460', linewidth=3,
         label = 'log(age) = 8.7')
ax2.plot(smc_lbol_89, smc_cul_lum_89, linestyle='-', color='#424242', linewidth=3,
         label = 'log(age) = 8.9')
ax2.plot(smc_lbol_91, smc_cul_lum_91, linestyle='-', color='#ff536d', linewidth=3,
         label = 'log(age) = 9.1')
ax2.text(x, y, r'$0.2Z_{sol}$', transform=ax2.transAxes, verticalalignment='top', fontsize=14)
plt.ylim(-6.0, -3.4)
plt.xlim(3.2, 4.2)
plt.xlabel(r'log $L_{bol}$', fontsize=20, labelpad=20)

ax3 = plt.subplot(1, 3, 3)
#ax6 = ax3.twiny()
#ax6.plot(sol_agb_87, sol_cul_lum_87,color='#ffffff',alpha=0)
ax3.plot(sol_lbol_87, sol_cul_lum_87, linestyle='-', color='#83c460', linewidth=3,
         label = 'log(age) = 8.7')
ax3.plot(sol_lbol_89, sol_cul_lum_89, linestyle='-', color='#424242', linewidth=3,
         label = 'log(age) = 8.9')
ax3.plot(sol_lbol_91, sol_cul_lum_91, linestyle='-', color='#ff536d', linewidth=3,
         label = 'log(age) = 9.1')
ax3.text(x, y, r'Z$_{sol}$', transform=ax3.transAxes, verticalalignment='top', fontsize=14)
plt.ylim(-6.0, -3.4)
plt.xlim(3.2, 4.2)
plt.xlabel(r'log $L_{bol}$', fontsize=20, labelpad=20)

plt.legend(loc="lower left", frameon=False, fontsize=10)
plt.tight_layout()
plt.show()
