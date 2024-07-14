from datetime import datetime
hoje = datetime.now()
hoje_brasileiro=hoje.strftime('%d/%m/%Y')
hoje_hora=hoje.strftime('%H:%M:%S')

data_aniversario=datetime(year=2004,month=6,day=22)

proximo_aniversario=data_aniversario.replace(year=hoje.year)

if proximo_aniversario < hoje:
    proximo_aniversario = proximo_aniversario.replace(year=hoje.year+1)
    
dias_para_aniversario = (proximo_aniversario - hoje).days


print(f'Data de Hoje: {hoje_brasileiro}')
print(f'Hora Atual: {hoje_hora}')
print(f'Data Aniversario: {data_aniversario.strftime('%d/%m/%Y')}')
print(f'Dias Para o Proximo Aniversario: {dias_para_aniversario}')