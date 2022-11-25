"""
Script to test the functionality of the generateSignal class and speed of 
signal generation
"""
from generateSignal import generateSignal
import matplotlib.pyplot as plt
import time

def main():
	# Initiate class
	generate= generateSignal(2, 44100)
	
	# Generate buffer and compute how long it takes
	t_i= time.time()
	sine_buffer= generate.createBuffer(50, 0.5, 1, f'sine')
	t_f= time.time()
	print(t_f-t_i)
	
	# Generate a second buffer and plot both
	triangle_buffer= generate.createBuffer(4, 0.25, 1, f'triangle')
	plt.plot(sine_buffer.T[0][:], label= 'sine wave @ 50 Hz')
	plt.plot(triangle_buffer.T[0][:], label= 'triangle wave @ 4 Hz')
	plt.xlabel('time, t (s)')
	plt.ylabel('Frequency, f (Hz)')
	plt.title('Generated waves with Hanning window applied')
	plt.legend()
	plt.show()

if __name__== '__main__':
	main()
