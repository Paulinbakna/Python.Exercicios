def meu_decorador(func):
    def mostrar():
        print('Antes da função')
        func()
        print('Depois da função')
    return mostrar
    
@meu_decorador
def funçao():
    print('Função chamada!')
    
    
funçao()