# Calculando o triangula retangulo
import math

n1 = float(input('Informe o cateto oposto: '))
n2 = float(input('Informe o cateto adjacente: '))
hip = math.hypot(n1, n2)
hip2 = (n1**2 + n2**2)**(1/2)

print('A hipotenusa é {:.2f} \n'
      'forma sem biblioteca {:.2f}'.format(hip,hip2))