"""
Script to collect and plot frequency signal radings form a MCP3208 chip
"""

import numpy as np
from adcSignal import adcSignal
from time import sleep

def main():
	frequencyArray= []
	print(f'0/5 data sets completed')
	for i in range(5):
		singleRun= []
		while True:
			adc= adcSignal(1)
			singleRun.append(adc.adcPoll()[0])
			sleep(0.01)
			if len(singleRun) >2500:
				break
		frequencyArray.append(singleRun)
		print(f'{i+1}/5 data sets completed')
	frequencyArray= np.array(frequencyArray)
	np.savetxt('frequencyVariationData/8000HzVariation.txt', frequencyArray, delimiter= ',')
if __name__== '__main__':
	main()
