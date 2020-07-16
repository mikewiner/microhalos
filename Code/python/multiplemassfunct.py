import sys
import numpy as np
import pylab as py

#AHF
file1   = str(sys.argv[1])
file2   = str(sys.argv[2])
file3   = str(sys.argv[3])
#file4   = str(sys.argv[4])
data    = np.loadtxt(file1)
data2   = np.loadtxt(file2)
data3   = np.loadtxt(file3)
#data4   = np.loadtxt(file4)
#outfile = open(sys.argv[5],"w")

#===================================

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


#===================================

#AHF 2
host2   = data2[:,1]
data22  = data2[host2 == 0]
Mamiga2 = data22[:,3]

x2            = np.log10(Mamiga2)
hist2, bins2  = np.histogram(x2,bins=30)
errhist2      = np.sqrt(hist2)
center2       = (bins2[:-1]+bins2[1:])/2
step2         = (center2[2]-center2[1])
hist2         = (hist2+0.0)/step2/(30**3)
errhist2      = (errhist2)/step2/(30**3) 


#======================================

#AHF 3

#no sub
host3   = data3[:,1]
data33  = data3[host3 == 0]
Mamiga3 = data33[:,3]

x3            = np.log10(Mamiga3)
hist3, bins3  = np.histogram(x3,bins=30)
errhist3      = np.sqrt(hist3)
center3       = (bins3[:-1]+bins3[1:])/2
step3         = (center3[2]-center3[1])
hist3         = (hist3+0.0)/step3/(30**3)
errhist3      = (errhist3)/step3/(30**3)


#======================================
#AHF 4
'''
#nosub 
host4   = data4[:,1]
data44  = data4[host4 == 0]
Mamiga4 = data44[:,3]

x4            = np.log10(Mamiga4)
hist4, bins4  = np.histogram(x4,bins=30)
errhist4      = np.sqrt(hist4)
center4       = (bins4[:-1]+bins4[1:])/2
step4         = (center4[2]-center4[1])
hist4         = (hist4+0.0)/step4/(30**3)
errhist4      = (errhist4)/step4/(30**3)
'''
#==========================================


py.figure(figsize=(15,10))
py.loglog()#(10**center,hist,'ob',label="AMIGA")
py.errorbar(10**center,hist,fmt='bo--',markersize=10,alpha=0.8, yerr=errhist,label='enhancement at 5x10$^{8}$')
py.errorbar(10**center2,hist2,fmt='r^--',markersize=10,alpha=0.8,yerr=errhist2,label = 'enhancement at 1x10$^{8}$')
py.errorbar(10**center3,hist3,fmt='gd--',markersize=10,alpha=0.8,yerr=errhist3,label = 'No enhancement')
#py.errorbar(10**center4,hist4,fmt='ms--',markersize=10,alpha=0.8,yerr=errhist4,label = 'cutoff at 2x10$^{6}$')
#py.xlim(3e-11,1e-6)
#py.ylim(1e-4,10)
py.xlabel("Mass ($M_{solar}$)", fontsize=22)
py.ylabel(r"$M$ $\frac{dn}{dM}$ [$pc^{-3}$]",fontsize=22)
py.title("Mass Function at z=31: Comparison between Enhancements",fontsize=22)
py.legend(loc="best")
py.savefig('enhancementcomparison.png',dpi=200)
py.show()

#for i in range(len(center)):
#    outfile.write(' %.15f %.5f %.5f\n'%(10**center[i],hist[i],errhist[i]))  
