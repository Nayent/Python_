print("#Numeros Primos\n")
a=0
while a>=0:
    a=int(input("Escolha um número: "))
    b=0
    for i in range(1,a,2):
        if a % i == 0:
            b+=1
    if b!=1 or a%2==0:
        print(f'O número {a} não é primo')
    elif b==1:
        print(f'O número {a} é primo')