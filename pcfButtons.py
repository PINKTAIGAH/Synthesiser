"""
Class that will poll and control all pcf button inputs.
"""

from DAH import PCF8574

class pcfButtons(object):
	def __init__(self, pcfAddress):
		#===============================================================
		# Constructor that will define general parameters 
		
		self.pcf= PCF8574(address= pcfAddress)
		self.waveformList= [f'sine', f'square', f'sawtooth', f'triangle', f'noise']
		self.octaveList= [0,1,2,3,4,5,6,7,8]
		self.waveformButton=0
		self.octaveButton= 1
		self.modeChangeButton= 1
		self.waveformIndex= 0
		self.octaveIndex= 0
		
	def checkButtonState(self, button):
		#===============================================================
		# Return bool representing the state of the desired button
		
		buttonState= False
		if self.pcf.digitalRead(button) ==0:
			buttonState= True 
		
		return buttonState
		
	def increaseIndex(self, buttonState, i):
		#===============================================================
		# Return increase index if desired button is pressed. ie: bool is true
		
		if buttonState== True:
			i++1
		return i
		
	def checkIndexOverflow(self, i, buttonList):
		#===============================================================
		# Check if index of button if out of bounds for corresponding list.
		# Set index to zero if true
		
		if i==len(buttonList):
            i=0
		return i 
		
	def waveformButtonState(self):
		#===============================================================
		# Return current button index for waveform button
		
		buttonState= self.checkButtonState(self.waveformButton)
		self.increaseIndex(buttonState, self.waveformIndex)
		self.checkIndexOverflow(self.waveformIndex, self.waveformList)
		
		return self.waveformIndex
		
	def octaveButtonState(self):
		#===============================================================
		# Return current button index for octave button
		
		buttonState= self.checkButtonState(self.octaveButton)
		self.increaseIndex(buttonState, self.octaveIndex)
		self.checkIndexOverflow(self.octaveIndex, self.octaveList)
		
		return self.octaveIndex
		
	def modeChangeButtonState(self):
		#===============================================================
		# Return current button state for modeChange button
		
		buttonState= self.checkButtonState(self.modeChangeButton)
		
		return buttonState
