nome = input('Digite nome: ')
genero = input('Digite genero (M/F): ')
idade = int(input('Digite idade: '))

if (genero == 'F' or genero == 'f') and idade < 25 :
    print(nome)
    print('ACEITA')
else:
    print('NAO ACEITA')