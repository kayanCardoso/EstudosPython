# Recalculando o salario

sal = float(input('Informe o sálario atual   R$'))
if sal > 1250:
    porcent = (sal * 10) / 100
    print(f'Seu salário vai ser de {sal + porcent:.2f}')
else:
    porcent = (sal * 15) / 100
    print(f'Seu salario vai ser de {sal + porcent:.2f}')
