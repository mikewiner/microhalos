'''
Create a M dn/dm mass function
and tabulate the data


sys.argv[1] is input file (AHF halos catalouge)
sys.argv[2] is output file (for tabulated data)

'''

import sys
import numpy as np
import pylab as py

#AHF
file1   = str(sys.argv[1])
data    = np.loadtxt(file1)
outfile = open(sys.argv[2],"w")

#No substructure!
host   = data[:,1]
data1  = data[host == 0]
Mamiga = data[:,3]

x          = np.log10(Mamiga)
hist, bins = np.histogram(x,bins=30)
errhist    = np.sqrt(hist)
center     = (bins[:-1]+bins[1:])/2
step       = (center[2]-center[1])
hist       = (hist+0.0)/step/(30**3)
errhist    = (errhist)/step/(30**3) 

py.figure()
py.loglog()#(10**center,hist,'ob',label="AMIGA")
py.errorbar(10**center,hist,yerr=errhist)

#Axis and Title Labels, Change as needed
py.xlabel("Mass ($M_{solar}$)")
py.ylabel(r"$M$ $\frac{dn}{dM}$ [$pc^{-3}$]")
py.title("Mass Function at z=31 ([$M_{solar}$][$pc^{-3}$] as a function of Mass)")
py.legend(loc="best")
py.show()

for i in range(len(center)):
    outfile.write(' %.15f %.5f %.5f\n'%(10**center[i],hist[i],errhist[i]))  
