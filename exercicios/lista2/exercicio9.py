salario_bruto = float(input('Digite salário bruto: '))
valor_prestacao = float(input('Digite valor da prestação: '))

if valor_prestacao <= salario_bruto * 0.3:
    print('Empréstimo aceito')
else:
    print('Empréstimo negado')