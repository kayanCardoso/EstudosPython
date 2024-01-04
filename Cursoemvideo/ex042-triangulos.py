n1 = float(input('Informe o primeiro lado:\n'))
n2 = float(input('Informe o segundo lado:\n'))
n3 = float(input('Informe o terceiro lado:\n'))

if n1 + n2 < n3 :
    print('Não pode ser um triangulo !!!')
elif n1 + n3 < n2 :
    print('Não pode ser um triangulo !!')
elif n2 + n3 < n1:
    print('Não pode ser um triângulo !!')
else:
    if n1 == n2 == n3:
        print('É um triângulo \033[32mEquilátero\033[m')
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('É um triângulo \033[32mIsosceles\033[m')
    else:
        print('É um triângulo \033[32mEscaleno\033[m')