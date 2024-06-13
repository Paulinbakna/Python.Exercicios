def decorador_com_retorno(func):
    def mostrar(*args, **kwargs):
        resultado= func(*args, **kwargs) *2
        print(f'Resultado da soma multiplicado: {resultado}')
    return mostrar


@decorador_com_retorno
def somar(a,b): 
    return a + b


somar(1,2)