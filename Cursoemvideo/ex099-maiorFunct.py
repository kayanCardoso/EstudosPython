
def maior(* num):
    top = list()
    pos = 0
    for i in enumerate(num):
        top.append(num[pos])
        pos+=1
    top.sort()
    print('-'*15)
    print(f'os numeros foram {num}')
    print(f'O maior numero foi {top[-1]}')
    print('-'*15)

maior(1,2,4,5,6,7,1,)    
maior(1,3)
maior(0,3,9,4)

