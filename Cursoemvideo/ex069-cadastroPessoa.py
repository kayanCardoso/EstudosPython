from colorama import Fore, init
init()
cores = {
    'amarelo': Fore.YELLOW,
    'azul': Fore.BLUE,
    'vermelho': Fore.RED,
    'verde': Fore.GREEN,
    'roxo': Fore.MAGENTA,
    'ciano': Fore.CYAN, 
    'reset': Fore.RESET
}

maior18 = men = fem20 = 0

while True:
    print('~'*20)
    print('      CADASTRO')
    print('~'*20)
    idade = int(input('Informe sua idade: '))
    while idade < 0:
        idade = int(input('Informe sua idade(Use numeros positivos): '))
    sexo = str(input('Qual seu sexo? [F/M] ')).upper().strip()[0]
    while sexo not in "FM":
       sexo = str(input('Qual seu sexo? [F/M] ')).upper().strip()[0] 
    if idade > 18 :
        maior18 += 1
    if sexo == 'M':
        men += 1
    if sexo == 'F' and idade < 20:
        fem20 += 1
    val = str(input('Deseja continuar ? [S/N]')).upper().strip()
    while val not in 'SN':
        val = str(input('Use uma letra valida, deseja continuar ? [S/N]')).upper().strip()
    if val == 'N':
        break
if maior18 > 1 :
    print(f'Tivemos {maior18} pessoas maiores de idade !!!')
elif maior18 == 1:
    print('Tivemos uma pessoa maior de idade !!')
else:
    print('Não tivemos pessoas maiores de idade !!')
if men == 1:
    print('Foi cadastrado apenas um homem !!')
else:
    print(f'Foram cadastrados {men} homens !!')
if fem20 == 1:
    print('Uma mulher com menos de 20 anos foi cadastrada !!')
else:
    print(f'{fem20} mulheres com menos de 20 anos foram cadastradas !!!')