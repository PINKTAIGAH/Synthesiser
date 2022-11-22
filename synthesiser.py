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
		self.keysAmount= 11
		self.keyParameters= [(0,1,1,1) for i in range(self.keysAmount)]
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
		
	def convertBufferToSoundPiano(self):
		#===============================================================
		# Convert and return a buffer object into a pygame sound object
		
		self.soundArray= [pygame.mixer.Sound(buffer=self.bufferArrayPiano[i]) for i in range(len(self.bufferArrayPiano))]
	
	def createBufferArrayPiano(self):
		#===============================================================
		# Create an array of buffer objects for all notes to be played
		
		self.bufferArrayPiano= [self.waveGenerator.createBuffer(self.frequencies[self.octaveIndex][i],\
				self.volume,self.length, self.waveforms[self.waveformIndex]) \
				for i in self.keysPressed]
	
	def createSoundArrayPiano(self):
		#===============================================================
		# Create an array of sound objects for all notes to be played
		
		self.createBufferArrayPiano()
		self.convertBufferToSoundPiano()
		
	def playSoundArray(self):
		#===============================================================
		# Play on system all sound objects in array
		
		for i, individualSound in enumerate (self.soundArray):
			individualSound.play()

	def writeCustomMessage(self):
		#===============================================================
		# Create strings that will be output to lcd screen during mode 
		# change loop
		
		self.line1= f'{self.adcParameters[0]} Hz, {self.adcParameters[2]} s      '
		self.line2= f'{self.adcParameters[1]}, {self.waveforms[self.waveformIndex]}    '
	
	def lcdPrintPiano(self):
		#===============================================================
		# Print current state of synthesiser to lcd screen for 'Piano mode'
		
		line1= f'Wave : {self.waveforms[self.waveformIndex]}     '
		line2= f'\nOctave: {self.octaveIndex}'
		self.lcd.write(line1, line2)
	
	def findActiveKeys(self):
		#===============================================================
		# Reduce keyParameters down only keys with acxtiver bindings and 
		# find indexes of keys with active bindings
		
		self.keyParameters= np.array(self.KeyParameters)
		self.activeKeyIndexes= np.where(self.KeyParameters != None)
		self.activeKeys= self.keyParameters[self.activeKeyIndexes]
		
	def convertBufferToSoundCustom(self):
		#===============================================================
		# Convert and return a buffer object into a pygame sound object
		
		self.soundArray= [pygame.mixer.Sound(buffer=self.bufferArrayCustom[i]) for i in range(len(self.bufferArrayCustom))]
	
	def createBufferArrayCustom(self):
		#===============================================================
		# Create an array of buffer objects for all notes to be played
		
		self.bufferArrayCustom= [self.waveGenerator.createBuffer(self.keyParameters[i][1],\
				self.keyParameters[i][2], self.keyParameters[i][3],\
				self.waveforms[self.keyParameters[i][0]]) for i in self.keysPressed]

	def createSoundArrayCustom(self):
		#===============================================================
		# Create an array of sound objects for all notes to be played
		
		self.createBufferArrayCustom()
		self.convertBufferToSoundCustom()
	
	def modeChangeLoop(self):
		#===============================================================
		# Loop that will find and find and return specified parameters from circuit
		
		sleep(1)
		running= True
		self.waveformIndex= 0
		while running:
			self.adcParameters= self.adc.adcPoll()
			self.waveformIndex= self.pcf.waveformButtonState()
			self.selectedKeyIndex= self.mcp.buttonsPressedSingle()
			self.writeCustomMessage()
			self.lcd.write(self.line1, self.line2)
			print(f'Selected button: {self.selectedKeyIndex}')
			
			click= self.pcf.modeChangeButtonState()
			if click== True:
				self.keyParameters[self.selectedKeyIndex]= (self.waveformIndex, *self.adcParameters)
				self.lcd.clear()
				break
			sleep(0.3)
				
	def runPiano(self):
		#===============================================================
		# Main loop that will run the synthesiser in piano mode
		running=True
		while running:
			self.keysPressed= self.mcp.buttonsPressedPoly()
			self.createSoundArrayPiano()
			self.playSoundArray()
			self.waveformIndex= self.pcf.waveformButtonState()
			self.octaveIndex= self.pcf.octaveButtonState()
			self.lcdPrintPiano()
			sleep(self.length)
			
	def runCustom(self):
		#===============================================================
		# Main loop that will run synthesiser in custumisable mode
		
		running= True
		while running:
			# Click variable defines if mode change button has been pressed
			# in this loop
			
			click= self.pcf.modeChangeButtonState()
			if click== True:
				self.modeChangeLoop()				
			
			self.keysPressed= self.mcp.buttonsPressedPoly()
			self.createSoundArrayCustom()
			self.playSoundArray()
			sleep(0.5)
			click= False
			sleep(0.5)
		
