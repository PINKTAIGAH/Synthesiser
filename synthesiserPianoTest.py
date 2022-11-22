"""
Script that will run synthesiser class in piano mode. Map each note in an 
octave to a button.
"""
from synthesiser import synthesiser
from LCD1602 import LCD1602

lcd= LCD1602()

def main():
	synth= synthesiser()
	synth.runPiano()

if __name__== '__main__':
    try :
        main()
    except KeyboardInterrupt:
        pass
    finally:
	    lcd.clear()
	    print(f'Program Terminated')
