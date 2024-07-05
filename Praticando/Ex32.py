import json

def remover(caminho,chave):
    with open(caminho,'r',encoding='utf-8') as arquivo:
        dados=json.load(arquivo)
        
        if chave in dados:
            del dados[chave]
    
    with open(caminho,'w',encoding='utf-8') as arquivo:
        json.dump(dados,arquivo,ensure_ascii=False,indent=4)


dados={
    "nome":"João",
    "idade":30,
    "cidade":"São Paulo",
    "habilidades":["Python","Css","C++","JavaScript"],
    "experiencia":"Pleno"
}

caminho=r"C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Praticando\Exemplo_remover.json"
with open(caminho,'w',encoding='utf-8') as arquivo:
    json.dump(dados,arquivo,ensure_ascii=False,indent=4)

chave="idade"
remover(caminho,chave)
print(f'A chave "{chave}" foi removida do arquivo: "{caminho}"')

with open(caminho,'r',encoding='utf-8') as arquivo:
    dados_atualizados=json.load(arquivo)
    print(f'Conteúdo atualizado do arquivo JSON:')
    print(json.dumps(dados_atualizados,ensure_ascii=False,indent=4))
    