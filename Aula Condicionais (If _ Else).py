n=int(input('Qual a sua idade? '))

if n>=18:
    print("Maior de idade")
    if n==18:
        print('18 Anos')
    else:
        print('Mais que 18 anos')
else:
    print("Menor de idade")
