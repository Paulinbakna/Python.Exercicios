from colorama import Fore,Style
def logger(function):
    from datetime import datetime
    from colorama import Fore,Style
    def inner_function(*args, **kwargs):
        try:
            result= function(*args, **kwargs)
            print(f'{Fore.BLUE}Data e Hora que foi chamada: {Style.RESET_ALL}{Fore.CYAN}{datetime.now()}{Style.RESET_ALL}\n{Fore.MAGENTA}Chamando a função: {Style.RESET_ALL}{Fore.GREEN}{function.__name__}{Style.RESET_ALL}')
            print(f'{Fore.YELLOW}Resultado:{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}{result}{Style.RESET_ALL}')
            print('-'*60)
            return result
        except Exception as e:
            print(f'{Fore.BLUE}Data e Hora que foi chamada: {Style.RESET_ALL}{Fore.RED}{datetime.now()}\nERRO!\nNao foi possivel chamar a função: {function.__name__}.\nErro apresentado: {str(e)}{Style.RESET_ALL}')
    return inner_function

@logger
def soma(a,b):
    return a + b

@logger
def subtrair(a,b):
    return a - b 

@logger
def multiplicar(a,b):
    return a * b

@logger
def dividir(a,b):
    return a * b


print('-'*60)
mensagem= '-- CALCULADORA BASICA -- ' 
centro=mensagem.center(60)
print(centro)
print('-'*60)
while True:    
    try:
        n1=int(input('Digite o 1° numero: '))
        n2=int(input('Digite o 2° numero: '))
        print('Certo agora escolha oq deseja fazer')
        print()
        print(f'------ Menu ------ ')
        print('[ 1 ] Soma')
        print('[ 2 ] Subtração')
        print('[ 3 ] Multiplicação')
        print('[ 4 ] Divisão')
        print('[ 5 ] Sair')
        print('--------------------')
        escolha=int(input(f'{Fore.CYAN}=>>{Style.RESET_ALL}'))
        
        if escolha == 1 :
            soma(n1,n2)
        elif escolha == 2 :
            subtrair(n1,n2)
        elif escolha == 3 :
            multiplicar(n1,n2)
        elif escolha == 4: 
            dividir(n1,n2)
        elif escolha == 5:
            print('Programa encerrado!')
        break
    except Exception as e:
        print('-'*60)
        print(f'{Fore.RED}Erro! Digite somente numeros!{Style.RESET_ALL}')
    if escolha == 5:
        print('Programa encerrado!')