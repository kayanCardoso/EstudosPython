# ano bissexto

from datetime import date
ano = int(input('Informe o ano que deseja analisar:(Informe "0" para o ano atual)\n'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')