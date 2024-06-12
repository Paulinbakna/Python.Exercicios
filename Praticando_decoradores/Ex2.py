def meu_decorador(func):
    def mostrar(*args, **kwargs):
        print('Antes da função!')
        result = func(*args, **kwargs)
        print(f'Resultado: {result}')
        print('Depois da função!')
        return result
    return mostrar
@meu_decorador
def funcao(a,b):
    print(f'Dentro da função: a={a} | b={b}')
    return a + b

resultado=funcao(1,2)
