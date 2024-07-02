import json


dados={"nome":"João",
       "idade":30,
       "cidade":"São Paulo",
       "habilidades":["Python","JavaScript","SQL"]}

#================ EX2 =============================================
dados_json=json.dumps(dados,ensure_ascii=False)

with open('Ex2.json','w',encoding='utf-8') as ex2:
    ex2.write(dados_json)


#================ANOTAÇÕES IMPORTAMTES=============================
#converte o dicionario para uma string JSON
dados_json=json.dumps(dados,ensure_ascii=False)

#transforma todos os elementos do json emm uma string
dados_json=json.loads(dados)

#Converter dicionarios,listas e tuplas para arquivo json
dados_json=json.dumps(dados)

#converte o dicionario para uma string json porem com indentação para melhor visualização
dados_json=json.dumps(dados,indent=4)

#converte o dicionario para uma string json com separadores personalizados
dados_json=json.dumps(dados,separators=(': ',"="))

#Coloca em ordem alfabetica
dados_json=json.dumps(dados,sort_keys=True)

#tranforma em uma arquivo json e faz com que os " ~ " nao apresente erro
dados_json=json.dumps(dados,ensure_ascii=False)

#Meio para ler um arquivo json\ e necessario colocar o local onde esta o arquivo
with open('C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Manipulação_de_Arquivos_e_Erros\dados_manual.json') as f:
    arquivo=json.load(f)

#cria o arquivo json e coloca os itens presente na lista no arquivo
with open('dados.json','w',encoding='utf-8') as arquivo:
    arquivo.write(dados_json)

#================================================================