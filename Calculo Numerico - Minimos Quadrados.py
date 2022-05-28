import numpy as np
from sympy import *

x=[]
y=[]
xT=[]
fi=Matrix()
fiT=Matrix()
fx=Matrix()
theta=Matrix()


g=int(input("Digite o grau da sua função: "))
d=int(input("Digite a quantidade de valores a ser digitado: "))



for i in range(0,g+1):
    linha=[]
    for j in range(0,d):
        if i==(g):
            linha.append(float(1))
        else:
            linha.append(float(input(f"Digite o valor de X[{i+1}][{j+1}]: ")))
            y.append(float(input(f"Digite o valor de F(X[{i+1}][{j+1}]): ")))
    x.append(linha)

xT=[[0 for i in range(g+1)] for j in range(d)]

for i in range(g+1):
    for j in range(d):
        xT[j][i] = x[i][j]

for i in range(g+1):
    fi = fi.col_insert(i,Matrix(x[i]))
for i in range(d):
    fiT = fiT.col_insert(i,Matrix(xT[i]))


fx = fx.col_insert(0,Matrix(y))


theta = ((fiT*fi)**-1)*(fiT*fx)

print(theta)

'''newx = float(input("Digite o valor novo x: "))

result = theta[0]*newx + theta[1]

print(f"O valor final é: {result}")'''