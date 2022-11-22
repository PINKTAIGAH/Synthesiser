"""
Class that will generate a sound buffer compatible with the 
pygame.mixer.Sound module. This class is also capable of creating a 
symetrical ASD envelope for the generated waveform.
"""

import numpy as np
import time
import scipy.signal as signal
import matplotlib.pyplot as plt

class generateSignal(object):
	
	def __init__(self, channelSize, outputRate):
		#===============================================================
		# Constructor what will define general relevant parameters for wave generation
		
		self.channelSize= channelSize
		self.outputRate= outputRate
		self.maxAmplitude= np.iinfo(np.int16).max
		self.attackDecayLengh= 5000
		
	def defineSignalParam(self, pitch, volume, duration):
		#===============================================================
		# Define wave specific parameters
		
		self.pitch= pitch
		self.volume= volume
		self.duration= duration
		self.totalSamples= int(self.outputRate*self.duration)
		self.amplitude= int(self.maxAmplitude*self.volume)
		
		# Array containing all time steps of generated wave
		self.t= np.linspace(0, self.duration, self.outputRate, endpoint=True)
		
		# Create empty array with dimentions of a pygame sound buffer
		self.emptyOutputBuffer= np.zeros((self.totalSamples, self.channelSize),\
										dtype= np.int16)
		
	def createHannWindow(self):
		#===============================================================
		# Funcion that will compute the left and right side of a hanning 
		# window
		
		window= np.hanning(2*self.attackDecayLengh)
		self.windowLeft= window[:self.attackDecayLengh-1]
		self.windowRight= window[self.attackDecayLengh:]
		
	def applyHannWindow(self, signalArray):
		#===============================================================
		# Apply hann window to any given signal array
		
		# Define index where the left and right window will be ap[plied
		leftWindowEnd= self.attackDecayLengh-1
		rightWindowStart= self.totalSamples-self.attackDecayLengh
		
		self.createHannWindow()
		
		# Apply hann window
		signalArray[:leftWindowEnd]= signalArray[:leftWindowEnd]* self.windowLeft
		signalArray[rightWindowStart:self.totalSamples]= signalArray[rightWindowStart:self.totalSamples]* self.windowRight
		
		return signalArray
		
	def fillOutputBuffer(self, signalArray):
		#===============================================================
		# Return a filled sound buffer with specified signalArray 
		
		outputBuffer= self.emptyOutputBuffer		
		channelInex= range(self.channelSize)
		
		# Assign wave amplitude by looping over all wave times and channels
		for i in range(self.totalSamples):
			outputBuffer[i][channelInex[0]]= outputBuffer[i][channelInex[1]]= signalArray[i]
		
		return outputBuffer
	
	def createSineBuffer(self):
		#===============================================================
		# Return sound buffer with sine wave
		
		signalArray= self.amplitude*signal.chirp(self.t, f0=self.pitch,\
						t1= self.totalSamples, f1= 3*self.pitch)
		signalArray= self.applyHannWindow(signalArray)
		outputBuffer= self.fillOutputBuffer(signalArray)
			
		return outputBuffer
		
	def createSquareBuffer(self):
		#===============================================================
		# Return sound buffer with square wave
		
		signalArray= self.amplitude*signal.sawtooth(2*np.pi*self.pitch*self.t)
		signalArray= self.applyHannWindow(signalArray)
		outputBuffer= self.fillOutputBuffer(signalArray)
		
		return outputBuffer
		
	def createTriangleBuffer(self):
		#===============================================================
		# Return sound buffer with triangle wave
		
		signalArray= self.amplitude*signal.sawtooth(2*np.pi*self.pitch*self.t, 0.5)
		signalArray= self.applyHannWindow(signalArray)
		outputBuffer= self.fillOutputBuffer(signalArray)
		
		return outputBuffer
		
	def createSawtoothBuffer(self):
		#===============================================================
		# Return sound buffer with sawtooth wave
		
		signalArray= self.amplitude*signal.sawtooth(2*np.pi*self.pitch*self.t)
		signalArray= self.applyHannWindow(signalArray)
		outputBuffer= self.fillOutputBuffer(signalArray)
		
		return outputBuffer	
	
	def createNoiseBuffer(self):
		#===============================================================
		# Return sound buffer with noise wave
		
		noiseMean= 0
		noiseStdDev= 0.5
		signalArray= self.amplitude*np.random.normal(noiseMean, noiseStdDev, self.totalSamples)
		signalArray= self.applyHannWindow(signalArray)
		outputBuffer= self.fillOutputBuffer(signalArray)
			
		return outputBuffer		
	
	def createBuffer(self, pitch, volume, duration, waveform= None):
		#===============================================================
		# Return sound buffer according to defined waveform type
		
		self.defineSignalParam(pitch, volume, duration)
		self.waveform= str(waveform)
		
		if self.waveform== f'sine':
			outputBuffer= self.createSineBuffer()
		elif self.waveform== f'square':
			outputBuffer= self.createSquareBuffer()
		elif self.waveform== f'triangle':
			outputBuffer= self.createTriangleBuffer()
		elif self.waveform== f'sawtooth':
			outputBuffer= self.createSawtoothBuffer()
		elif self.waveform== f'noise':
			outputBuffer= self.createNoiseBuffer()
		else:
			# Throw error if input waveform if not recognised by class
			raise Exception(f'Waveform type not recognised \nTry: \'sine\',' + \
						f'\'square\', \'triangle\', \'sawtooth\' or \'noise\'')

		return outputBuffer
