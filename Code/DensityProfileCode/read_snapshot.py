#### Read Snapshot and create density profile ####
# change hubble parameter and omegamatter in the code as needed
# The file output is all in physical units

import math
import numpy as np
import sys
import pylab as py 
import time

#### Variables that can change with simulation 
h      = 0.72
omegam = 0.27


if len(sys.argv) != 7:
    print '\nusage: ./snapshot2profile <infile> <outfile> <xc> <yc> <zc> <virrad>\n'
    print sys.argv
    sys.exit(2)

infile    = open(sys.argv[1],"rb")
name      = str(sys.argv[1])
outfile   = open(sys.argv[2],"w")
xc        = float(sys.argv[3])
yc        = float(sys.argv[4])
zc        = float(sys.argv[5]) 

#### Begin header fortran read statement
dummy = np.fromfile(infile,dtype=np.int32,count=1)

# The following should add up to 256 bytes
npart     = np.fromfile(infile,dtype=np.int32,count=6)
mass      = np.fromfile(infile,dtype=np.float64,count=6)
a         = np.fromfile(infile,dtype=np.float64,count=1)
z         = np.fromfile(infile,dtype=np.float64,count=1)
virialrad = float(sys.argv[6]) / h * (1/(1+z))
flagsfr   = np.fromfile(infile,dtype=np.int32,count=1)
flagfeedb = np.fromfile(infile,dtype=np.int32,count=1)
nall      = np.fromfile(infile,dtype=np.int32,count=6)
unused    = np.fromfile(infile,dtype=np.int32,count=34)

#### End header fortran read statement
dummy = np.fromfile(infile,dtype=np.int32,count=1)

#### Begin positions fortran read statement
dummy = np.fromfile(infile,dtype=np.int32,count=1)

# Here we will assume that there are only particles of type 1 (x1000 to convert to parsecs/h)
positions = np.fromfile(infile,dtype=np.float32,count=npart[1]*3).reshape([npart[1],3])*1000

#### End positions fortran read statement
dummy = np.fromfile(infile,dtype=np.int32,count=1)

#### Creating Array of Radii
radius = np.sqrt((xc - positions[:,0])**2 + (yc - positions[:,1])**2 + (zc - positions[:,2])**2)

#### Binning Radii in logspace
bin        = np.logspace(-2.6,0.2,num=100)       #HARD CODED = BAD :(
hist, bins = np.histogram(radius,bins=bin)

center     = (bins[:-1]+bins[1:])/2
center     = center / h * (1/(1+z))                     #convert to physical units

density    = hist/(bins[1:]**3 - bins[:-1]**3)
density    = (density * mass[1]) / ((4./3.) * np.pi)   #units of solarmass / pc^3 * h^2 (comoving)
density    = density * h**2 * (1+z)**3                 # convert to physical units

error      = np.sqrt(hist)
errdensity = error/(bins[1:]**3 - bins[:-1]**3)
errdensity = (errdensity * mass[1]) / ((4./3.) * np.pi) #units of solarmass / pc^3 * h^2 (comoving)
errdensity = errdensity * h**2 * (1+z)**3

#### Plot virial radius
py.figure()
#py.plot([virialrad,virialrad],[1e-7,1e0],'-r',label='Rvir')

#### Plot Density Profile
py.loglog(center,density,'-b',label="density")
py.errorbar(center, density, yerr=errdensity)
py.xlabel(r'Radius ($pc$)')
py.ylabel(r'Density ([$M_{solar}$] [$pc^{-3}$])')
py.title("Density Profile of %s halo\nx=%.3f, y=%.3f, z=%.3f" %(name, xc, yc, zc))
py.legend(loc="best")
py.show()

#### Write data to outfile
outfile.write("Density Profile of %s halo\nx=%.3f, y=%.3f, z=%.3f\n" %(name, xc, yc, zc))
for i in range(len(center)):
    outfile.write('%.15f %.12f %.3f %.12f\n'%(center[i],density[i],virialrad,errdensity[i]))
   

'''
print radius.min()
print data[:,0].min(),data[:,0].max()
print data[:,1].min(),data[:,1].max()
print data[:,2].min(),data[:,2].max()

for i in range(10):
    print data[i], radius[i]
'''
