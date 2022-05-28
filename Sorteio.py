import random
n1=input('Digite o Primeiro nome: ')
n2=input('Digite o Segundo nome: ')
n3=input('Digite o terceiro nome: ')
n4=input('Digite o Quarto nome: ')
lista=[n1,n2,n3,n4]
x=random.choice(lista)                   #Sorteia aleatoriamente um elemento
print(f'O escolhido foi {x}')

random.shuffle(lista)                    #Embaralha a lista
print("A ordem será ")
print(lista)