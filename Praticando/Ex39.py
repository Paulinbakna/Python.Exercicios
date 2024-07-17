from datetime import datetime,timezone,timedelta
import time

#Converta a data e hora atuais para o fuso horario utc+0 (londres)
fuso_londres=timezone(timedelta(hours=+1))
hora_hoje_londres=datetime.now(fuso_londres)
hora_formatada=hora_hoje_londres.strftime('%I:%M:%S')
print(f'Hora Atual em londres: {hora_formatada}')

#Crie uma variavel que represente a data e hora em novaYork (fuso horario UTC-5)
fuso_nova_york=timezone(timedelta(hours=-5))

hora_hoje_nova_york=datetime.now(fuso_nova_york)

data_formatada_nova_york=hora_hoje_nova_york.strftime('%d/$B/%Y')

hora_formatada_nova_york=hora_hoje_nova_york('%I:%M:%S')
print(f'Hora Atual em Nova York: {hora_formatada_nova_york} | Data atual: {data_formatada_nova_york}')

