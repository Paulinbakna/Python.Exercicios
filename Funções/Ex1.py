def maior_numero(num1,num2):
    if num1 > num2:
        print(f'O numero {num1} e o maior numero.') 
    elif num1 == num2:
        print(f'Os numeros {num1} e {num2} são iguais')
    else:
        print(f'O numero {num2} e o maior numero.')
    

n1=int(input('Digite um numero:'))
n2=int(input('Digite um numero:'))
maior_numero(n1,n2)
