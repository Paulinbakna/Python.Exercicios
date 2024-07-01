import json

dados={"nome":"João",
       "idade":30,
       "cidade":"São Paulo",
       "habilidades":["Python","JavaScript","SQL"]}

#transforma todos os elementos do json emm uma string
dados_json=json.loads(dados)

#Converter dicionarios,listas e tuplas para arquivo json
dados_json=json.dumps(dados)

#gerenciar o espaçamento do arquivo
dados_json=json.dumps(dados,indent=4)

#muda o item que separa as palavras
dados_json=json.dumps(dados,separators=(': ',"="))

#Coloca em ordem alfabetica
dados_json=json.dumps(dados,sort_keys=True)

#Meio para ler um arquivo json 
with open('C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Manipulação_de_Arquivos_e_Erros\dados_manual.json') as f:
    arquivo=json.load(f)


#----------------------------------------------------------------------------------------
dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "habilidades": ["Python", "JavaScript", "SQL"]}

json_str = '{' + ', '.join(f'"{k}": "{v}"' if isinstance(v, str) else f'"{k}": {v}' if isinstance(v, int) else f'"{k}": ["' + '", "'.join(v) + '"]' for k, v in dados.items()) + '}'

open('dados_manual.json', 'w', encoding='utf-8').write(json_str)


