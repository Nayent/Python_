for a in range(0,10):
    print(a,end=' ')
    if a<5:
        print('Menor que 5')
    else:
        print('Maior ou igual a 5')

print('\n')

quant=0

for b in "batata":
    print(b)
    if b == 'a':
        quant=quant+1

print('\nHá {} letras a'.format(quant))

numero=0

while numero<10:
    numero+=1
    print(numero)
    if numero==5:
        break

