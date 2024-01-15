sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\nOpção invalida!!  Informe [M/F]')).strip().upper()[0]
if sexo == 'M':
    print('Você escolheu a opção Masculino(a)')
else:
    print('Você escolheu a opção Femenina(o)')