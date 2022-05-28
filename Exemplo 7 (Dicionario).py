brasil=[]
estado={}
for a in range(0,3):
    estado['UF']=input('Unidade Federativa: ')
    estado['Sigla']=input('Sigla do Estado: ')
    brasil.append(estado.copy())
for b in brasil:
    for c in b.values():
        print(f'{c}', end=' ')
    print()
