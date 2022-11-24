import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file1= np.loadtxt('1000HzVariation.txt', delimiter= ',')
file2= np.loadtxt('2000HzVariation.txt', delimiter= ',')
file3= np.loadtxt('4000HzVariation.txt', delimiter= ',')
file4= np.loadtxt('8000HzVariation.txt', delimiter= ',')

variations= np.array([file1, file2, file3, file4])

columnVals= [1000, 2000, 4000, 8000]
columns= ['1000Hz','2000HZ','4000Hz','8000Hz']
df= pd.DataFrame(variations.T, columns= columns)
#df.to_csv('frequencyVariations.txt', index= False)


std= df.std().to_numpy()

plt.plot(columnVals, std)
plt.show()


