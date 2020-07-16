'''
M^2 mass function of AHF halo catalogue
'''

import sys
import numpy as np
import pylab as py

#AHF
file2 = str(sys.argv[1])
data2=np.loadtxt(file2)


#No substructure!
host = data2[:,1]
data3 = data2[host == 0]

Mamiga=data3[:,3]

x2=np.log10(Mamiga)
total2=len(x2)
hist2, bins2=np.histogram(x2,bins=30)
center2 = (bins2[:-1]+bins2[1:])/2
step2=(center2[1]-center2[0])/2
hist2=(10**center2*(hist2+0.0)/step2)/(30**3) 


py.figure()
py.loglog(10**center2,hist2,'ob',label="AHF")
py.xlabel("Mass ($M_{solar}$)")
py.ylabel(r"$M^2$ $\frac{dn}{dM}$ $\frac{1}{V}$ [$M_{solar}$][$pc^{-3}$]")
py.title("Mass Function at z=31 ([$M_{solar}$][$pc^{-3}$] as a function of Mass)")
py.legend(loc="best")
py.show()

