import statistics

def moda(valores):
    try:
        moda= statistics.multimode(valores)
    except statistics.StatisticsError as e :
        return f'Erro ao calcular a moda: {e}'

    return f'Moda dos valores: {moda}'
