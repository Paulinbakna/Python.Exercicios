#Crie um diretório chamado "meus_arquivos" no diretorio atual
import os

caminho=r'C:\Users\Paulin\Downloads'
os.chdir(caminho)
os.mkdir('meus_arquivos')
print('Pasta Criada!')
