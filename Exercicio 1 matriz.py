#Crie uma matriz de 3 linhas e 4 colunas com os valores digitados pelo usuario
lin=3
col=4
mat=[[0 for x in range(col)] for y in range(lin)]

for i in range(lin):
    for j in range(col):
        mat[i][j]=int(input("Digite um valor para a matriz: "))

for i in range(lin):
    print(mat[i])