import Ex1funcoes
from time import sleep

print("=-= CALCULADORA =-=")
while True:    
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    a=int(input('Digite um numero:'))
    sleep(1)
    b=int(input('Digite outro numero: '))
    sleep(1)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Certo agora escolha oq deseja fazer: ')
    print('--------------------')
    print('[ 1 ] Somar ')
    print('[ 2 ] Subtrair ')
    print('[ 3 ] Multiplicar ')
    print('[ 4 ] Dividir ')
    print('[ 5 ] Sair ')
    print('--------------------')
    n=int(input('-->>'))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    sleep(1)
    
    if n == 1:
        print(Ex1funcoes.somar(a,b))
        sleep(2)
        
    elif n == 2:
        print(Ex1funcoes.subtrair(a,b))
        sleep(2)
        
    elif n == 3:
        print(Ex1funcoes.multiplicar(a,b))
        sleep(2)
    
    elif n == 4:
        print(Ex1funcoes.dividir(a,b))
        sleep(2)
    
    elif n == 5:
        print('Saindo Do Programa....')
        break
    else:
        print('Não consegui indentidicar. Por favor digite novamente!')
        sleep(2)
    
sleep(2)
print('Programa Finalizado!')
