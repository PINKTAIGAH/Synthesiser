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
	square_buffer= generate.createBuffer(10, 0.7, 1, f'square')
	t_f= time.time()
	print(t_f-t_i)
	
	# Generate a second buffer
	sawtooth_buffer= generate.createBuffer(4, 0.5, 1, f'triangle')

	# Generate a third buffer
	noise_buffer= generate.createBuffer(None, 0.05, 1, f'noise')
	
	# Plot the signals 
	plt.plot(generate.t, square_buffer.T[0][:], label= 'sine wave @ 50 Hz')
	plt.plot(generate.t, sawtooth_buffer.T[0][:], label= 'sawtooth wave @ 4 Hz')
	plt.plot(generate.t, noise_buffer.T[0][:], label='noise signal' )
	plt.xlabel('time, t (s)')
	plt.ylabel('Frequency, f (Hz)', x= 0.5)
	plt.title('Generated waves with Tukey window applied')
	plt.legend()
	plt.savefig("plots/waves_tukay_additional.png",bbox_inches='tight')
	plt.show()
	


if __name__== '__main__':
	main()
