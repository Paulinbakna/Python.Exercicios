import json

def mesclar_arquivos(caminho1,caminho2,caminho_arquivo_saida):
    with open(caminho1,'r',encoding='utf-8') as arquivo:
        dados1=json.load(arquivo)
    
    with open(caminho2,'r',encoding='utf-8') as arquivo:
        dados2=json.load(arquivo)
    
    dados_mesclados={**dados1,**dados2}
    
    with open(caminho_arquivo_saida,'w',encoding='utf-8') as arquivo:
        json.dump(dados_mesclados,arquivo,ensure_ascii=False,indent=4)
    
dados_exemplo1={
    "nome":"João",
    "idade":35,
    "cidade":"São Paulo"
}

dados_exemplo2={
    "habiblidades": ["Python","CSS","HTML","JavaScript","C++"],
    "experiencia":"5 anos"
}

caminho1=r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Praticando\caminho1.json'
caminho2=r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Praticando\caminho2.json'

with open(caminho1,'w',encoding='utf-8') as arquivo:
    json.dump(dados_exemplo1,arquivo,ensure_ascii=False,indent=4)

with open(caminho2, 'w',encoding='utf-8') as arquivo:
    json.dump(dados_exemplo2,arquivo,ensure_ascii=False,indent=4)

caminho_arquivo_saida=r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Praticando\arquivo_teste.json'

mesclar_arquivos(caminho1,caminho2,caminho_arquivo_saida)

print(f'Os arquivos {caminho1} e {caminho2} foram mesclados')

with open(caminho_arquivo_saida,'r',encoding='utf-8') as arquivo:
    dados_mescaldos=json.load(arquivo)
    print('Conteudo do arquivo JSON mesclado:')
    print(json.dumps(dados_mescaldos,ensure_ascii=False,indent=4))
    