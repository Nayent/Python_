frase='Oba mai c ta bão?'
print(frase[10])                                      #Mostra o elemento de posição 10 da string
print(frase[10:16])                                   #Mostra os elementos de posição 10 a 15
print(frase[10:16:2])                                 #Mostra os elementos de posição 10 a 15 pulando de 2 em 2
len(frase)                                            #Tamanho da string
frase.count('o',0,13)                                 #Conta quantas vezes a letra 'o' aparece do 0 ao 12
frase.find('Oba')                                     #Mostra onde começou a frase requerida; caso não exista ela retorna o valor -1
'Oba' in frase                                        #Se existe True

frase.replace('Oba','Epa')                            #Substitui a palavra OBA po EPA
frase.upper()                                         #Deixa tudo maiusculo
frase.lower()                                         #Deixa tudo em minusculo
frase.capitalize()                                    #Deixa só a primeira letra maiuscula e o resto minusculo
frase.title()                                         #Deixa o letra do inicio de cada palvra em maiusculo
frase.strip()                                         #Remove os espaços do inicio e fim da string
frase.rstrip()                                        #Remove somente os espaços do lado direito
frase.lstrip()                                        #Remove somento os espaços do lado esquerdo

frase.split()                                         #Divide em varias string dentro de uma lista de acordo com cada espaço
' '.join(frase)                                       #Junta denovo os elementos e recria a string original


frase.startswith()                                    #Pergunta se a frase começa com determinada sintaxe


###
import re

padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
padraomelhorado = "[0-9]{4,5}[-][0-9]{4}"

retorno = re.search(padrao,StringQueQuerPesquisar)
print(retorno.group())

retornoParaTextoComMaisDeUmaCoisaProcurando = re.findall(padraomelhorado,StringQueQuerPesquisar)
###


