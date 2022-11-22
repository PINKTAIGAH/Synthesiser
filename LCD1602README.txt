#--------------------------------------

# The wiring for the LCD is as follows:
# 1 : GND					 - GROUND
# 2 : 5V					 - 5V
# 3 : Contrast (0-5V)        - 5V + 4KOhm potentiometer
# 4 : RS (Register Select)	 - GPIO 22
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe		 - GPIO 17
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4			 - GPIO 25
# 12: Data Bit 5			 - GPIO 24
# 13: Data Bit 6			 - GPIO 23
# 14: Data Bit 7			 - GPIO 18
# 15: LCD Backlight +5V 	 - 5V + 4KOhm potentiometer
# 16: LCD Backlight GND		 - GROUND
