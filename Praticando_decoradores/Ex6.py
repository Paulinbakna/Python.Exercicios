def verificar(func):
    def mostrar(*args, **kwargs):
        if mostrar.autenticado == True:
            func(*args, **kwargs)
            print(f'Usuario Autenticado.Acesso Liberado.')
        else:
            print(f'Usuario não autenticado. Acesso Negado')
            return
    mostrar.autenticado= False
    return mostrar

@verificar
def acesso():
    print(f'Tentando acessar...')

acesso()
acesso.autenticado = True
acesso()