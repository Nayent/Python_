import math
from sympy import *

y=[]
x=[]

def fx(x):

    fx=1/(x**2)#Equacao Aqui

    return fx

n=int(input("Digite o valor de N: "))
tam = n+1

x.append(float(input("Digite o primeiro valor de X: ")))
xn=(float(input("Digite o ultimo valor de X: ")))
h=(xn-x[0])/n

for i in range(1,tam):
    x.append(x[i-1]+h)

a=input("Possui a Equação(e) ou os valores de F(x)(f)?  ")

if a == 'e':
    for i in range(0,tam):
        y.append(fx(x[i]))
elif a == 'f':
    for i in range(0,tam):
        y.append(float(input(f"Digite o valor de y na posição {i}: ")))

soma = 0

for i in range(1,tam-1):
    soma+=y[i]
integral=(h/2)*((y[0]+y[tam-1])+ 2*(soma))

z = symbols('x')

k=float(input(f"Digite o valor maximo para a seguinte derivada segunda da função {fx(z).diff(z,2)}: "))

erro=((h**2)/12)*(x[tam-1]-x[0])*(fx(z).diff(z,2).subs(z,k))

print(integral)

print(f"O erro é de {erro}")
