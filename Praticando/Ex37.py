from datetime import datetime,timedelta

#Crie uma variavel que represente a hora atual
hora=datetime.now()
hora_atual=hora.strftime('%H:%M:%S')
print(f'Hora atual: {hora_atual}')

#Adicione 30 minutos á variavel e imprima a nova hora
adicionar_minutos=hora + timedelta(minutes=30)
print(f'Hora atual +30 minutos: {adicionar_minutos.strftime('%H:%M:%S')}')

#Subtraia 1 hora da variavel e imprima a nova hora
tirar_hora=hora - timedelta(hours=1)
print(f'Hora atual -1 hora : {tirar_hora.strftime('%H:%M:%S')}')

#Verifique se a hora atual é posterior á hora 18:00
verificar=datetime.strptime('18:00:00','%H:%M:%S')

if  hora > verificar:
    print(f'A hora atual {hora_atual} e posterior a hora {verificar.strftime('%H:%M:%S')} ')
else:
    print(f'A hora atual {hora_atual} não e posterior a hora {verificar.strftime('%H:%M:%S')}')

#Calcule a diferença em segundos entre a hora atual e a hora 09:00:00
hora_antiga=datetime.strptime('09:00:00','%H:%M:%S')
diferenca=(hora - hora_antiga).seconds

print(f'Difeerença de segundos da hora {hora_antiga.strftime('%H:%M:%S')} para a hora atual {hora_atual}: {diferenca} segundos')