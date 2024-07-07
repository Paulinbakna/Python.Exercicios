def dividir(n1,n2):
    try:
        resutado=n1/n2
        
    except ZeroDivisionError:
        return '-->> Error! Divisão por zero não e permitida! <<--'
    except TypeError:
        return '-->> Error! Digite um valor valido! <<--'
    else:
        return f'Resultado: {resutado}'

    finally:
        print('-->> Função Dividir Chamada <<--')
    
num1=int(input('Digite um numero:'))
num2=int(input('Digite mais um numero:'))
funcao=dividir(num1,num2)
print(funcao)
   