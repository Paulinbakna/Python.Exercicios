#Obtenha o caminho completo do arquivo "arquivo.txt"
import os

caminho=r'C:\Users\Paulin\Downloads\TESTE'
for caminho,diretorio,arquivo in os.walk(caminho):
    print(caminho)
    print(diretorio)
    print(arquivo)
    