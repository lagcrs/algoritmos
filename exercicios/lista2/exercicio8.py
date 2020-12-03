num = int(input('Digite um numéro: '))

if num % 10 == 0:
    print('multiplo de 10')
elif num % 5 == 0:
    print('multiplo de 5')
elif num % 2 == 0:
    print('multiplo de 2')
else:
    print('não é multiplo de 10, 5 e 2')