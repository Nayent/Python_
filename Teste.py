import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

tau = []

dados = pd.read_excel(r'C:\Users\guino\OneDrive\Área de Trabalho\Book1.xlsx')

dados1 = pd.DataFrame(dados).to_numpy()

dados1 = dados1[:,2:4]

print(dados1)
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.scatter(dados1[:,0], dados1[:,1], edgecolors='k', marker='.')
plt.show()

for i in range(0,len(dados1[:,0])):
    taus = -(dados1[i, 0] / (np.log(1 - dados1[i, 1]/2.04)))
    tau.append(taus)

Tau = pd.DataFrame(tau)

print(Tau.mean())
