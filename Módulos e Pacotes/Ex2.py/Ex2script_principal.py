import media
import mediana
import moda
from time import sleep

valores=[]

while True:
    try:
        sleep(0.5)
        print('=-'*20)    
        n=int(input('Digite os valores: '))
        if n > 0:
            valores.append(n)
        elif n == 0:
            if len(valores) < 2:
                print('E necessario digitar no minimo 2 numeros')
            else:
                break
        else:
            print('O numero deve ser positivo!')
    except ValueError:
        print('Valor digitado invalido por favor digite um valor valido!')
    
    sleep(0.5)
    print('=-'*20)    
    continuar=input('Quer continuar?[S/N]')
    
    if continuar in 'Nn':
        if len(valores) < 2:
            print('E necessario digitar no minimo 2 numeros!')
        else:    
            break

print('=-'*20)    
print(f'Valore inseridos: {valores}')
sleep(2)
print(media.media(valores))
sleep(2)
print(mediana.mediana(valores))
sleep(2)
print(moda.moda(valores))
