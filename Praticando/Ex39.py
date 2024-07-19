from datetime import datetime,timezone,timedelta
import time

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Converta a data e hora atuais para o fuso horario utc+0 (londres)
fuso_londres=timezone(timedelta(hours=+1))
hora_londres=datetime.now(fuso_londres)
hora_formatada=hora_londres.strftime('%I:%M:%S')
print(f'Hora Atual em londres: {hora_formatada}')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Crie uma variavel que represente a data e hora em novaYork (fuso horario UTC-5)
fuso_ny=timezone(timedelta(hours=-5))

hora_ny=datetime.now(fuso_ny)
hora_formatada_ny=hora_ny.strftime('%H:%M:%S ')
data_formatada_ny=hora_ny.strftime('%d/%m/%Y')
    
print(f'Hora Atual em Nova York: {hora_formatada_ny} | Data atual: {data_formatada_ny}')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Converte a variável de nova york para o fuso horario local

fuso_local=fuso_nova_york=timezone(timedelta(hours=-3))
hora_local=datetime.now(fuso_local)
hora_local_formatada=hora_local.strftime('%H:%M:%S')
print(f'Hora local: {hora_local_formatada}')

