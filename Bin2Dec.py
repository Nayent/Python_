while True:
    print('1) Binario para Decimal')
    print('2) Decimal para Binario')
    print('3) Sair')
    escolha = input('> ')

    if escolha == '1':
        t = True
        while t == True:
            cont = 0
            bin = input('Digite o numero binario desejado.\n> ')

            for i in bin:
                if i != '0' and i != '1':
                    cont += 1

            if cont == 0:
                break
            else:
                print('Valores invalidos, digite apenas os números 1 e 0\n')

        j = 0
        dec = 0
        for i in bin[::-1]:
            dec += int(i)*2**j
            j += 1
        print(f'O número binario {bin} corresponde ao número decimal {dec}\n')

    elif escolha == '2':
        dec = input('Digite o número decimal desejado.\n> ')
        bin = bin(int(dec))
        bin = str(bin).replace('0b', '')
        print(f'O número decimal {dec} corresponde ao número binario {bin}\n')

    elif escolha == '3':
        break;