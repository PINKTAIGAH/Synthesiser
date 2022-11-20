"""
Class that will poll and control all mcp button inputs.
"""

from DAH import MCP23S17

class mcpButton(object):
	
	def __init__(self, mcpChip, mcpAddress):
		#===============================================================
		# Constructor that defines genrral button parameters
		
		self.mcp= MCP12S17(chip= mcpChip, address= mcpAddress)
		self.mcpButtonNumber= 11
		
	def mcpButtonsPressedIndex(self):
		#===============================================================
		# Find index of mcp buttons being pressed
		
		self.index= []
		for i, _ in enumerate(self.mcpListStates):
			if self.mcpListStates[i]== 0:
				self.index.append(i)
		
	
	def mcpConvertBinaryToList(self):
		#===============================================================
		# Convert raw mcpBinaryState input to a list of individual button
		# states
		
		self.mcpListStates= [int(x) for x in str(self.mcpBinaryState)]
		self.mcpListStates= self.mcpListStates[::-1]
		
	def mcpPollButtonPoly(self):
		#===============================================================
		# Poll all mcp buttons and return binary string representing all
		# button states. If length binary is < number of buttons, fill
		# remaining with zeros
		
		self.mcpBinaryState= bin(self.mcp.portRead())[2:].zfill(self.mcpButtonNumber)
		
		
	def mcpButtonsPressedPoly(self):
		#===============================================================
		# Return indexes of all mcp buttons being pressed simultaneously
		
		self.mcpButtonsPressedPoly()
		self.mcpConvertBinaryToList()
		self.mcpButtonsPressedIndex()
		
		return self.index
		
	def mcpButtonPressedSingle(self):
		#===============================================================
		# Return index of a single mcp buttons being pressed. If no buttons
		# are being pressed or registered button press is not within range, 
		# return index of first button.
		
		self.mcpButtonsPressedPoly()
		self.mcpConvertBinaryToList()
		self.mcpButtonsPressedIndex()
		
		if len(self.index)==0 or self.index[0]> self.mcpButtonNumber-1:
			return 0
			
		else:
			return self.index[0]
			 
				
	
		 
	
	
