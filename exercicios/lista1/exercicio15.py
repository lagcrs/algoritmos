cdu = int(input('Digite um numero de 3 dígitos: '))
c = cdu // 100
d = cdu % 100 // 10
u = cdu % 10
print(f'primeiro numero: {c}\nsegundo numero: {d}\nterceiro numero: {u}')