from math import sqrt

num = float(input('Digite um numéro: '))

if num > 0:
    print('Raiz: ', sqrt(num))
elif num < 0:
    print('Quadrado do número: ', num ** 2)