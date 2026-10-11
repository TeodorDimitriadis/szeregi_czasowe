import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def D(dane):
    a = 0
    for i in range(1,len(dane)):
        a += (dane[i] - dane[i-1])**2
    return a/(len(dane)-1)
      
dane = pd.read_csv('temperatury_90_dni.csv',parse_dates=['date'])

dane_temperatura = dane['temperature_C']

#1
srednia = np.mean(dane_temperatura)
mediana = np.median(dane_temperatura)
odchylenie_standardowe = np.std(dane_temperatura)
minimum = np.min(dane_temperatura)
maximum = np.max(dane_temperatura)
Q1 = np.quantile(dane_temperatura, 1/4)
Q3 = np.quantile(dane_temperatura, 3/4)

print('1')
print(srednia,mediana,odchylenie_standardowe,minimum,maximum,Q1,Q3)

plt.hist(dane_temperatura, bins=20, color = 'blue')
plt.grid()
plt.show()

plt.plot(dane_temperatura)
plt.grid()
plt.show()

#2
permutacje = np.random.permutation(dane_temperatura)

srednia = np.mean(permutacje)
mediana = np.median(permutacje)
odchylenie_standardowe = np.std(permutacje)
minimum = np.min(permutacje)
maximum = np.max(permutacje)
Q1 = np.quantile(permutacje, 1/4)
Q3 = np.quantile(permutacje, 3/4)

print('2')
print(srednia,mediana,odchylenie_standardowe,minimum,maximum,Q1,Q3)

plt.hist(permutacje, bins=20, color = 'blue')
plt.grid()
plt.show()

plt.plot(permutacje)
plt.grid()
plt.show()

print(D(dane_temperatura))
print(D(permutacje))

