media = 0
velho = 0
nomevelho = ''
menor = 0
for i in range(0,4):
    print('=-'*20)
    nome = str(input('Qual seu nome ? ')).upper()
    idade = int(input('Qual sua idade ? '))
    sexo = int(input('Qual seu sexo\n1-Masculino\n2-Feminino\n'))
    print('=-'*20,'\n')
    if sexo > 2 or sexo < 1:
        print('\033[31mOpção invalida!!\033[m')
    else:
        if sexo == 1 and idade > velho:
            velho = idade
            nomevelho = nome
        if sexo == 2 and idade < 21:
            menor += 1
    media += idade
print(f'O homem mais velho é {nomevelho} e sua idade é de {velho} anos')
print(f'A media de idade é {media/4:.1f}')
if menor == 0:
    print('Nenhuma mulher está abaixo de 21 anos')
elif menor == 1:
    print('Uma mulher está abaixo dos 21 anos')
else:
    print(f'{menor} mulheres são menores de 21 anos')