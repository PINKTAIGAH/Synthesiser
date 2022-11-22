"""
Script that will run synthesiser class in custom mode. Define the parameters of
sound generated from each available key
"""
from synthesiser import synthesiser

def main():
	synth= synthesiser()
	synth.runCustom()

if __name__== '__main__':
    try :
        main()
    except KeyboardInterrupt:
        pass
    finally:
	    #lcd.clear()
	    print(f'Program Terminated')

