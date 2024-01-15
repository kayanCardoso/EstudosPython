
from random import randint

pc = randint(0,10)
y = 0
print('~'*5,'JOGO DA ADIVINHAÇÃo','~'*5)
x = int(input('Informe um número de 0 a 10: '))
while x != pc:
    if x != pc:
        print('Você \033[31mERROU\033[m')
        print(f'Eu escolhi \033[35m{pc}\033[m e você \033[35m{x}\033[m')
        print('Tente novamente\n')
    pc = randint(0,10)
    y += 1
    x = int(input('Informe um número novamente de 0 a 10: '))
print('\033[32mVocê ganhou\033[m')
print(f'Eu escolhi {pc} e você também {x}, foram necessarias {y} tentativas!!')