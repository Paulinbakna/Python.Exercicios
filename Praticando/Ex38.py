from datetime import datetime, timezone,timedelta
import time

#Formate a data de hoje no formato dd de MMMM de yyyy
data_hoje=datetime.now()
data_formatada=data_hoje.strftime('%d de %B de %Y')
print(data_formatada)
print('-'*40)

#formate a hora atual no formato hh:mm:ss (12 horas) com AM/PM
hora_hoje=datetime.now()
hora_formatada=hora_hoje.strftime('%I:%M:%S %p')
print(hora_formatada)
print('-'*40)

#Crie uma string que represente a data e hora atuais no formato completo (ano,mes,dia,hora,minuto,segundo,fuso horario)
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]


dia=data_hoje.day
mes=meses[data_hoje.month - 1]
ano=data_hoje.year

hora=hora_hoje.hour
minutos=hora_hoje.minute
segundos=hora_hoje.second

fuso_horario=timezone(timedelta(hours=-3))
fuso=datetime.now(fuso_horario)
fuso_formatado=fuso.strftime('%Z')
nome_fuso=time.tzname[time.localtime().tm_isdst]


print(f'Dia: {dia} | Mes: {mes} | Ano: {ano}')
print(f'Hora: {hora} | Minutos: {minutos} | Segundos: {segundos}')
print(f'Fuso Horario: {nome_fuso} {fuso_formatado}')
print('-'*40)

