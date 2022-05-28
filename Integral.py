from sympy import *

x, y ,z = symbols('x y z')

integral = input("Digite a função a ser integrada em relação a X:\n")

integral_resolvida = integrate(integral,x)

print(f"A integral de {integral} é: {integral_resolvida}")