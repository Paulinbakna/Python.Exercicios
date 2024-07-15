from datetime import datetime,timedelta

#crie uma variacel que represente a data de hoje
data_hoje=datetime.now()
print(f'Data de Hoje: {data_hoje.strftime('%d/%m/%Y')}')

#adicione 10 dias a variavel e imprima a nova data
dez_dias=data_hoje +  timedelta(days=10)
print(f'Data atual somado a +10 dias: {dez_dias.strftime('%d/%m/%Y')}')

#Subtraia 5 dias da variavel e imprima a nova data
cinco_dias=data_hoje - timedelta(days=5)
print(f'Data a 5 dias atras: {cinco_dias.strftime('%d/%m/%Y')}')

#Verifique se a data de hoje é anterior a data 01/01/2000
verificar=datetime.strptime('01/01/2000','%d/%m/%Y')

if data_hoje > verificar:
    print(f'A data {data_hoje.strftime('%d/%m/%Y')} e superior a data: {verificar.strftime('%d/%m/%Y')}')
else:
    print(f'A data {data_hoje.strftime('%d/%m/%Y')} não é superior a data: {verificar.strftime('%d/%m/%Y')}')
    
    
#Calcule a diferença em dias entre a data de hoje e a data 01/01/2024
data_antiga=datetime.strptime('01/01/2024','%d/%m/%Y')
diferenca= (data_hoje-data_antiga).days

print(f'Diferença de dias da data {data_antiga.strftime('%d/%m/%Y')} para a data atual {data_hoje.strftime('%d/%m/%Y')}: {diferenca} dias')

