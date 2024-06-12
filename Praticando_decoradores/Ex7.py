def memoria(func):
    cache={}
    def mostrar(*args):
        if args in cache:
            print('Retornando do cache')
            return cache[args]
        result=func(*args)
        cache[args]=result
    return mostrar

@memoria
def somar(a,b):
    return a + b

print(somar(1,2))
print(somar(1,3))
print(somar(2,2))
print(somar(1,2))
print(somar(1,3))

