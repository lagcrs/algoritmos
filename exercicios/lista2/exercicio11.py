num = int(input('Digite um número de 4 algarismos: '))

centena = num // 100

if centena % 4 == 0:
    print(f'({centena}) é multiplo de 4')
else:
    print(f'({centena}) não é multiplo de 4'')