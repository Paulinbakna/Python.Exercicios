def verificar_tipo(tipo):
    def decorador(func):
        def mostrar(*args, **kwargs):
            if all(isinstance(arg,tipo) for arg in args):
                return func(*args, **kwargs)
            else:
                print('ERRO! Os argumentos tem que ser do mesmo tipo!')
        return mostrar
    return decorador

@verificar_tipo(int)
def somar(a,b):
    return a + b

print(somar(1,2))

print(somar(1,'3'))
