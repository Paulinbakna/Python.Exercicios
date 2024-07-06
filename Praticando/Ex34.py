try:
    import json

    def adicionar_par_chave(caminho,chave,valor):
        with open(caminho,'r',encoding='utf-8') as arquivo:
            dados=json.load(arquivo)
            
        dados[chave]=valor
        
        with open(caminho,'r',encoding='utf-8') as arquivo:
            json.dump(dados,arquivo,ensure_ascii=False,indent=4)


    dados_exemplo={
        "nome":"João",
        "idade":25,
        "cidade":"São Paulo",
        "habilidades":["Python","Css","C++","JavaScript"]
    }

    caminho=r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Praticando\arquivo_teste.json'

    with open(caminho,'w',encoding='utf-8')as arquivo:
        json.dump(dados_exemplo,arquivo,ensure_ascii=False,indent=4)

    chave='experiencia'
    valor='Pleno'
    adicionar_par_chave(caminho,chave,valor)
    print(f'A chave "{chave}" com valor "{valor}" foi adicionado ao arquivo "{caminho}"')

    with open(caminho,'r',encoding='utf-8') as arquivo:
        valores=json.load(arquivo)
        print('Conteudo atualizado do arquivo Json')
        print(json.dumps(valores,ensure_ascii=False,indent=4))
except:
    print('Erro Inesperado!')

finally:
    print('-->> O Codigo não apresentou nenhum Error! <<--')
      