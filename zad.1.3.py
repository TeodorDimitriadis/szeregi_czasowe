import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def D(dane):
    a = 0
    for i in range(1,len(dane)):
        a += (dane[i] - dane[i-1])**2
    return a/(len(dane)-1)

wektor_normalny = np.random.normal(0,1,2000)
D_0 = D(wektor_normalny)

wektor_permutacji = []
for i in range(500):
    permutacja = np.random.permutation(wektor_normalny)
    wektor_permutacji.append(D(permutacja))

plt.hist(wektor_permutacji, bins=20)
plt.axline((D_0,0),(D_0,50),color = 'red')
plt.grid()
plt.show()