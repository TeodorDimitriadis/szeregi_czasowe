import pandas as pd
import scipy.stats as sc
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv('zadanie1.csv')

for kolumna in {'godziny_nauki','sredni_wynik_testow'}:
    srednia = np.mean(dane[kolumna])
    odchylenie_standardowe = np.std(dane[kolumna])
    minimum = np.min(dane[kolumna])
    maksimum = np.max(dane[kolumna])
    wspolczynnik_pearsona = sc.pearsonr(dane['godziny_nauki'], dane['sredni_wynik_testow'])[0]
    print(f'{kolumna}: {srednia},{odchylenie_standardowe},{minimum},{maksimum},{wspolczynnik_pearsona}')

plt.scatter(dane['godziny_nauki'], dane['sredni_wynik_testow'])
plt.grid()
plt.show()