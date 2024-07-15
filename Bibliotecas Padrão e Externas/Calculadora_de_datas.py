from datetime import datetime

hoje=datetime.now()
data_formatada=hoje.strftime('%d/%m/%Y')
hora_atual=hoje.strftime('%H:%M:%S')

dia=int(input('Digite o dia: '))
mes=int(input('Digite o mes: '))
ano=int(input('Digite o ano (com 4 digitos): '))

data_digitada=datetime(year=ano,month=mes,day=dia)

proximo_aniversario=data_digitada.replace(year=hoje.year)
if proximo_aniversario < hoje:
    proximo_aniversario = proximo_aniversario.replace(year=hoje.year + 1)

dias_para_aniversario= (proximo_aniversario - hoje).days

print(f'Data de Hoje: {data_formatada}')
print(f'Hora Atual: {hora_atual}')
print(f'Data Aniversario Digitada: {data_digitada.strftime('%d/%m/%Y')}')
print(f'Dias Para o Proximo Aniversario: {dias_para_aniversario} dias ')

