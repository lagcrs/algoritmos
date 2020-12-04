nome = input('Digite nome: ')

if (nome[:4] == 'José' or nome[:4] == 'Jose' or nome[:4] == 'jose' or nome[:4] == 'josé' or nome[:4] == 'JOSÉ' or nome[:4] == 'JOSE') or nome == 'José':
    print(nome)
else:
    print('seu nome não é josé')