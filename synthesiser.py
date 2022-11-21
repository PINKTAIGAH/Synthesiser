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
		
		self.adcChip= 1
		self.mcpChip= 0
		self.pcfAddress= 0x38
		self.mcpAddress= 0x20
		self.bitSize= 16
		self.channelSize= 2
		self.outputRate= 44100
		self.octaves= (0,1,2,3,4,5,6,7,8)
		self.waveforms= ('sine', 'square', 'triangle', 'sawtooth', 'noise')
		self.frequencies=  np.loadtxt(f'frequencies.txt', delimiter= ',',\
							comments= '#')
		
		# Initialize pygame mixer module
		pygame.mixer.init(frequency= OUTPUT_RATE, channels= self.channelSize, size= -self.bitSize)
		
		# Initialize all classes for circuit I/O
		adc= adcSignal(self.adcChip)
		pcf= pcfButtons(self.pcfAddress)
		mcp= mcpButtons(self.mcpChip, self.mcpAddress)
		lcd= LCD1602()
		
	def convertBufferToSound(self):
		#===============================================================
		# Convert and return a buffer object into a pygame sound object
		
		self.note= pygame.mixer.Sound(buffer= self.buffer) 
	
	def createNoteArray(self):
		#===============================================================
		# Convert an array of sound objects dictaded by button presses
		
		 
		
 
		 
