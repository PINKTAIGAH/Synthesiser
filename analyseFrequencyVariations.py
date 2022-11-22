"""
Script that will analysse and plot frequency variation datasets
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.statistics as statistics

def main():
	1000Hz=np.load('1000HzVariation.txt', delimiter= ',')
	2000Hz=np.load('1000HzVariation.txt', delimiter= ',')
	4000Hz=np.load('1000HzVariation.txt', delimiter= ',')
	8000Hz=np.load('1000HzVariation.txt', delimiter= ',')
	
	
	
