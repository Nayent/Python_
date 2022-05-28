import pandas as pd

notas = pd.read_csv("ratings.csv")

pd.set_option('display.max_rows', None)


notas.rating.plot(kind='hist')




