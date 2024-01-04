nota1 = float(input('Informe sua primeira nota :\n'))
nota2 = float(input('Informe sua segunda nota :\n'))
media = (nota1 + nota2)/2

if media >= 7: 
    print('Você foi \033[32mAPROVADO!!!\033[m')
elif media >= 5:
    print('Você está de \033[33mRECUPERAÇÃO!!!\033[m')
else:
    print('Você foi \033[31mREPROVADO!!!\033[m')
