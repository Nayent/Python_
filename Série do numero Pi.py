soma = 0
x = 0

for i in range(1,100000000):
    soma = soma + (1/(i**2))


x=(soma*6)**(1/2)

print(f"Soma {soma} e valor de pi: {x}")