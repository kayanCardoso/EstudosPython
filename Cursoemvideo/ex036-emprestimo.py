
# exercicio 036 emprestimo da casa

valor = float(input('Qual valor da casa?\n '))
salario = float(input('Qual seu salário?\n'))
ano = int(input('Vai pagar me quantos anos?\n'))
parcela = ano * 12

if (valor / parcela) > (salario * 30 / 100) :
    print('Seu imprestimo foi\033[31m NEGADO!!!\033[m')
else:
    print('Seu imprestimo foi \033[32mAPROVADO!!\033[m')