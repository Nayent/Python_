print("1)Celcius\n2)Fahrenheit\n3)Kelvin\n")
a=int(input("Escolha a temperatura que vai ser transformada: "))
b=int(input("Escolha a temperatura que vai ser resultante: "))
c=float(input("Informe a temperatura: "))

if a==1:
    if b==2:
        result=c * 9 / 5 + 32
    if b==3:
        result=c + 273.15

if a==2:
    if b==1:
        result=(c - 32) * 5 / 9
    if b==3:
        result=(c - 32) * 5 / 9 + 273.15

if a==3:
    if b==1:
        result=c - 273.15
    if b==2:
        result=(c - 273.15) * 9 / 5 + 32

d=round(result,5)

if b==1:
    print(f"A temperatura em Celcius é igual a {d}ºC")
if b==2:
    print(f"A temperatura em Fahrenheit é igual a {d}ºF")
if b==3:
    print(f"A temperatura em Kelvin é igual a {d}K")