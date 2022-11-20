"""
Script to test the functionality of the lcd class
"""
from lcd import lcd
from time import sleep

def main():
	line1= f'This is'
	line2= f'a test message'
	
	n= lcd()	# Initialize lcd class
	n.write(line1, line2)	# Write message to lcd
	sleep(5)
	n.clear()	#Clear screen

if __name__== '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
	
