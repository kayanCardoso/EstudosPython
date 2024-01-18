# Desafioo 067 
cont = 1
while True:
    n = int(input('Qual número você deseja ver a tabuada(Sáidanúmero negativo)'))
    print('-'*30)
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} X {cont} = {n*cont}')
        cont += 1
    cont = 1 
    print('-'*30)    