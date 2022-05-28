from random import randint
from time import sleep
comp=randint(0,5)
print('-=-'*19)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*19)
x=int(input('Em que numero eu pensei?  '))
print("Processando...")
sleep(2)
if comp==x:
    print('Parabens!! Você Acertou! ')
else:
    print(f'Errou, o numero que eu pensei foi o \033[35m{comp}')