from datetime import date

pessoa = dict()
pessoa['nome'] = input('Nome: ')
ano = date.today().year
idade = int(input('Ano de nascimento: '))
while idade > ano or idade < 1920:
    idade = int(input('Você não tem essa idade !!! informe uma correta: '))

pessoa['Idade'] = ano - idade
pessoa['ctps'] = int(input('Número carteira de trabalho (0 não tem): '))
if pessoa['ctps'] > 0 :
    contra = int(input('Ano de contratação: '))
    while contra < idade or contra < (idade+14):
        print('Data invalída')
        contra = int(input('Informe novamente: '))
    pessoa['contratacao'] = contra
    pessoa['Salário'] = float(input('Salário R$:'))
if pessoa['ctps'] > 0 :
    print('~='*30)
    print(f'Oi {pessoa["nome"]}, esse é seu relatorio!!!')
    print(f'Idade {pessoa["Idade"]}')
    print(f'CTPS {pessoa["ctps"]}')
    print(f'Foi contratado em {pessoa["contratacao"]}')
    print(f'Se aposentara com {(pessoa["contratacao"]-idade)+35} anos de idade')
else:
    print('~='*30)
    print(f'Oi {pessoa["nome"]}, esse é seu relatorio!!!')
    print(f'Idade {pessoa["Idade"]}')
    print(f'Não tem CTPS')
