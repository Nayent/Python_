equation = list(filter(None, (input("Digite a função para verificar a estabilidade: ")).strip().split(' ')))
equation = list(map(float, equation))

data = [equation,]

list_jk = []
jk_aux = 0
iteracoes = (len(equation) * 2) - 2

for itter in range(iteracoes):
    # Replicando as linhas e invertendo
    if itter % 2 == 0:
        data.append(list(reversed(data[itter])))
        # Adicionando novo valor de JK
        list_jk.append(data[itter][-1] / data[itter+1][-1])
    else:
        # Criando a nova linha a partir das 2 anteriores e o JK
        new_line = []
        for index in range(len(equation)-jk_aux-1):
            new_line.append(round(data[itter-1][index] - (data[itter][index] * list_jk[jk_aux]), 4))
        jk_aux += 1
        data.append(new_line)

# Mostrando os resultados obtidos
if all([abs(x) < 1 for x in list_jk]):
    print('O sistema é ESTÁVEL, sendo os seguintes valores para jk:\n\n', list_jk, '\n\nA tabela gerada é a seguinte:\n')
    for row in data[:-1]:
        print(row)
else:
    print('O sistema é INSTÁVEL, sendo os seguintes valores para jk:\n\n', list_jk, '\n\nA tabela gerada é a seguinte:\n')
    for row in data[:-1]:
        print(row)