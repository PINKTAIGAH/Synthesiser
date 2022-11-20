"""
Script to test the functionality of the lcd class
"""
from LCD1602 import LCD1602
from time import sleep

def main():
	line1= f'This is'
	line2= f'a test message'
	
	lcd= LCD1602()	# Initialize lcd class
	lcd.write(line1, line2)	# Write message to lcd
	sleep(5)
	lcd.clear()	#Clear screen

if __name__== '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
	
