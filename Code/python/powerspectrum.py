'''
Graphs the power Spectrum
give the power.dat file as sys.argv[1]
'''

import sys
import numpy as np
import pylab as py

filename = str(sys.argv[1])
data = np.loadtxt(filename)

x = data[:,0]

y = data[:,3]
y = y*x**3

py.figure()
py.loglog(x,y,'-b')
py.xlabel('$k$')
py.ylabel('$k^{3}P(k)$')
py.title('Cutoff Power Spectrum at z=500')
py.show()

