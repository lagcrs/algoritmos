palavra = input("Digite uma palavra: ")

#concatenar
print(palavra + 'oi')

#tamanho
print(len(palavra))

#primeiro caractere
print(f'Primeiro caractere da string {palavra}: {palavra[0]}')

#ultimo caractere
print(f'Ultimo caractere da string {palavra}: {palavra[-1]}')

# 3 primeiros elementos da strings
print(f'Três primeiros elementos da string {palavra}: {palavra[:3]}')

# 3 ultimos elementos da strings
print(f'Três ultimos elementos da string {palavra}: {palavra[-3:]}')