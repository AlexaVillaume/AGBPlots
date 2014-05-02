'''
Make radius cut on LMC data and put it into sperate files as input for the plotting routine
Data from http://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-dd?catalog=sage_ar_irac_e1e2&mode=html&passproj&
'''
import geom_utils
'''
from astropy.table import Table
lmc_data = Table.read('LMC/spitzer.sage_cat_irac3886.tbl', format='ascii.commented_header')
print lmc_data.colnames
print len(lmc_data)
## Holy crap this takes a long time to run, optimize in some way?
for i, source in enumerate(lmc_data):
    if geom_utils.makeRadiusCut(float(source['ra']), float(source['dec']), 81.0, -60.8, math.pi) != 1:
        lmc_data.remove_row(i)
print len(lmc_data)
with open('lmc_irac1irac4.phot', 'w') as f:
    for source in lmc_data:
        if lmc_data['mag3_6'] != 'null' and lmc_data['mag8_0'] != 'null':
            f.write('%10s' % lmc_data['mag3_6'] + '%10s' % lmc_data['mag8_0'] + '\n')
with open('lmc_irac1twomj.phot', 'w') as f:
    for source in lmc_data:
        if lmc_data['mag3_6'] != 'null' and lmc_data['magj'] != 'null':
            f.write('%10s' % lmc_data['mag3_6'] + '%10s' % lmc_data['magj'] + '\n')
'''

# Make initial radius cut on the data

catalog = {}
with open('LMC/spitzer.sage_ar_irac_e1e225084.tbl', "r") as f:
    for object in f:
        object_cols = object.split()
        if object_cols[0][0] != '#':
            if object_cols[1] != 'null' and object_cols[2] != 'null':
                if geom_utils.makeRadiusCut(float(object_cols[1]),
                                            float(object_cols[2]), 81.0, -60.8, 10):
                    catalog[object_cols[0]] = object_cols

# Make cmd1 and cmd2 files
with open('lmc_irac1irac4.phot', 'w') as f:
    for obj, values in catalog.items():
        if values[5] != 'null' and values[7] != 'null':
            f.write('%10s' % values[5] + '%10s' % values[7] + '\n')

with open('lmc_irac1twomj.phot', 'w') as f:
    for obj, values in catalog.items():
        if values[3] != 'null' and values[5] != 'null':
            f.write('%10s' % values[3] + '%10s' % values[5] + '\n')
