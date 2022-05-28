#Crie um programa que verifique se há o nome silva no nome digitado
txt=input('Digite seu nome completo: ').strip().lower()
tt=txt.split()
a=0
for i in range(len(tt)):
    if tt[i]=='silva':
        a+=1
        break
if a>0:
    print('Há silva no seu nome')
else:
    print("Não há silva no seu nome")