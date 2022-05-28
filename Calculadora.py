## Aqui tera todos os tipos de contas possiveis.
from sympy import *

#Integral

def integ():
    x, y, z = symbols('x y z')
    integral = input("Digite a função a ser integrada em relação a X:\n")

    integral_resolvida = integrate(integral,x)

    print(f"A integral de {integral} é: {integral_resolvida}")

#Derivada

def deriv():
    x, y, z = symbols('x y z')
    derivada = input("Digite a função a ser derivada em relação a X:\n")

    derivada_resolvida = diff(derivada, x)

    print(f"A derivada de {derivada} é: {derivada_resolvida}")


def bhaskara():
    print("#Calculo de Bhaskara#\nPara realizar o calculo de Bhaskara informe A B C respectivamente")
    a = float(input("A >>> "))
    b = float(input("B >>> "))
    c = float(input("C >>> "))

    delta = b ** 2 - 4 * a * c

    if delta >= 0:
        x1 = (-b + delta ** 0.5) / 2 * a
        x2 = (-b - delta ** 0.5) / 2 * a
        print(f"As raizes da equação são: X1 = {x1} e X2 = {x2}")
    if delta < 0:
        delta = -delta
        x1R = (-b) / 2 * a
        x1I = (delta ** 0.5) / 2 * a
        x2R = (-b) / 2 * a
        x2I = - (delta ** 0.5) / 2 * a
        if x1R == 0 or x2R == 0:
            print(f"As raizes da equação são: X1 = {x1I}i e X2 = {x2I}i")
        else:
            print(f"As raizes da equação são: X1 = {x1R} + {x1I}i e X2 = {x2R} {x2I}i")


print("\nEscolha a operação que deseja realizar:\n")
print("A) Integral\nB) Derivada\nC) Bhaskara\n")

escolha = input(">>> ")

if (escolha.upper() == "A"):
    integ()
if (escolha.upper() == "B"):
    deriv()
if (escolha.upper() == "C"):
    bhaskara()