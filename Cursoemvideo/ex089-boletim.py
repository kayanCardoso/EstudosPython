
alunos = list()
nome = list()
notas = list()
c = 0

while True:
    nome.append(input('Informe o nome : ').capitalize())
    n1 = float(input('Informe a primeira nota : '))
    while n1 > 10 or n1 < 0:
        n1 = float(input('Informe uma nota válida !!!\n'))
    notas.append(n1)
    n2 = float(input('Informe a segunda nota :'))
    while n2 > 10 or n2 < 0:
        n2 = float(input('Informe uma nota válida !!!\n'))
    notas.append(n2)
    nome.append(notas[:])
    alunos.append(nome[:])
    notas.clear()
    nome.clear()
    x = input('Deseja continuar ? [S/N]').upper().strip()[0]
    while x not in 'SN':
        x = input('Informe uma opção valida!![S/N]').upper().strip()[0]
    if x == 'N':
        break
print('~='*20)
print('{:<5}'.format('No.'),'{:<10}'.format('NOME'), 'Média')
for i, c in enumerate(alunos):
    print(f'{i}','{:<3}'.format(''),f'{alunos[i][0]:10}',f'{(alunos[i][1][0]+alunos[i][1][1])/2}')

y = len(alunos)
teste = 0
while teste != 999:
    print('¨'*20)
    teste = int(input('Mostrar as notas de qual aluno (saída 999)'))
    if teste != 999:
        print(f'as notas de {alunos[teste][0]} são {alunos[teste][1]}')

