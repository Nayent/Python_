import math

x=[]
y=[]

def fx(x,y):

    fx = (math.sin(x*y)) #Equacao Aqui

    return fx

a=int(input("Deseja o Metodo de Runge-Kutta em qual ordem?  "))

h = float(input("Digite o valor de h: "))
x.append(float(input("Digite o valor inicial de x: ")))
y.append(float(input("Digite o valor inicial de y: ")))
final = float(input("Digite o valor final do x: "))

if a == 2:

    i = x[0]
    j = 0
    while i < final:
        x.append(x[j] + h)
        y.append(y[j] + (h / 2) * (fx(x[j],y[j]) + fx(x[j]+h,y[j]+h*fx(x[j],y[j]))))
        i = i + h
        j += 1

if a == 3:

    i = x[0]
    j = 0
    while i < final:
        x.append(x[j] + h)
        k1 = h * fx(x[j], y[j])
        k2 = h * fx(x[j] + h / 2, y[j] + k1 / 2)
        k3 = h * fx(x[j] + (3 * h) / 4, y[j] + (3 * k2) / 4)
        y.append(y[j] + (2 / 9) * k1 + (1 / 3) * k2 + (4 / 9) * k3)
        i = i + h
        j += 1
#        print(k1, k2, k3, k4)

if a == 4:

    i = x[0]
    j = 0
    while i < final:
        x.append(x[j] + h)
        k1 = h * fx(x[j], y[j])
        k2 = h * fx(x[j] + h / 2, y[j] + k1 / 2)
        k3 = h * fx(x[j] + h / 2, y[j] + k2 / 2)
        k4 = h * fx(x[j] + h, y[j] + k3)
        y.append(y[j] + (1/6)*(k1 + 2 * k2 + 2 * k3 + k4))
        i = i + h
        j += 1
#        print(k1, k2, k3, k4)


print(f"O valor de y({x[j]}) é {y[j]}")