Nomes_pessoas=['Joca','Maria','Claudia','Ana','Marcos']

#================ EX1 ==================================================================
with open('EX1.json','r+') as ex1:
    for v,valor in enumerate(ex1):
        print(v+1,valor)


#================ ANOTAÇÕES IMPORTAMTES ================================================
#'w' -> Usado somente para escrever algo(Porem exclui toda vez que algo for mudado)
with open('Nomes_pessoas.txt','w') as arquivo:
    for valor in Nomes_pessoas:
        arquivo.write(str ('Nomes:'+ valor + '\n'))

  
#'a' -> Usado para acrescentar algo(No caso escrever a mesa coisa denovo sem excluir o anterior)
with open('Nomes_pessoas.txt','a') as arquivo:
    for valor in Nomes_pessoas:
        arquivo.write(str ('Nomes:'+ valor + '\n'))


#'r' -> Usado somente para ler algo(Mostra no terminal o que esta escrito no arquivo)
with open('Nomes_pessoas.txt','r') as arquivo:
    for valor in Nomes_pessoas:
        print(valor)

#'r+' -> Usado para ler e escrever algo(No caso ele vai ler todo o arquivo e adicionar a informação no final)
with open('Nomes_pessoas.txt','r+') as arquivo:
    for valor in Nomes_pessoas:
        arquivo.write(str ('Nomes:'+ valor + '\n'))
    arquivo.write('Pedro')

#EX1
#Mostra os nomes e o numero que cada nome representa
with open('Nomes_pessoas.txt','r+') as arquivo:
    for v,valor in enumerate(arquivo):
        print(v+1,valor)


