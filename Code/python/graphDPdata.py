'''
Plot standard Density profile tabulated data
'''


import sys
import numpy as np
import pylab as py

if len(sys.argv) != 2:
    print '\nusage: ./data2profile <infile(data)>\n'
    print sys.argv
    sys.exit(2)

filename = str(sys.argv[1])
data     = np.loadtxt(filename)
 
name      = str(data[0]) + str(data[1])
center    = data[2:,0]
hist      = data[2:,1]
#virialrad = data[2,3]

#py.plot([virialrad,virialrad],[1e-7,1e0],'-r',label='Rvir')
py.loglog(center,hist,'-b',label="density")
py.xlabel(r'Radius ($pc$)')
py.ylabel(r'Density ([$M_{solar}$] [$pc^{cubed}$])')
py.title("%s\n%s" %(name, xyzvalues))
py.legend(loc="best")
py.show()
