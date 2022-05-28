import matplotlib.pyplot as mp

meses = ['Janeiro','Fevereiro','Março','Abril',' Maio','Junho','Julho','Agosto','Setembro','outubro','Novembro','Dezembro']
valores = [8453,9875,5468,1548,3658,6987,6589,8974,4568,1238,9856,2356]

mp.stem(meses,valores, use_line_collection=True)
mp.ylim(0,11000)
mp.title("Faturamento Obtido em 2019")
mp.ylabel("Faturamento")
mp.xlabel("Meses")
mp.show()