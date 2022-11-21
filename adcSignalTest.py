"""
Test script for adcSignal class
"""
from adcSignal import adcSignal
from time import sleep

def main():
	while True:
		adc= adcSignal(1)
		print(adc.adcPoll())
		sleep(0.5)
	
if __name__== '__main__':
	main()
