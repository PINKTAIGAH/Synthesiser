"""
Script to collect and plot frequency signal radings form a MCP3208 chip
"""

import numpy as np
from adcSignal import adcSignal
from time import sleep

def main():
	frequencyArray= []
	while True:
		adc= adcSignal(1)
		frequencyArray.append(adc.adcPoll()[0])
		sleep(0.01)
		if len(frequencyArray) >5000:
			break
	frequencyArray= np.array([frequencyArray])
	np.savetxt('frequencyVariation.txt', frequencyArray, delimiter= ',')
	print(frequencyArray.size)
if __name__== '__main__':
	main()
