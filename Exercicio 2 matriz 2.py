#Crie uma matrix 2x3 e faça a transposta dela (Resultando em uma 3x2)
lin=2
col=3
mat=[[0 for x in range(col)] for y in range(lin)]
met=[[0 for x in range(lin)] for y in range(col)]

for i in range(lin):
    for j in range(col):
        mat[i][j]=int(input(f"digite o valor da linha {i+1} e coluna {j+1}: "))
        met[j][i]=mat[i][j]

for i in range(col):
    print(met[i])
