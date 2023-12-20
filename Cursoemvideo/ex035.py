# Analisando triangulo

l1 = float(input('Informe o primeiro lado : '))
l2 = float(input('Informe o segundo lado : '))
l3 = float(input('Informe o terceiro lado : '))

if l1 + l2 < l3:
    print('Não pode ser um triangulo!!')
elif l1 + l3 < l2:
    print('Não pode ser um triangulo!!')
elif l3 + l2 < l1:
    print('Não pode ser um triangulo!!')
else:
    print('Pode ser um triângulo!!')