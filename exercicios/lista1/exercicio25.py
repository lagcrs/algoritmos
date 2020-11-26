from math import sqrt

lado = float(input('Digite lado do paralelepípedo: '))
altura = float(input('Digite altura do paralelepípedo: '))
profundidade = float(input('Digite profundidade do paralelepípedo: '))

diagonal = sqrt( lado**2 + altura**2 + profundidade**2 )

print(f'Diagonal: {diagonal:.2f}')