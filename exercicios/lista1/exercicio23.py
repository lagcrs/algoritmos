from math import pi

raio = float(input('Digite raio do circulo: '))

perimetro = 2 * pi * raio
area = pi * raio ** 2

print(f'Perimetro: {perimetro:.2f}')
print(f'Area: {area:.2f}')