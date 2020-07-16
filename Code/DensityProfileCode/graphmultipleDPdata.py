'''
graphmultipleDPdata.py 

Graphs multiple data output files from read_snapshot.py (up to 4)
USAGE:
There are 7 command line options
First 4 are options for data outputs from read_snapshot (enter zero if you do not want to graph)
The fith, sixth and seventh are options for axes enter anything other than a number for the proper usage 

Options for axes labels are at the bottom and can be commented and uncommented

'''
import sys
import numpy as np
import pylab as py

if len(sys.argv) != 8:
    print '\nusage: ./data2profile <infile1> <infile2> <infile3> <infile4> <densityopt> <radiusopt> <fix>\n'
    print sys.argv
    sys.exit(2)

#### Read in command line arguements
print str(sys.argv[1])

## Read infile1
if str(sys.argv[1]) != '0':
    infile1    = open(sys.argv[1],"r")
    name1      = infile1.readline()
    xyzvalues1 = infile1.readline()
    data1      = np.loadtxt(infile1)
    center1     = data1[:,0]
    hist1       = data1[:,1]
    virialrad1  = data1[0,2]

## Read infile2
if str(sys.argv[2]) != '0':
    infile2    = open(sys.argv[2],"r")
    name2      = infile2.readline()
    xyzvalues2 = infile2.readline()
    data2      = np.loadtxt(infile2)
    center2     = data2[:,0]
    hist2       = data2[:,1]
    virialrad2  = data2[0,2]

## Read infile3
if str(sys.argv[3]) != '0':
    infile3    = open(sys.argv[3],"r")
    name3      = infile3.readline()
    xyzvalues3 = infile3.readline()
    data3      = np.loadtxt(infile3)
    center3     = data3[:,0]
    hist3       = data3[:,1]
    virialrad3  = data3[0,2]
 
## Read infile4
if str(sys.argv[4]) != '0':
    infile4    = open(sys.argv[4],"r")
    name4      = infile4.readline()
    xyzvalues4 = infile4.readline()
    data4      = np.loadtxt(infile4)
    center4     = data4[:,0]
    hist4       = data4[:,1]
    virialrad4  = data4[0,2]

#### Reading in options
densityopt  = int(sys.argv[5])
radiusopt   = int(sys.argv[6])
fix         = int(sys.argv[7])

#### Plot Virial Rad
#py.plot([virialrad,virialrad],[1e-7,1e0],'-r',label='Rvir')


#### Options
#===============================================================================

##Fixing the density
if fix == 1:
    if str(sys.argv[1]) != '0':
        hist1 = hist1 / ( (4./3.) * np.pi )**2
    if str(sys.argv[2]) != '0':
        hist2 = hist2 / ( (4./3.) * np.pi )**2
    if str(sys.argv[3]) != '0':
        hist3 = hist3 / ( (4./3.) * np.pi )**2
    if str(sys.argv[4]) != '0':
        hist4 = hist4 / ( (4./3.) * np.pi )**2
elif fix != 0:
    print 'fix must either be one (to fix) or zero (to not)'
    sys.exit(2)

##Changing Radius
if radiusopt == 1:
    if str(sys.argv[1]) != '0':
        center1 = center1 / virialrad1
    if str(sys.argv[2]) != '0':
        center2 = center2 / virialrad2
    if str(sys.argv[3]) != '0':
        center3 = center3 / virialrad3
    if str(sys.argv[4]) != '0':
        center4 = center4 / virialrad4
elif radiusopt == 2:
    ah = 32.*0.72
    if str(sys.argv[1]) != '0':
        center1 = center1 / ah
    if str(sys.argv[2]) != '0':
        center2 = center2 / ah
    if str(sys.argv[3]) != '0':
        center3 = center3 / ah
    if str(sys.argv[4]) != '0':
        center4 = center4 / ah
elif radiusopt != 0:
    print 'radiusopt must either be one (over Rvir) two (Rphysical) or zero (nothing)'
    sys.exit(2)

##Changing the Density
if densityopt == 1:
    rhocrit = 1.43845e-7
    if str(sys.argv[1]) != '0':
        hist1 = hist1 / rhocrit
    if str(sys.argv[2]) != '0':
        hist2 = hist2 / rhocrit
    if str(sys.argv[3]) != '0':
        hist3 = hist3 / rhocrit
    if str(sys.argv[4]) != '0':
        hist4 = hist4 / rhocrit

elif densityopt == 2:
    rhomat  = 8.325e-8
    if str(sys.argv[1]) != '0':
        hist1 = hist1 / rhomat
    if str(sys.argv[2]) != '0':
        hist2 = hist2 / rhomat
    if str(sys.argv[3]) != '0':
        hist3 = hist3 / rhomat
    if str(sys.argv[4]) != '0':
        hist4 = hist4 / rhomat
elif densityopt != 0:
    print 'densityopt must be 0 (nothing) 1 (over rhocrit) or 2 (over rhomat)'
    sys.exit(2)

#==================================================================================

#### Create Plot
if str(sys.argv[1]) != '0':
    py.loglog(center1,hist1,'-b',label="4thLargest")
if str(sys.argv[2]) != '0':
    py.loglog(center2,hist2,'-r',label="3rdLargest")
if str(sys.argv[3]) != '0':
    py.loglog(center3,hist3,'-g',label="2ndLargest")
if str(sys.argv[4]) != '0':
    py.loglog(center4,hist4,'-y',label="Largest")


#py.xlabel(r'Radius ($pc$)')
#py.ylabel(r'Density ([$M_{solar}$] [$pc^{-3}$])')

py.xlabel(r'$r_{physical}$')

#py.xlabel(r'$r/r_{vir}$')
py.ylabel(r'$\rho/\rho_{crit}$')

#py.xlim(xmax=111)
#py.xlim(xmin=0.04)
#py.ylim(ymax=10000)
#py.ylim(ymin=10)

py.title('Comparison of Density Profiles\nThe four 2nd largest halos across all cuts')
py.legend(loc="best")
py.show()
