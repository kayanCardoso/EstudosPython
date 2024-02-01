from time import sleep

def contador():
    print('-='*20)
    print('Contagem de 1 em 1 até 10')
    for i in range(1,11):
        print(i,end=' ',flush=True)
        sleep(0.5)
    print('FIM')
    print('-='*20)
    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10,-1,-2):
        print(i,end=' ',flush=True)
        sleep(0.5)
    print('FIM')
    print('-='*20)
    print('Sua vez agora !!!')
    x = int(input('de: '))
    y = int(input('até: '))
    z = int(input('passo: '))
    if x > y:
        if z == 0:
            for i in range(x,y-1,-1):
               print(i,end=' ',flush=True)
               sleep(0.5)
            print('FIM')
        elif 0 > z:
            for i in range(x,y-1,z):
               print(i,end=' ',flush=True)
               sleep(0.5)
            print('FIM')
        else:
            for i in range(x,y-1,-z):
                print(i,end=' ',flush=True)
                sleep(0.5)
            print('FIM')
    else:
        if z == 0:
            for i in range(x,y+1,1):
                print(i,end=' ',flush=True)
                sleep(0.5)
            print('FIM')
        else:
            for i in range(x,y+1,z):
                print(i,end=' ',flush=True)
                sleep(0.5)
            print('FIM')

    print('-='*20)


contador()
