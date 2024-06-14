def repete(vezes):
    def decorador(func):
        def mostrar(*args, **kwargs):
            for _ in range(vezes):
                func(*args, **kwargs)
        return mostrar
    return decorador


@repete(5)
def mensagem():
    print('Ola estou repetindo!')
    
mensagem()
