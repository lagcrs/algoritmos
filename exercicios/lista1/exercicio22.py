import math

base = float(input('Digite a base: '))
altura = float(input('Digite a altura: '))

perimetro = 2 * (base + altura)
area = base * altura
diagonal = math.sqrt(base ** 2 + altura**2)

print('Perimetro: ', perimetro)
print('Area: ', area)
print('Diagonal: ', diagonal)