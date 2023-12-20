# Jogo da advinhação
from random import randint
comp = randint(0,5)
n1 = int(input('Qual número eu pensei ? '))
if comp == n1:
    print('Parabéns!! você acertou')
else:
    print('Você errou burro !!')