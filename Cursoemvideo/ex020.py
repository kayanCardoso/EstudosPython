# sequencia embaralhada
import random

n1 = str(input('Primeiro nome : '))
n2 = str(input('Segundo nome : '))
n3 = str(input('Terceiro nome : '))
n4 = str(input('Quarto nome : '))
li = [n1, n2, n3, n4]
random.shuffle(li)
print('A ordem é\n{}'.format(li))