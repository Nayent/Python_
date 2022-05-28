from sympy import *

x, y ,z = symbols('x y z')

derivada = input("Digite a função a ser derivada em relação a X:\n")

derivada_resolvida = diff(derivada,x)

print(f"A derivada de {derivada} é: {derivada_resolvida}")