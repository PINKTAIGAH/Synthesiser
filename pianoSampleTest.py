"""
Script to test playing .wav files using pygame
"""
import pygame, time
import numpy as np

pygame.mixer.init(frequency= 44100, channels= 2, size= -16)

note= pygame.mixer.Sound('pianoSamples/A2.wav')
note.play()

time.sleep(2)
