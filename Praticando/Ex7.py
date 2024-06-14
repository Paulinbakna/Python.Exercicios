def memoria(func):
    cache={}
    
    def mostrar(*args):
        if args in cache:
            print('Retornando do cache')
            return cache[args]
        result=func(*args)
        cache[args]=result
        return result
    return mostrar

@memoria
def somar(a,b):
    return a + b

print(f'Resultado da soma: {somar(1,2)}')
print(f'Resultado da soma: {somar(1,3)}')
print(f'Resultado da soma: {somar(2,3)}')
print(f'Resultado da soma: {somar(1,2)}')
print(f'Resultado da soma: {somar(1,3)}')

