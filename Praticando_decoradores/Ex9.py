def contador_execuções(func):
    def mostrar(*args, **kwargs):
        mostrar.contador += 1
        print(f"A função {func.__name__}foi chamada {mostrar.contador} vezes")
        return func(*args, **kwargs)
    mostrar.contador = 0
    return mostrar

@contador_execuções
def teste():
    print('teste')

teste()
teste()
teste()
#------------------------