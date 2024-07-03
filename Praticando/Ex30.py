import json

#Exemplo 7: Adicionar um novo item a uma lista em um arquivo JSON Este exemplo demonstra como ler um arquivo JSON, adicionar um novo item a uma lista existente, e escrever as mudanças de volta ao arquivo.

def adicionar_json(caminho_arquivo,chave,novo_valor):
    with open(caminho_arquivo,'r',encoding='utf-8') as arquivo:
        dados=json.load(arquivo)
    
    if chave in dados and isinstance(dados[chave],list):
        dados[chave].append(novo_valor)
    else:
        dados[chave]=novo_valor
    
    with open(caminho_arquivo,'w',encoding='utf-8') as arquivo:
        json.dump(dados,arquivo,ensure_ascii=False,indent=4)

dados_exemplo={
    "nome":"João",
    "idade":35,
    "cidade":"São Paulo",
    "habilidades":["Python","CSS","HTML","JavaScript"]
}

caminho_arquivo=r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Praticando\arquivo_teste.json'

with open(caminho_arquivo,'w',encoding='utf-8') as arquivo:
    json.dump(dados_exemplo,arquivo,ensure_ascii=False,indent=4)

chave='habilidades'
novo_valor='C++'
adicionar_json(caminho_arquivo,chave,novo_valor)

print(f'Item {novo_valor} adicionado a lsita {chave}')

with open(caminho_arquivo,'r',encoding='utf-8') as arquivo:
    dados_atualizados=json.load(arquivo)
    print('Conteudo do arquivo json atualizado')
    print('-'*40)
    print(json.dumps(dados_atualizados,ensure_ascii=False,indent=4))
    print('-'*40)

