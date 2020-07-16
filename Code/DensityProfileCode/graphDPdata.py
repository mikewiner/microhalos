import sys
import numpy as np
import pylab as py

if len(sys.argv) != 5:
    print '\nusage: ./data2profile <infile> <densityopt> <radiusopt> <fix>\n'
    print sys.argv
    sys.exit(2)

#### Read in command line arguements
infile      = open(sys.argv[1],"r")
densityopt  = int(sys.argv[2])
radiusopt   = int(sys.argv[3])
fix         = int(sys.argv[4])

#### Read input file
name        = infile.readline()
xyzvalues   = infile.readline()
data        = np.loadtxt(infile)

center    = data[:,0]
hist      = data[:,1]
virialrad = data[0,2]

#### Plot Virial Rad
py.plot([virialrad,virialrad],[1e-7,1e0],'-r',label='Rvir')

#### Options
#===============================================================================

##Fixing the density
if fix == 1:
    hist = hist / ( (4./3.) * np.pi )**2
elif fix != 0:
    print 'fix must either be one (to fix) or zero (to not)'
    sys.exit(2)

##Changing Radius
if radiusopt == 1:
    center = center / virialrad
elif radiusopt != 0:
    print 'radiusopt must either be one (over Rvir) or zero (nothing)'
    sys.exit(2)

##Changing the Density

#Over Critical Density today
if densityopt == 1:
    rhocrit = 1.43845e-7
    hist    = hist / rhocrit
elif densityopt == 2:
    rhomat  = 8.325e-8
    hist    = hist / rhomat
elif densityopt != 0:
    print 'densityopt must be 0 (nothing) 1 (over rhocrit) or 2 (over rhomat)'
    sys.exit(2)

#==================================================================================

#### Create Plot
py.loglog(center,hist,'-b',label="density")
py.xlabel(r'Radius ($pc$)')
py.ylabel(r'Density ([$M_{solar}$] [$pc^{-3}$])')
py.title("%s%s" %(name,xyzvalues))
py.legend(loc="best")
py.show()
