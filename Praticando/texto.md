import csv

# Função para calcular a média dos valores em uma coluna específica de um arquivo CSV
def calcular_media(caminho_arquivo, nome_coluna):
# Abre o arquivo CSV no modo de leitura ('r') e com codificação UTF-8
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
# Cria um leitor CSV que lê cada linha como um dicionário
        leitor = csv.DictReader(arquivo)
        
# Cria uma lista de valores, extraindo os valores da coluna especificada
# e convertendo-os para float
        valores = [float(linha[nome_coluna]) for linha in leitor]
        
# Calcula a média dos valores. Se a lista estiver vazia, retorna 0
        media = sum(valores) / len(valores) if valores else 0
        
# Retorna a média calculada
        return media

# Exemplo de uso da função
caminho_arquivo = 'exemplo.csv'  # Caminho para o arquivo CSV
nome_coluna = 'idade'  # Nome da coluna da qual queremos calcular a média

# Calcula a média dos valores na coluna especificada
media = calcular_media(caminho_arquivo, nome_coluna)

# Imprime a média calculada
print(f'A média dos valores na coluna {nome_coluna} é: {media}')
