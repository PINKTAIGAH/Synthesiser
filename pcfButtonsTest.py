"""
Test script for pcfButtons class
"""
from pcfButtons import pcfButtons
from time import sleep
def main():
	octaves= (1,2,3,4,5,6,7)
	pcf= pcfButtons(0x38)
	while True:
		#print(pcf.waveformButtonState(), pcf.octaveButtonState(octaves))
		print(pcf.modeChangeButtonState())
		sleep(0.5)

if __name__== '__main__':
	main()
		


