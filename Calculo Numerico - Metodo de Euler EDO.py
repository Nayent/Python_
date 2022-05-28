import math

y=[]
x=[]

def fx(x,y):

    fx = (y**2 - 1)/(x**2 +1) #Equacao Aqui

    return fx

h=float(input("Digite o valor de h: "))
x.append(float(input("Digite o valor inicial de x: ")))
y.append(float(input("Digite o valor inicial de y: ")))
final=float(input("Digite o valor final do x: "))

i= x[0]
j=0
while i < final:
    x.append(x[j]+h)
    y.append(y[j]+h*(fx(x[j],y[j])))
    print(f"{i}")
    i=i+h
    j+=1
    i = round(i, 5)


for i in range(0,len(y)):
    print("%.2f %.8f"% (x[i],y[i]))



