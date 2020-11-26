from math import sqrt

lado = float(input('Digite o lado do quadrado: '))

perimetro = 4 * lado
area = lado ** 2
diagonal = lado * sqrt(2)
print(f'Perimetro: {perimetro:.2f}\nArea: {area:.2f}\nDiagonal: {diagonal:.2f}')