import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\guino\OneDrive\Documentos\UTFPR\4º Periodo\Física Experimental 2\Relatório 4\Dados.xlsx')

pd.set_option('display.max_rows', 2230)
pd.set_option('display.max_columns', 20)

X = []
Y = []

for x,y in zip(df["CH1"],df["Unnamed: 2"]):
    # print(x,"  -  ",y)
    X.append(x)
    Y.append(y)

# plt.plot(X,Y)
plt.scatter(X,Y, s=2, edgecolors='k', color='b', label = 'Dados Obtidos')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2)
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.title("Dados obtidos através do osciloscópio")
plt.xlabel("Tempo(s)")
plt.ylabel("Tensão(V)")
plt.show()


