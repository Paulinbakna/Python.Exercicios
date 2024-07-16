from datetime import datetime

#Formate a data de hoje no formato dd de MMMM de yyyy
data_hoje=datetime.now()
data_formatada=data_hoje.strftime('%d de %B de %Y')
print(data_formatada)

#formate a hora atual no formato hh:mm:ss (12 horas) com AM/PM
hora_hoje=datetime.now()
hora_formatada=hora_hoje.strftime('%I:%M:%S %p')
print(hora_formatada)

#Crie uma string que represente a data e hora atuais no formato completo (ano,mes,dia,hora,minuto,segundo,fuso horario)
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

dia=data_hoje.day
mes=meses(data_hoje.month - 1)
ano=data_hoje.year
hora=hora_hoje.hour
minutos=hora_hoje.minute
segundos=hora_hoje.second
fuso_horario=hora_hoje.
