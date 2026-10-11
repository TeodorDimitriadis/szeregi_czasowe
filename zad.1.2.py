import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def D(dane):
    a = 0
    for i in range(1,len(dane)):
        a += (dane[i] - dane[i-1])**2
    return a/(len(dane)-1)


wektor_D = []
for i in range(500):
    wektor_normalny = np.random.normal(0,1,2000)
    wektor_D.append(D(wektor_normalny))

plt.hist(wektor_D,bins=20)
plt.grid()
plt.show()
print(np.mean(wektor_D))