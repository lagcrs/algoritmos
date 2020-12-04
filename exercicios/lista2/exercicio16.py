sigla = input('Digite uma das siglas: SP / RJ / MG: ')

if sigla == 'RJ' or sigla == 'rj':
    print('Carioca')
elif sigla == 'SP' or sigla == 'sp':
    print('Paulista')
elif sigla == 'MG' or sigla == 'mg':
    print('Mineiro')
else:
    print('Outro estado')