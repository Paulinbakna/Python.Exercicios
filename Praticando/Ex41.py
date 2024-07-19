from datetime import datetime,time

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Verifique se uma string de entrada represenda uma data válida no formato yyyy-mm-dd

dia=int(input('Digite a data (dd): '))
mes=int(input('Digite o mes (mm): '))
ano=int(input('Digite o ano: (yyyy): '))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
try:
    data_digitada=datetime(day=dia,month=mes,year=ano)
    data_completa=data_digitada.strftime('%d/%m/%Y')
    datetime.strptime(data_completa,'%d/%m/%Y')
    print(f'Data: {data_completa}')
except ValueError:
    print('Data no formato incorreto!')


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Verifique se uma string de entrada representa uma hora valida no formato hh:mm:ss

hora=int(input('Digite o numero da hora:'))
minuto=int(input('Digite o minuto: '))
segundos=int(input('Digite os segundos:'))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
try:
    hora_digitada=time(hour=hora,minute=minuto,second=segundos)
    hora_completa=hora_digitada.strftime('%H:%M:%S')
    datetime.strptime(hora_completa,'%H:%M:%S')
    print(f'Hora: {hora_completa}')
except ValueError:
    print('Hora digitada Incorreta!')
    