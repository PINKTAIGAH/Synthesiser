"""
Class that allows for the control of a 16x2 lcd screen via raspberry pi's
GPIO pins 
"""
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

class lcd(object):
	def __init__(self):
		#===============================================================
		# Constructor that defines lcd parameters and GPIO pin connections
		# and initialises the lcd method
		
		self.lcdRows= 2
		self.lcdColumns= 16
		self.lcdRS = digitalio.DigitalInOut(board.D22)
		self.lcdEN = digitalio.DigitalInOut(board.D17)
		self.lcdD4 = digitalio.DigitalInOut(board.D25)
		self.lcdD5 = digitalio.DigitalInOut(board.D24)
		self.lcdD6 = digitalio.DigitalInOut(board.D23)
		self.lcdD7 = digitalio.DigitalInOut(board.D18)
		self.lcd = characterlcd.Character_LCD_Mono(self.lcdRS, self.lcdEN,\
				self.lcdD4, self.lcdD5, self.lcdD6, self.lcdD7,\
				self.lcdColumns, self.lcdRows)
		self.lcd.clear()		
		
	def write(self, line1= None, line2= None):
		#===============================================================
		# Write input strings to lcd screen
		self.lcd.message= f'{line1}\n{line2}'
		
	def clear(self):
		#===============================================================
		# Clear all writng from lcd screen 
		self.lcd.clear()

		
		
