expre = (str(input('Digite a expressão :')))
p1 = expre.count('(')
p2 = expre.count(')')
if p1 == p2:
    print('A expressão está certa!!')
else:
    print('A expressão está errada!!')
