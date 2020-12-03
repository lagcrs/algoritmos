num = int(input('Digite um número de 3 algarismos: '))

centena = num // 100

if centena % 2 == 0:
    print(f'Primeiro número ({centena}) é par')
else:
    print(f'Primeiro número ({centena}) é ímpar')
