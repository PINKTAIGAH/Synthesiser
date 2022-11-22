"""
Class that will run main code loops for a sythesisers by taking inputs
from a circuit and output sounds.
"""
from adcSignal import adcSignal
from pcfButtons import pcfButtons
from mcpButtons import mcpButtons
from LCD1602 import LCD1602
from generateSignal import generateSignal
import numpy as np
from time import sleep
import pygame

class synthesiser(object):
	def __init__(self):
		#===============================================================
		# Constructor that will define general parameters for synthesiser
		
		self.volume=0.5
		self.length= 0.3
		self.adcChip= 1
		self.mcpChip= 0
		self.pcfAddress= 0x38
		self.mcpAddress= 0x20
		self.bitSize= 16
		self.channelSize= 2
		self.outputRate= 44100
		self.octaveIndex= 0
		self.waveformIndex= 0
		self.octaves= (0,1,2,3,4,5,6,7,8)
		self.waveforms= ('sine', 'square', 'triangle', 'sawtooth', 'noise')
		self.frequencies=  np.loadtxt(f'frequencies.txt', delimiter= ',',\
							comments= '#')
		
		# Initialize pygame mixer module
		pygame.mixer.init(frequency= self.outputRate, channels= self.channelSize, size= -self.bitSize)
		
		# Initialize all classes for circuit I/O
		self.waveGenerator= generateSignal(self.channelSize, self.outputRate)
		self.adc= adcSignal(self.adcChip)
		self.pcf= pcfButtons(self.pcfAddress)
		self.mcp= mcpButtons(self.mcpChip, self.mcpAddress)
		self.lcd= LCD1602()
		
	def convertBufferToSound(self):
		#===============================================================
		# Convert and return a buffer object into a pygame sound object
		
		self.soundArray= [pygame.mixer.Sound(buffer=self.bufferArray[i]) for i in range(len(self.bufferArray))]
	
	def createBufferArray(self):
		#===============================================================
		# Create an array of buffer objects for all notes to be played
		
		self.bufferArray= [self.waveGenerator.createBuffer(self.frequencies[self.octaveIndex][i],\
				self.volume,self.length, self.waveforms[self.waveformIndex]) \
				for i in self.keysPressed]
	
	def createSoundArray(self):
		#===============================================================
		# Create an array of sound objects for all notes to be played
		
		self.createBufferArray()
		self.convertBufferToSound()
		
	def playSoundArray(self):
		#===============================================================
		# Play on system all sound objects in array
		
		for i, individualSound in enumerate (self.soundArray):
			individualSound.play()

	def lcdPrintPiano(self):
		#===============================================================
		# Print current state of synthesiser to lcd screen for 'Piano mode'
		
		line1= f'Wave : {self.waveforms[self.waveformIndex]}     '
		line2= f'\nOctave: {self.octaveIndex}'
		self.lcd.write(line1, line2)
	
	def runPiano(self):
		#===============================================================
		# Main loop that will run the synthesyser
		running=True
		while running:
			self.keysPressed= self.mcp.buttonsPressedPoly()
			self.createSoundArray()
			self.playSoundArray()
			self.waveformIndex= self.pcf.waveformButtonState()
			self.octaveIndex= self.pcf.octaveButtonState()
			self.lcdPrintPiano()
			sleep(self.length)
			
		
		
