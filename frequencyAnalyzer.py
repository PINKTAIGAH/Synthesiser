import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

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
variations= variations.reshape(-1, variations.shape[-1])

columnVals= [250,500,750,1000,2000,3000,4000,5000,6000,7000,8000]
frequencies= ['250Hz','500Hz','750Hz','1000Hz','2000Hz','3000Hz','4000Hz','5000Hz','6000Hz','7000Hz','8000Hz']
columns= []
for i,frequency in enumerate(frequencies):
    line= [f'{frequency} {j+1}' for j in range(5)]
    columns= columns+line

df= pd.DataFrame(variations.T, columns= columns)
df.to_csv('frequencyVariations.txt', index= False)

std= df.std().to_numpy()
df_std= pd.DataFrame([std], columns= columns)
mean_std= [df_std.iloc[:, 0:4].mean(axis=1), df_std.iloc[:, 5:9].mean(axis=1),\
         df_std.iloc[:, 10:14].mean(axis=1), df_std.iloc[:, 15:19].mean(axis=1),\
         df_std.iloc[:, 20:24].mean(axis=1), df_std.iloc[:, 25:29].mean(axis=1),\
         df_std.iloc[:, 30:34].mean(axis=1), df_std.iloc[:, 35:39].mean(axis=1),\
         df_std.iloc[:, 40:44].mean(axis=1), df_std.iloc[:, 45:49].mean(axis=1),\
         df_std.iloc[:, 50:54].mean(axis=1)]
mean_std= [x[0] for _, x in enumerate(mean_std)]

sem_std= [df_std.iloc[:, 0:4].sem(axis=1), df_std.iloc[:, 5:9].sem(axis=1),\
         df_std.iloc[:, 10:14].sem(axis=1), df_std.iloc[:, 15:19].sem(axis=1),\
         df_std.iloc[:, 20:24].sem(axis=1), df_std.iloc[:, 25:29].sem(axis=1),\
         df_std.iloc[:, 30:34].sem(axis=1), df_std.iloc[:, 35:39].sem(axis=1),\
         df_std.iloc[:, 40:44].sem(axis=1), df_std.iloc[:, 45:49].sem(axis=1),\
         df_std.iloc[:, 50:54].sem(axis=1)]
sem_std= [x[0] for _, x in enumerate(sem_std)]

df_data= pd.DataFrame( np.array([columnVals, mean_std, sem_std,]).T, columns= ['frequencies', 'mean of std', 'sem of std'], index= frequencies)
df_data.to_csv('stdVariationData.txt')

res= linregress(columnVals, mean_std)
residuals= np.subtract(np.array(mean_std), res.intercept+res.slope*np.array(columnVals))
print(np.array(mean_std))
print(res.intercept+res.slope*np.array(columnVals))
print(residuals)

plt.errorbar(columnVals, mean_std, yerr= sem_std, fmt= 'kx', ms= 7 , ecolor= 'k', label= 'measured')
plt.plot(columnVals, res.intercept+ res.slope*np.array(columnVals), label= 'predicted')
plt.xlabel('Max frequency, f (Hz)')
plt.ylabel('Standard deviation $\sigma$ (Hz)')
plt.title('Standard deviation of pitch parameter fluctuations ')
plt.legend()
plt.show()
plt.clf()

plt.errorbar(columnVals, residuals, yerr= sem_std, fmt= 'kx', ms= 7 , ecolor= 'k')
plt.axhline(0, c= 'k', linewidth= .5 )
plt.xlabel('Max frequency, f (Hz)')
plt.ylabel('Residual of standard deviation, (Hz)')
plt.title('Residuals of standard deviation of pitch parameter fluctuations ')
plt.show()

