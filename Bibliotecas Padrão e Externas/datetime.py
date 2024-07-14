from datetime import datetime,timedelta
#Para poder somar datas e necessario importar o "timedelta"

#Ver data e hora de hoje
hoje= datetime.now()

#ver somente o dia
hoje.day

#ver somente o mes
hoje.month

#ver somente o ano
hoje.year

#ver somente o hora
hoje.hour

#ver somente os minutos
hoje.minute

#ver somente os segundos
hoje.second

print(hoje)


#somando datas
#para somar basta passar o nome que voce gostaria de somar mais o valor que voce deseja adicionar
amanha=hoje + timedelta(days=1)

#criando uma data especifica
data_qualquer=datetime(year=2023,month=9,day=15)

#calculando a quantidade de dias que se passou da data ou que ainda ira passar
data_atraso=hoje-data_qualquer
#!!!Atenção, No python o valor fica negativo se a primeira data que voce passar for a menor!!!

#para vewr somente os dias
data_atraso.days

#escrever uma data especifica no datetime,o strptime ele pega um texto e transforma em data 
data_compra='10/05/2022'
data_compra=datetime.strptime(data_compra,'%d/%m/%Y')

#tranformar datas em formato brasileiro, o strftime tranforma data em texto
data_compra.strftime('%d/%m/%Y')
