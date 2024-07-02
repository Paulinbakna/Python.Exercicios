import csv

def calcualr_media(caminho_arquivo,nome_coluna):
    #abre o arquivo CSV no modo de leitura ('r') e com codificação UTF-8
    with open(caminho_arquivo, 'r+',encoding='utf-8') as arquivo:
        leitor=csv.DictReader(arquivo)
    
    #Cria uma lista de valores,extraindo os valores da coluna especificada e converte para float para facilitar o calculo
    valores=  [float(linha[nome_coluna]) for linha in leitor ]

    #Calcula a média dos valores. Se a lista estiver vazia, retorna 0
    media= sum(valores)/ len(valores) if valores else 0

    #Retorna a média calculada
    return media

#Exemplo de uso da função
caminho_arquivo='exemplo.csv' #Caminho para o  arquivo CSV

nome_coluna='idade' #Nome da coluna da qual queremos calcular média(Exemplo para facilitar o entendimento abaixo )

#== arquivo.CSV (apenas para entendimento) ==== 

# nome,   idade,  salario
# João,   30   ,  2500
# Ana,    25   ,  2400  
# Maria,  40   ,  2600
# Carlos, 50   ,  3000

#Nesse exemplo as colunas são: nome, idade e salario

#Calcula a média dos valores na coluna especificada
media =calcualr_media(caminho_arquivo,nome_coluna)

#imprime a média calculada
print(f'A média dos valores na coluna {nome_coluna} é: {media}')

