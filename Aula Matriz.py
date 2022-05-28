#lin=int(input("Tamanho de linhas da matriz: "))
#col=int(input("Tamanho de colunas da matriz: "))
#mat=[[0 for x in range(col)] for y in range(lin)]

#for i in range(lin):
#    print(mat[i])


matriz=[[1,2,3],[4,5,6],[7,8,9]]

matriz[0][1]=200

for i in range(0,3):
    print(matriz[i])

print('\n',matriz)