#Renomei o arquivo "arquivo_antigo.txt" para "arquivo_novo.txt"
import os 

caminho=r'C:\Users\Paulin\Downloads\TESTE'
os.chdir(caminho)
os.rename('arquivo_antigo.txt','arquivo_novo.txt')