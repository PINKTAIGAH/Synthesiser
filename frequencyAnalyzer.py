import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file1= np.loadtxt('frequencyVariationData/250HzVariation.txt', delimiter= ',')
file2= np.loadtxt('frequencyVariationData/500HzVariation.txt', delimiter= ',')
file3= np.loadtxt('frequencyVariationData/750HzVariation.txt', delimiter= ',')
file4= np.loadtxt('frequencyVariationData/1000HzVariation.txt', delimiter= ',')
file5= np.loadtxt('frequencyVariationData/2000HzVariation.txt', delimiter= ',')
file6= np.loadtxt('frequencyVariationData/3000HzVariation.txt', delimiter= ',')
file7= np.loadtxt('frequencyVariationData/4000HzVariation.txt', delimiter= ',')
file8= np.loadtxt('frequencyVariationData/5000HzVariation.txt', delimiter= ',')
file9= np.loadtxt('frequencyVariationData/6000HzVariation.txt', delimiter= ',')
file10= np.loadtxt('frequencyVariationData/7000HzVariation.txt', delimiter= ',')
file11= np.loadtxt('frequencyVariationData/8000HzVariation.txt', delimiter= ',')

variations= np.array([file1,file2,file3,file4,file5,file6,file7,file8,file9,file10,file11,])

columnVals= [250,500,750,1000,2000,3000,4000,5000,6000,7000,8000]
columns= ['250Hz','500Hz','750Hz','1000Hz','2000Hz','3000Hz','4000Hz','5000Hz','6000Hz','7000Hz','8000Hz']
df= pd.DataFrame(variations.T, columns= columns)
df.to_csv('frequencyVariations.txt', index= False)


std= df.std().to_numpy()
df_std= pd.DataFrame([std,columnVals], columns= columns)
df_std.to_csv('stdVariationData.txt', index= False)
plt.scatter(columnVals, std, marker= 'x')
plt.xlabel('Max frequency, f (Hz)')
plt.ylabel('Standard deviation $\sigma$ (Hz)')
plt.title('Standard deviation of pitch parameter fluctuations ')
plt.show()


