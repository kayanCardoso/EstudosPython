def resul(lst,sit = False):
    '''
    -> função de analise de situação de alunos
    lst = lista de notas dos alunos
    sit: para mostrar se sua situação está boa ou não (false padrão) 
    return = dicionario com as informções
    
    '''
    lst.sort()
    tot = 0
    for i, v in enumerate(lst):
        tot += v
    if sit == False:
        notas = {
            'total': len(lst),
            'maior': lst[-1],
            'menor': lst[0],
            'media': tot / len(lst)  
        }
        return notas 
    else:
        if tot / len(lst) >= 7:
            situ = 'BOA'
        elif  tot / len(lst) >= 5:
            situ = 'MEDIA'
        else:
            situ = 'RUIM'
        notas = {
            'total': len(lst),
            'maior': lst[-1],
            'menor': lst[0],
            'media': (tot / len(lst)),
            'situação': situ
        }

    return notas


notas = list()
while True:
    notas.append(float(input('Informe a nota: ')))
    cont = input('Deseja continuar[S/N]: ').upper()[0]
    while cont not in 'SN':
        cont = input('Deseja continuar[S/N]: ').upper()[0]
    if cont == 'N':
        break

resp = resul(notas,sit=True)
print(resp)

