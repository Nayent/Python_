import math

def fx(x):
    fx = (x+2)**3#função aqui
    return fx

x=[]
y=[]
par=[]
impar=[]

h = float(input("Digite o valor de h: "))
x.append(float(input("digite o primeiro valor de x: ")))
xn=float(input("Digite o ultimo valor de x: "))

n=(xn-x[0])/h
n=int(n+1)

for i in range(1,n):
    x.append(x[i-1]+h)

for i in range(0,n):
    y.append(fx(x[i]))

somapar=0
somaimpar=0

for i in range(1,n-1):
    if i%2==0:
        par.append(y[i])
        somapar+=y[i]
    else:
        impar.append(y[i])
        somaimpar+=y[i]

integral = (h/3) * (y[0] + y[n-1] + 4*(somaimpar) + 2*(somapar))

print(integral)
