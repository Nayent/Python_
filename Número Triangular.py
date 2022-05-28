#Verifique se o número do usuario é triangular!!

num=int(input("Digite um numero: "))

a = 0

for i in range(num):
    if (i*(i+1)*(i+2))== num:
        a+=1
        break
if a==1:
    print(f"O numero {num} é triangular pois {i} x {i + 1} x {i + 2} = {num}")
else:
    print(f"O numero {num} não é triangular!")