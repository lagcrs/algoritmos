ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite ano atual: '))

idade = ano_atual - ano_nascimento

if ano_nascimento < 0 or ano_nascimento > ano_atual:
    print('Ano de nascimento digitado é inválido...')
else:
    print('Sua idade: ', idade)