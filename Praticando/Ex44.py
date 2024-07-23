#Exclua o arquivo "arquivo.txt" do diretório atual
import os

caminho=r'C:\Users\Paulin\Downloads\TESTE'
os.chdir(caminho)
os.remove('arquivo.txt')
print('Arquivo Excluido!')
