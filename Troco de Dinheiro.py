#Troco para o cliente

num=float(input("Digite o valor da compra: "))
cli=float(input("Digite o valor pago pelo cliente: "))

dif=cli-num
dif1=dif
a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;j=0;k=0;l=0

while dif>=100:
    a+=1
    dif = dif - 100
while dif>=50:
    b+= 1
    dif = dif - 50
while dif>=20:
    c+=1
    dif = dif - 20
while dif>=10:
    d+=1
    dif = dif - 10
while dif>=5:
    e+= 1
    dif = dif - 5
while dif>=2:
    f+= 1
    dif = dif - 2
while dif>=1:
    g+= 1
    dif = dif - 1
while dif>=0.5:
    h+= 1
    dif = dif - 0.5
while dif>=0.25:
    i+= 1
    dif = dif - 0.25
while dif>=0.10:
    j+= 1
    dif = dif - 0.10
while dif>=0.05:
    k+= 1
    dif = dif - 0.05
while dif>=0.01:
    l+= 1
    dif = dif - 0.01

print(f"\nO valor a ser devolvido é de R${dif1}, utilizando:\nNotas de R$100,00: {a}\nNotas de R$50,00:  {b}\nNotas de R$20,00:  {c}\nNotas de R$10,00:  {d}\nNotas de R$5,00:   {e}\nNotas de R$2,00:   {f}\nMoedas de R$1,00:  {g}\nMoedas de R$0,50:  {h}\nMoedas de R$0,25:  {i}\nMoedas de R$0,10:  {j}\nMoedas de R$0,05:  {k}\nMoedas de R$0,01:  {l}")