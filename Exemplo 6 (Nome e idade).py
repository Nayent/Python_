num=list()
nop=list()
for i in range(0,5):
    nop.append(input("Qual o seu nome: "))
    nop.append(int(input("Qual a sua idade: ")))
    print('\n')
    num.append(nop[:])
    nop.clear()

for i in range(0,5):
    for j in range(0,1):
        print(f'{num[i][j]} tem {num[i][j+1]} anos')