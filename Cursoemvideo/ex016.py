# Formatando o número
import  math
num = float(input('Digite um número : '))
print('O valor digitado foi {} sua parte inteira é {} '
      '\n outra forma {:.0f}'
      '\n outra forma {}'.format(num,math.trunc(num),num, int(num)))