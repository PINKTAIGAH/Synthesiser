"""
Test script for mcpButtons class.
"""
from mcpButtons import mcpButtons
from time import sleep

def main_poly():
	#===================================================================
	# Test poly press functionality
	
	while True:
		mcp= mcpButtons(0, 0x20)
		print(mcp.mcpButtonsPressedPoly())
		sleep(0.2)
		
def main_single():
	#===================================================================
	# Test single press functionality
	
	while True:
		mcp= mcpButtons(0, 0x20)
		print(mcp.mcpButtonsPressedSingle())
		sleep(0.2)
		
if __name__== '__main__':
	main_single()
