"""
Script to plot an hanning window of arbitrary length
"""
import numpy as np
import matplotlib.pyplot as plt

n= 10000
y= np.hanning(n)
plt.plot(y)
plt.xlabel('Length (a.u)')
plt.ylabel('Amplitude (a.u)')
plt.title('Hanning window of length 10000')
plt.show()