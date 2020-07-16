'''
graphmultipleDPdata.py
Graphs density profiles of multiple data output files from read_snapshot.py (up to 4)
USAGE:

For the legend to be correct enter the halos in descending size in the command line

There are 7 command line options
First 4 are options for data outputs from read_snapshot (enter zero if you do not want to graph)
The fith, sixth and seventh are options for axes enter anything other than a number between 0-2 for the proper usage
'''

import sys
import numpy as np
import pylab as py
import scipy
from scipy import *
from scipy import optimize 

#### Hardcoded Parameters
h           = 0.72
omegamatter = 0.27
rhocrit     = 2.775e-7 * h**2                 # units are solar masses/parsec^3
rhomat      = rhocrit * omegamatter


if len(sys.argv) != 8:
    print '\nusage: ./data2profile <infile1> <infile2> <infile3> <infile4> <densityopt> <radiusopt> <errorbars>\n'
    #print the options
    print sys.argv
    sys.exit(2)

#### Read in command line arguments
infile    = []
name      = []
xyzvalues = []
positions = []
center    = []
hist      = []
virialrad = []
errhist   = []

for i in range(4):
    n = i+1 
    if str(sys.argv[n]) != '0':
        infile.append(open(sys.argv[n],"r"))
        name.append(infile[i].readline())
        xyzvalues.append(infile[i].readline())
        positions.append(np.loadtxt(infile[i]))
    	center.append(positions[i][:,0])
    	hist.append(positions[i][:,1])
    	virialrad.append(positions[i][0,2])
        errhist.append(positions[i][:,3])

#### Reading in options
densityopt  = int(sys.argv[5])
radiusopt   = int(sys.argv[6])
errors      = int(sys.argv[7])

#### Plot Virial Rad
#py.plot([virialrad,virialrad],[1e-7,1e0],'-r',label='Rvir')


#### Options
#================================================================================

##Changing Radius
if radiusopt == 1:
    py.xlabel(r'$r/r_{vir}$') 
    for i in range(4):
        n = i+1
    	if str(sys.argv[n]) != '0':
        	center[i] = center[i] / virialrad[i]
elif radiusopt != 0:
    print 'radiusopt must either be one (over Rvir) or zero (nothing)'
    sys.exit(2)
else:
    py.xlabel(r'Radius ($pc$)') 

##Changing the Density
if densityopt == 1:
    py.ylabel(r'$\rho/\rho_{crit,0}$')         
    for i in range(4):
        n = i+1
        if str(sys.argv[n]) != '0':
            hist[i]    = hist[i]    / rhocrit
            errhist[i] = errhist[i] / rhocrit
elif densityopt == 2:
    py.ylabel(r'$\rho/\rho_{matter,0}$')     
    for i in range(4):
        n=i+1
        if str(sys.argv[n]) != '0':
            hist[i]    = hist[i]    / rhomat
            errhist[i] = errhist[i] / rhomat 
elif densityopt == 0:
    py.ylabel(r'Density ([$M_{solar}$] [$pc^{-3}$])')    
else:
    print 'densityopt must be 0 (nothing) 1 (over rhocrit) or 2 (over rhomat)'
    sys.exit(2)

#==================================================================================

#### Create Plot

## Adding error bars
if errors == 0:
    if str(sys.argv[1]) != '0':
        py.loglog(center[0],hist[0],'-b',label="1st Largest")
    if str(sys.argv[2]) != '0':
        py.loglog(center[1],hist[1],'-r',label="2nd Largest")
    if str(sys.argv[3]) != '0':
        py.loglog(center[2],hist[2],'-g',label="3rd Largest")
    if str(sys.argv[4]) != '0':
        py.loglog(center[3],hist[3],'-y',label="4th Largest")    
elif errors == 1:
    py.loglog()
    for i in range(4):
        n = i+1
    	if str(sys.argv[n]) != '0':
            py.errorbar(center[i], hist[i], yerr=errhist[i],label='halo #%d'%n)
else:
    print 'error must either be one (error bars) or zero (no error bars)'
    sys.exit(2)

py.title('Comparison of Density Profiles')
py.legend(loc="best")
py.show()
 
