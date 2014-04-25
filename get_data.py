'''
Match up the Barmby and Caldwell data tables in order recreate figs 7 from b+j 2012
Matching data from Table 1 from Barmby + Jalilian 2012 and Table 1 from Caldwell et al 2009
'''

from astropy.table import Table

caldwell = Table.read('caldwell2011_vogcs.xml')
barmby = Table.read('barmby2012.txt', format='ascii.commented_header')


# Find matching objects
with open("matched_catalog.txt", "w") as f:
    for obj1 in barmby:
        for obj2 in caldwell:
            if obj1['name'] == obj2['col1'][0:4]:
                f.write('%5s' % obj1['name'] + '%10.3f' % obj1['ks'] + '%10.3f' % obj1['err5'] +
                        '%10.3f' % obj1['3.6l'] + '%10.3f' % obj1['err6'] + '%10.3f' % obj1['4.5l'] +
                        '%10.3f' % obj1['err7'] + '%10.3f' % obj2['col9'] + '%10.3f' % obj2['col10'] +
                        '%10.3f' % obj1['ebv'] + '%10.3f' % obj1['met'] + '\n')

