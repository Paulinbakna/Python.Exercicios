#Verifique se o arquivo "arquivo.txt" existe no diretório atual
import os 

caminho= r'C:\Users\Paulin\Downloads\TESTE'
os.chdir(caminho)
lista=os.listdir()
for i in lista:
    if i == 'arquivo.txt':
        print('Arquivo Encontrado!')
        
