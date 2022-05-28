pessoas = {'Nome':'Nomura', 'Sexo':'M', 'Idade':'19'}
del pessoas['Sexo']
pessoas['Nome']='Guilherme'
pessoas['Peso']='66.6'
for k,v in pessoas.items():
    print(f"{k} = {v}")

print(pessoas.keys())
print(pessoas.values())