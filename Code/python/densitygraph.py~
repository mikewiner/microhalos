'''
Visiualization of all the halo centers
sys.argv[1] is AHF halo catalogue

downward view parallel to z axis
'''

import sys
import numpy as np
import pylab as py

filename = str(sys.argv[1])
data = np.loadtxt(filename)

host = data[:,1]
data2 = data[host == 0]

x = data2[:,5]*1000
y = data2[:,6]*1000
z = data2[:,7]*1000

py.figure()
py.scatter(x,y,s=1,marker='.',color = 'b')
py.xlim(0,max(x))
py.ylim(0,max(y))
py.xlabel('Parsecs')
py.ylabel('Parsecs')
py.title('Downward view of halos in comoving box')
py.show()
