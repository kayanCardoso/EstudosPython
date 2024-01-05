from random import randint
from time import sleep
pc = randint(1, 3)
emopc = ''
emops = ''
if pc == 1:
    emopc = '🫱'
elif pc == 2: 
    emopc = '✊'
else:
    emopc = '✌️'
print('Vamos jogar Jokepô')
print('|','_'*30,'|')
ps = int(input('Escolha o que irá jogar\n\n 1 = 🫱 \n2 = ✊ \n3 = ✌️ \n'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
if ps == 1:
    emops = '🫱'
elif ps == 2:
    emops = '✊'
elif ps == 3:
    emops = '✌️'
if pc == ps :
    print(f'Deu empate eu escolhi{emopc}  e você {emops}')
elif ps > 3 or ps < 1:
    print('Numero invalido!!')
elif pc == 1 and ps == 2 or pc == 2 and ps == 3 or pc == 3 and ps == 1:
    print(f'Eu ganhei !! {emopc}  ganha disso  {emops}')
else:
    print(f'Você ganhou !! {emops}  ganha disso  {emopc}')