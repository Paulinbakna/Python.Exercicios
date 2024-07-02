# Ex4: Atualizar um valor específico em um arquivo JSON

import json

def atualizar_json(caminho_arquivo, chave, novo_valor):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    
    dados[chave] = novo_valor

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

# Exemplo de uso
caminho_arquivo = 'caminho/para/o/arquivo.json'
chave = 'idade'
novo_valor = 31
atualizar_json(caminho_arquivo, chave, novo_valor)
print(f'O valor da chave {chave} foi atualizado para {novo_valor} no arquivo {caminho_arquivo}')
