from datetime import datetime

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Obtenha o dia da semana da data de hoje
dias=["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]

data=datetime.now()
dia=dias[data.weekday()]
print(f'Dia da semana: {dia}')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Obtenha o número do mês da data de hoje
meses=["1","2","3","4","5","6","7","8","9","10","11","12"]

mes=meses[data.month - 1 ]
print(f'Numero do mês: {mes}')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Obtenha o ano da data de hoje 
ano=data.year
print(f'Ano: {ano}')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Obtenha a hora no formato de 12 horas (AM/PM) da hora atual
hora=data.strftime('%I:%M:%S %p')
print(f'Hora no formato de 12 horas: {hora}')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Obtenha o minuto da hora atual
minuto=data.minute
print(f'Minuto da Hora Atual: {minuto}')
