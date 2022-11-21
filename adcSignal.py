"""
Class that will poll and return the analog signals from a MCP 3208 chip
"""
from DAH import MCP3208

class adcSignal(object):
	def __init__(self, chip):
		#===============================================================
		# Constructor that will ddefine general parametes of the adcSignal
		# class
		
		self.adc= MCP3208(chip= chip)
		self.channelSize= 3
		self.maxPitch= 2000
		self.maxLenght= 5
		
	def adcPollRaw(self):
		#===============================================================
		# Poll relevant channels and add them to a list (with index corresponding
		# to channels). The following defines what parameter each channel represents 
		# Channel 0 => pitch
		# Channel 1 => volume
		# Channel 2 => lenght
		
		self.adcReadingRaw= [self.adc.analogReadFloat(channel= i) for i in range(self.channelSize)]
	
	def convertRawToData(self):
		#===============================================================
		# Convert raw adc readings into desired parameters
		
		self.adcReading= self.adcReadingRaw
		
		self.adcReading[0]= int(self.adcReadingRaw[0]*self.maxPitch)
		self.adcReading[1]= round(self.adcReadingRaw[1], 2)
		self.adcReading[2]= round(self.adcReading[2]*self.maxLenght, 2)
		
	def adcPoll(self):
		#===============================================================
		# Return converted parameter data from the adc signals
		
		self.adcPollRaw()
		self.convertRawToData()
		
		return self.adcReading
		

		
		
		
		

