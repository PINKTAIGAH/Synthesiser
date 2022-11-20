"""
Script to test the functionality of the generateSignal class and speed of 
signal generation
"""
from generateSignal import generateSignal
import matplotlib.pyplot as plt
import time

def main():
	# Initiate class
	generate= generateSignal()
	
	# Generate buffer and compute how long it takes
	t_i= time.time()
	sine_buffer= generate.createBuffer(20, 0.5, 1, f'sine')
	t_f= time.time()
	print(t_f-t_i)
	
	# Generate a second buffer and plot both
	triangle_buffer= generate.createBuffer(0.5, 0.25, 1, f'triangle')
	plt.plot(sine_buffer.T[0][:])
	plt.plot(triangle_buffer.T[0][:])
	plt.show()

if __name__== '__main__':
	main()
