# Calculando seno, cosseno e tangente

import math
n1 = float(input('Digite o ângulo desejado : '))
ang = math.radians(n1)
se = math.asin(ang)
co, tan = math.acos(ang), math.atan(ang)

print('Seu ângulo de {} representa um \nseno de {:.2f} \n'
      'cosseno de {:.2f} \ntangente de {:.2f}'.format(n1, se, co, tan))
