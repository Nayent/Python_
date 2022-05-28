def tri (x,y,z):
    if (x+y)>=z and (x+z)>=y and (y+z)>=x:
        return 1
    else:
        return 0

a=int(input("Digite um valor: "))
b=int(input("Digite um valor: "))
c=int(input("Digite um valor: "))

if tri(a,b,c)==1:
    print("É um triangulo")
else:
    print('Não é um triangulo')
