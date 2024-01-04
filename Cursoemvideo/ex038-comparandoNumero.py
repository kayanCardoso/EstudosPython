n1 = int(input('Informe o primeiro valor: \n'))
n2 = int(input('Informe o segundo valor:\n'))

if n1 > n2:
    print(f'O primeiro valor é maior {n1} > {n2}')
elif n2 > n1:
    print(f'O segundo valor é maior {n2} > {n1}')
else:
    print(f'Os dois valores são iguais {n1} = {n2}')