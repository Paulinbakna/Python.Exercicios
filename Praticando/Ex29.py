import json
#Ex4: Crie um script que leia um arquivo JSON e atualize um valor específico dentro do JSON.

def atualizar_json(caminho_arquivo,chave,novo_valor):
    with open(caminho_arquivo,'r',encoding='utf-8') as arquivo:
        
        dados= json.load(arquivo)
        
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
    
chave='idade'
novo_valor=99
atualizar_json(caminho_arquivo,chave,novo_valor)
print(f'O valor da chave: {chave} foi atualizado para {novo_valor} no arquivo que se localiza em {caminho_arquivo}')

with open(caminho_arquivo,'r',encoding='utf-8') as arquivo:
    dados_atualizados=json.load(arquivo)
    print('Conteudo do arquivo json atualizado')
    print('-'*40)
    print(json.dumps(dados_atualizados,ensure_ascii=False,indent=4))
    print('-'*40)
    
    
