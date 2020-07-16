import sys
import numpy as np
import pylab as py

file1    = str(sys.argv[1])
halonum  = int(sys.argv[2])
outfile  = open(sys.argv[3],'w')
data     = np.loadtxt(file1)

hosthalo = data[halonum-1,0]
host     = data[:,1]
data     = data[host == hosthalo]

for i in range(len(data)):
    outfile.write('%.14f %f %f %f %f\n'%(data[i,3],data[i,5]*1000,data[i,6]*1000,data[i,7]*1000, data[i,11]*1000)) 




print ('%lf' %hosthalo) 
