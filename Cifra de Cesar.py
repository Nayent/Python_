alf='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

codigo=input("Digite o codigo a ser encriptado: \n")
chave=int(input("Escolha o valor da chave: "))

cript=''

codigo=codigo.upper()

for i in codigo:
    if i in alf:
        a=alf.find(i)
        a=a+chave
        while a>len(alf):
            a=a-len(alf)
        cript=cript+alf[a]
    else:
        cript=cript+i

print("O texto criptografado é: \n{}".format(cript))



