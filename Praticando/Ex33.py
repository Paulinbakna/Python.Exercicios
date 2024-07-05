import json

def filtrar_dados(caminho,chave,valor):
    with open(caminho,'r',encoding='utf-8') as arquivo:
        dados=json.load(arquivo)
    
    dados_filtrados={k:v for k , v in dados.items() if v == valor}
    
    caminho_arquivo_filtrado=r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Praticando\dados_filtrados.json'
    
    with open(caminho_arquivo_filtrado,'w',encoding='utf-8') as arquivo:
        json.dump(dados_filtrados,arquivo,ensure_ascii=False,indent=4)
    
    return caminho_arquivo_filtrado


dados={
    "nome":"Carlos",
    "idade":25,
    "cidade":"Rio de Janeiro",
    "habilidades":["Java","Css","C++","JavaScript"],
    "experiencia":'10 anos'
}

caminho=r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Praticando\exemplo.json'
with open(caminho,'w',encoding='utf-8')as arquivo:
    json.dump(dados,arquivo,ensure_ascii=False,indent=4)

chave='experiencia'
valor='10 anos'
caminho_arquivo_filtrado=filtrar_dados(caminho,chave,valor)
print(f'Os dados filtrados foram salvos em {caminho_arquivo_filtrado}')

with open(caminho_arquivo_filtrado,'r',encoding='utf-8') as arquivo:
    arquivo_dados_filtrados= json.load(arquivo)
    print(f'Conteudo do  arquivo Json criado:')
    print(json.dumps(arquivo_dados_filtrados,ensure_ascii=False,indent=4))
    