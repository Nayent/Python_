#Crie um programa que leia o nome de uma cidade e se começar com santo responda TRUE
txt=input('Escreva uma frase: ')
txt=txt.lower()
txt=txt.lstrip()
te=txt.split()
if te[0]=='santo':
    print('True')
else:
    print('False')
