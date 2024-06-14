import time

def tempo_execucao(func):
    def mostrar(*args, **kwargs):
        inicio=time.time()
        fim=time.time()
        result=func(*args, **kwargs)
        print(f'Resultado: {result}')
        print(f'Tempo de execução: {inicio-fim}')
        return result
    return mostrar
@tempo_execucao
def estudar(tempo):
    print(f'Estudando por {tempo} Horas')
    time.sleep(3)
    print(f'Pausa para  o café')
    
estudar(3)