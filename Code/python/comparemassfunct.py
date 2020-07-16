'''
Compares two M^2 mass functions 

'''

import sys
import numpy as np
import pylab as py


#AHF 512: First Argument 
file1 = str(sys.argv[1])
data=np.loadtxt(file1)

host2 = data[:,1]
data4 = data[host2 == 0]

Mamiga2= data4[:,3]

x2=np.log10(Mamiga2)
total2=len(x2)
hist2, bins2=np.histogram(x2,bins=30)
center2 = (bins2[:-1]+bins2[1:])/2
step2=(center2[1]-center2[0])/2
hist2=(10**center2*(hist2+0.0)/step2)/(30**3) 


#============================================================


#AHF 256: Second Argument
file2 = str(sys.argv[2])
data2=np.loadtxt(file2)

host = data2[:,1]
data3 = data2[host == -1]
Mamiga=data3[:,3]

x=np.log10(Mamiga)
total=len(x)
hist, bins=np.histogram(x,bins=30)
center = (bins[:-1]+bins[1:])/2
step=(center[1]-center[0])/2
hist=(10**center*(hist+0.0)/step)/(30**3)

#=============================================================

#Graphing Stuff
py.figure()
py.semilogy(center,hist*1.1,'ob',label="AMIGA256")
py.semilogy(center2,hist2,'or',label="AMIGA512")
py.xlabel("log M ($M_{solar}$)")
py.ylabel(r"$M^2$ $\frac{dn}{dM}$ $\frac{1}{V}$ [$M_{solar}$][$pc^{-3}$]")
py.title("Mass Function at z=31 ([$M_{solar}$][$pc^{-3}$] as a function of log M)")
py.legend(loc="best")
py.show()

