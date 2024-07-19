from datetime import datetime

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
    print(f'Data no formato incorreto!')
